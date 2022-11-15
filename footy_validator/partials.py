from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.http import require_POST

from footy_validator.logic.get_player_from_transfermarkt import get_player_search_result
from footy_validator.logic.squad_validation import validate_user_submission
from footy_validator.repositories import UserSubmissionRepository


@require_POST
def get_basic_footballer_information(request):
    footballer_name = request.POST.get("player_name")
    search_result = get_player_search_result(footballer_name)
    return TemplateResponse(
        request, "partials/player_search_result.html", {"search_result": search_result}
    )


@require_POST
def submit_team(request):
    temp_team_id = request.session.get("temp_submission_id")
    repository = UserSubmissionRepository()
    user_submission = repository.get_by_id(temp_team_id)
    if not user_submission:
        return HttpResponse(500)
    validations = validate_user_submission(user_submission)
    return TemplateResponse(
        request,
        "partials/validations.html",
        {"validations": validations, "is_correct": len(validations) == 0},
    )
