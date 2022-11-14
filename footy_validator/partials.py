from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from footy_validator.logic.get_player_from_transfermarkt import get_player_search_result
from footy_validator.logic.squad_validation import validate_user_submission
from footy_validator.models import TemporaryUserSubmission
from footy_validator.models import UserSubmission


@require_POST
@csrf_exempt
def get_basic_footballer_information(request):
    footballer_name = request.POST.get("player_name")
    search_result = get_player_search_result(footballer_name)
    return TemplateResponse(
        request, "partials/player_search_result.html", {"search_result": search_result}
    )


@require_POST
def submit_team(request):
    temp_team_id = request.session.get("temp_submission_id")
    temp_submission = TemporaryUserSubmission.objects.get(id=temp_team_id)
    new_user_submission = UserSubmission.objects.create()
    new_user_submission.players.set(temp_submission.players.all())
    validations = validate_user_submission(new_user_submission)
    is_correct = True
    for validation in validations:
        if validation.reasons_incorrect:
            is_correct = False
    return TemplateResponse(
        request,
        "partials/validations.html",
        {"validations": validations, "is_correct": is_correct},
    )
