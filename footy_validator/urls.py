from django.urls import path

from .partials import (
    add_to_team,
    get_basic_footballer_information,
    remove_from_team,
    submit_team,
)
from .views import UserSubmissionView, index

urlpatterns = [
    path("", index, name="index"),
    path(
        "submission/<uuid:id>",
        UserSubmissionView.as_view(),
        name="user-submission-view",
    ),
    path("find_player/", get_basic_footballer_information, name="find-player-view"),
    path("add_to_team/", add_to_team, name="add-to-team-view"),
    path("remove_from_team/", remove_from_team, name="remove-from-team-view"),
    path("submit_team/", submit_team, name="submit-team-view"),
]
