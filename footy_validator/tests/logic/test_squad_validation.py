import pytest

from footy_validator.logic.squad_validation import validate_user_submission

pytestmark = pytest.mark.django_db


def test_validate_user_submission_correct_if_different_club_teams(
    user_submission_factory, football_player_factory, club_team_factory
):
    user_submission = user_submission_factory()
    bayern = club_team_factory(name="Bayern Munich")
    barca = club_team_factory(name="FC Barcelona")
    muller = football_player_factory(full_name="Thomas Müller")
    muller.club_teams.add(bayern)
    lewandowski = football_player_factory(full_name="Robert Lewandowski")
    lewandowski.club_teams.add(barca)
    user_submission.players.set([muller, lewandowski])

    validation_results = validate_user_submission(user_submission)
    assert len(validation_results) == 2  # 2 Players in total
    incorrect_result = [
        result for result in validation_results if result.reasons_incorrect != []
    ]
    assert len(incorrect_result) == 0  # 0 of them have conflicts


def test_validate_user_submission_incorrect_if_same_club_teams(
    user_submission_factory, football_player_factory, club_team_factory
):
    user_submission = user_submission_factory()
    bayern = club_team_factory(name="Bayern Munich")
    barca = club_team_factory(name="FC Barcelona")
    muller = football_player_factory(full_name="Thomas Müller")
    muller.club_teams.add(bayern)
    lewandowski = football_player_factory(full_name="Robert Lewandowski")
    lewandowski.club_teams.add(barca)
    lewandowski.club_teams.add(bayern)  # Also played for Bayern -> Conflict
    user_submission.players.set([muller, lewandowski])

    validation_results = validate_user_submission(user_submission)
    assert len(validation_results) == 2  # 2 Players in total
    incorrect_result = [
        result for result in validation_results if result.reasons_incorrect != []
    ]
    assert len(incorrect_result) == 1  # 0 of them have conflicts
    assert incorrect_result[0].reasons_incorrect == [
        " played for Bayern Munich. Robert Lewandowski also played there."
    ]


def test_validate_user_submission_correct_if_different_national_teams(
    user_submission_factory, football_player_factory, national_team_factory
):
    user_submission = user_submission_factory()
    germany = national_team_factory(name="Germany")
    poland = national_team_factory(name="Poland")
    muller = football_player_factory(full_name="Thomas Müller")
    muller.national_teams.add(germany)
    lewandowski = football_player_factory(full_name="Robert Lewandowski")
    lewandowski.national_teams.add(poland)
    user_submission.players.set([muller, lewandowski])

    validation_results = validate_user_submission(user_submission)
    assert len(validation_results) == 2  # 2 Players in total
    incorrect_result = [
        result for result in validation_results if result.reasons_incorrect != []
    ]
    assert len(incorrect_result) == 0  # 0 of them have conflicts


def test_validate_user_submission_incorrect_if_same_national_teams(
    user_submission_factory, football_player_factory, national_team_factory
):
    user_submission = user_submission_factory()
    germany = national_team_factory(name="Germany")
    muller = football_player_factory(full_name="Thomas Müller")
    muller.national_teams.add(germany)
    schweinsteiger = football_player_factory(full_name="Bastian Schweinsteiger")
    schweinsteiger.national_teams.add(germany)
    user_submission.players.set([muller, schweinsteiger])

    validation_results = validate_user_submission(user_submission)
    assert len(validation_results) == 2  # 2 Players in total
    incorrect_result = [
        result for result in validation_results if result.reasons_incorrect != []
    ]
    assert len(incorrect_result) == 1  # 0 of them have conflicts
    assert incorrect_result[0].reasons_incorrect == [
        " played for Germany. Bastian Schweinsteiger also played there."
    ]


def test_validate_user_submission_incorrect_if_same_national_teams_and_club_team(
    user_submission_factory,
    football_player_factory,
    national_team_factory,
    club_team_factory,
):
    user_submission = user_submission_factory()
    germany = national_team_factory(name="Germany")
    bayern = club_team_factory(name="Bayern Munich")
    muller = football_player_factory(full_name="Thomas Müller")
    muller.national_teams.add(germany)
    muller.club_teams.add(bayern)
    schweinsteiger = football_player_factory(full_name="Bastian Schweinsteiger")
    schweinsteiger.national_teams.add(germany)
    schweinsteiger.club_teams.add(bayern)
    user_submission.players.set([muller, schweinsteiger])

    validation_results = validate_user_submission(user_submission)
    assert len(validation_results) == 2  # 2 Players in total
    incorrect_result = [
        result for result in validation_results if result.reasons_incorrect != []
    ]
    assert len(incorrect_result) == 1  # 0 of them have conflicts
    assert incorrect_result[0].reasons_incorrect == [
        " played for Bayern Munich. Bastian Schweinsteiger also played there.",
        " played for Germany. Bastian Schweinsteiger also played there.",
    ]


def test_validate_user_submission_incorrect_and_only_shows_conflicts(
    user_submission_factory,
    football_player_factory,
    national_team_factory,
    club_team_factory,
):
    user_submission = user_submission_factory()
    germany = national_team_factory(name="Germany")
    bayern = club_team_factory(name="Bayern Munich")
    manchester = club_team_factory(name="Manchester United")
    chicago = club_team_factory(name="Chicago Fire")
    muller = football_player_factory(full_name="Thomas Müller")
    muller.national_teams.add(germany)
    muller.club_teams.add(bayern)
    schweinsteiger = football_player_factory(full_name="Bastian Schweinsteiger")
    schweinsteiger.national_teams.add(germany)
    schweinsteiger.club_teams.add(bayern)
    schweinsteiger.club_teams.add(manchester)
    schweinsteiger.club_teams.add(chicago)
    user_submission.players.set([muller, schweinsteiger])

    validation_results = validate_user_submission(user_submission)
    assert len(validation_results) == 2  # 2 Players in total
    incorrect_result = [
        result for result in validation_results if result.reasons_incorrect != []
    ]
    assert len(incorrect_result) == 1  # 0 of them have conflicts
    assert incorrect_result[0].reasons_incorrect == [
        " played for Bayern Munich. Bastian Schweinsteiger also played there.",
        " played for Germany. Bastian Schweinsteiger also played there.",
    ]
