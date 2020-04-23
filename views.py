from uuid import UUID

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.views.generic import DetailView, ListView

from quiz.models import QuizAnswer, QuizQuestion

from .helpers import get_next_question_id, get_previous_question_id
from .models import JurisprudenceQuiz


class QuizListView(ListView):
    queryset = JurisprudenceQuiz.objects.select_related("jurisprudence_text").order_by(
        "created"
    )
    template_name = "quiz/quiz_list.html"


class QuizDetailView(DetailView):
    queryset = JurisprudenceQuiz.objects.all()
    template_name = "quiz/quiz_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "quiz"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jurisprudence"] = self.object.jurisprudence_text
        return context


class QuizTextDetailView(DetailView):
    queryset = JurisprudenceQuiz.objects.all()
    template_name = "quiz/quiz_text_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "quiz"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jurisprudence"] = self.object.jurisprudence_text
        return context


class QuizQuestionDetailView(DetailView):
    queryset = QuizQuestion.objects.select_related("jurisprudence_quiz")
    template_name = "quiz/quiz_question_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz = self.object.jurisprudence_quiz
        current_question = self.object
        context = _get_navigation_context(context, current_question)
        return context


def _get_navigation_context(context: dict, current_question: QuizQuestion):
    context["next_question_id"] = get_next_question_id(current_question)
    context["previous_question_id"] = get_previous_question_id(current_question)
    return context


def start_quiz(request, id: UUID):
    quiz = get_object_or_404(JurisprudenceQuiz, id=id)
    first_question = quiz.questions.first()
    if first_question:
        return redirect("quiz-question-detail", id=first_question.id)
    else:
        return HttpResponse("This quiz does not have any questions.", status=404)


def validate_answer_for_question(request, question_id: UUID, answer_id: UUID):
    """
    Validates a given answer for a given question.
    A question has many possible answers, but only one correct one.
    This API is called with the answer that the user chose, so we check if this is the
    right one - and if not return the correct one and an explanation why that is the case
    (usually in form of a snippet of the actual text)
    """
    question = get_object_or_404(
        QuizQuestion.objects.select_related("jurisprudence_quiz"), id=question_id
    )
    answer = get_object_or_404(QuizAnswer, id=answer_id)
    template_name = "quiz/quiz_question_answer_selected.html"
    context = {
        "question": question,
        "chosen_answer": answer,
        "quiz": question.jurisprudence_quiz,
    }
    context = _get_navigation_context(context, question)
    return TemplateResponse(request=request, template=template_name, context=context)
