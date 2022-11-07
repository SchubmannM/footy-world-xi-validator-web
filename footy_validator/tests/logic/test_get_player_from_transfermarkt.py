from footy_validator.dataclasses import ClubTeamData
from footy_validator.dataclasses import FootballPlayerData
from footy_validator.dataclasses import NationalTeamData
from footy_validator.logic.get_player_from_transfermarkt import get_player_from_url
from footy_validator.logic.get_player_from_transfermarkt import get_player_search_result


def test_get_player_search_result(mocker, search_result_soup):
    mocker.patch(
        "footy_validator.logic.get_player_from_transfermarkt.get_soup_from_url",
        return_value=search_result_soup,
    )
    input_player_name = "Thomas Müller"
    search_result = get_player_search_result(input_player_name)
    assert (
        search_result.player_picture
        == "https://img.a.transfermarkt.technology/portrait/small/58358-1667830486.jpg?lm=1"
    )
    assert (
        search_result.player_url
        == "https://www.transfermarkt.co.uk/thomas-muller/profil/spieler/58358"
    )
    assert search_result.player_name == "Thomas Müller"


def test_get_player_from_url(mocker, detailed_view_soup):
    mocker.patch(
        "footy_validator.logic.get_player_from_transfermarkt.get_soup_from_url",
        return_value=detailed_view_soup,
    )
    url = "https://www.transfermarkt.co.uk/thomas-muller/profil/spieler/58358"
    detailed_view_result: FootballPlayerData = get_player_from_url(url)  # type: ignore
    assert detailed_view_result.player_instance is None
    assert detailed_view_result.full_name == "Thomas Müller"
    assert detailed_view_result.birthday is None
    assert detailed_view_result.alias == ""
    assert (
        detailed_view_result.profile_picture_url
        == "https://img.a.transfermarkt.technology/portrait/header/58358-1667830486.jpg?lm=1"
    )
    assert (
        detailed_view_result.profile_url
        == "https://www.transfermarkt.co.uk/thomas-muller/profil/spieler/58358"
    )
    assert detailed_view_result.club_teams == [
        ClubTeamData(name="FC Bayern II"),
        ClubTeamData(name="Bayern Munich"),
        ClubTeamData(name="FC Bayern U19"),
        ClubTeamData(name="FC Bayern II"),
        ClubTeamData(name="FC Bayern U17"),
        ClubTeamData(name="FC Bayern U19"),
        ClubTeamData(name="B. München Yth."),
        ClubTeamData(name="FC Bayern U17"),
        ClubTeamData(name="TSV Pähl Yth."),
        ClubTeamData(name="B. München Yth."),
    ]
    assert detailed_view_result.national_teams == [
        NationalTeamData(name="Germany"),
        NationalTeamData(name="Germany"),
        NationalTeamData(name="Germany"),
        NationalTeamData(name="Germany"),
        NationalTeamData(name="Germany"),
    ]
