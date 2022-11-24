import logging
from dataclasses import dataclass
from typing import List
from typing import Optional

import requests
from bs4 import BeautifulSoup

from footy_validator.dataclasses import ClubTeamData
from footy_validator.dataclasses import FootballPlayerData
from footy_validator.dataclasses import NationalTeamData

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
}
BASE_URL = "https://www.transfermarkt.co.uk"

logger = logging.getLogger(__name__)


@dataclass
class PlayerSearchResult:
    player_picture: str
    player_url: str
    player_name: str


def get_soup_from_url(url: str) -> BeautifulSoup:
    search_tree = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(search_tree.content, "html.parser")
    return soup


def get_player_search_result(input_player_name: str) -> Optional[PlayerSearchResult]:
    url = f"{BASE_URL}/schnellsuche/ergebnis/schnellsuche?query={input_player_name}&x=0&y=0"
    soup = get_soup_from_url(url)
    player = soup.find("td", {"class": "hauptlink"})
    if not player:
        logger.info("Player {input_player_name} could not be found.")
        return None
    player_info = player.find_parent("td")
    player_picture: str = player_info.img.get("src")  # type: ignore
    hauptlink = player_info.find("td", "hauptlink")  # type: ignore
    if not hauptlink:
        return None
    player_url: str = hauptlink.a.get("href")  # type: ignore
    player_name: str = hauptlink.a.get("title")  # type: ignore
    return PlayerSearchResult(
        player_picture=player_picture,
        player_url=BASE_URL + player_url,
        player_name=player_name,
    )


def get_player_from_url(player_url: str) -> Optional[FootballPlayerData]:
    teams: List[ClubTeamData] = list()
    national_teams: List[NationalTeamData] = list()
    pageSoup = get_soup_from_url(player_url)
    profile_image = pageSoup.find("img", {"class": "data-header__profile-image"})
    player_name = profile_image.get("alt")
    profile_picture_url = profile_image.get("src")
    all_clubs = pageSoup.find_all(
        "img", {"class": "tm-player-transfer-history-grid__club-logo lazy"}
    )

    for club in all_clubs:
        club_img = ""
        club_name = club.get("alt")
        data_srcset = club.get("data-srcset")
        club_img = (
            data_srcset.strip().replace("\n", "").replace("tiny", "big").split(" ")[0]
        )
        if "_" in club_img:
            # Some teams have something like a hash in their filename - we remove it here.
            first_part, second_part = club_img.split("_")
            _, cleansed_second_part = second_part.split(".")
            club_img = f"{first_part}.{cleansed_second_part}"
        if club_name and club_name != "Retired" and club_name != "Without Club":
            teams.append(ClubTeamData(name=club_name, team_picture_url=club_img))

    national_team_table = pageSoup.find(string="National team career").find_parent(
        "div"
    )
    if national_team_table:
        all_national_teams = national_team_table.find_all(
            "div", {"class": "grid national-career__row"}
        )
        for team in all_national_teams:
            team_img = team.find("img")
            national_team_name = team_img.get("alt")
            team_img = (
                team_img.get("data-src")
                .strip()
                .replace("\n", "")
                .replace("verysmall", "head")
                .split(" ")[0]
            )
            national_teams.append(
                NationalTeamData(name=national_team_name, team_picture_url=team_img)
            )

    player = FootballPlayerData(
        full_name=player_name,
        club_teams=teams,
        national_teams=national_teams,
        player_instance=None,
        birthday=None,
        alias="",
        profile_picture_url=profile_picture_url,
        profile_url=player_url,
    )
    return player
