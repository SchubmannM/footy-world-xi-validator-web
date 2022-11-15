from django.urls import path

from .partials import get_basic_footballer_information
from .partials import submit_team
from .views import football_team
from .views import index
from .views import player_search
from .views import player_validation_form

urlpatterns = [
    path("", index, name="index"),
    path("football_team/", football_team, name="football-team"),
    path("player_search/", player_search, name="player-search"),
    path("find_player/", get_basic_footballer_information, name="find-player-view"),
    path("submit_team/", submit_team, name="submit-team-view"),
    path(
        "player_validation_form/", player_validation_form, name="player-validation-form"
    ),
]
