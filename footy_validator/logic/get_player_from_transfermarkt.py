import logging
from typing import List, Optional

from bs4 import BeautifulSoup
from footy_validator.dataclasses import (
    FootballPlayerData,
    ClubTeamData,
    NationalTeamData,
)
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
}
BASE_URL = "https://www.transfermarkt.co.uk"

logger = logging.getLogger(__name__)


def get_player(input_player_name: str) -> Optional[FootballPlayerData]:
    teams: List[ClubTeamData] = list()
    national_teams: List[NationalTeamData] = list()

    page = f"{BASE_URL}/schnellsuche/ergebnis/schnellsuche?query={input_player_name}&x=0&y=0"

    search_tree = requests.get(page, headers=HEADERS)
    soup = BeautifulSoup(search_tree.content, "html.parser")
    players = soup.find_all("a", {"class": "spielprofil_tooltip"})
    player_name = players[0] if players else None
    if not player_name:
        logger.info("Player {input_player_name} could not be found.")
        return

    player_url = player_name.attrs.get("href")
    pageTree = requests.get(BASE_URL + player_url, headers=HEADERS)
    pageSoup = BeautifulSoup(pageTree.content, "html.parser")
    transfers = pageSoup.find_all("tr", {"class": "zeile-transfer"})

    for transfer in transfers:
        transfer_table_rows = transfer.findAll("a", {"class": "vereinprofil_tooltip"})

        left_team = transfer_table_rows[2].text
        teams.append(ClubTeamData(name=left_team))

        try:
            joined_team = transfer_table_rows[5].text
            teams.append(ClubTeamData(name=joined_team))
        except IndexError:
            logger.warning(
                "The club table with transfers does not have a fifth column. The player probably retired."
            )
            pass

    national_team_header = pageSoup.find(string="National team career")
    if national_team_header:
        national_team_table = national_team_header.find_parent("div", {"class": "box"})
        all_national_team_links = national_team_table.findAll(
            "a", {"class": "vereinprofil_tooltip"}
        )
        national_teams = [
            NationalTeamData(name=team.text) for team in all_national_team_links
        ]
    player = FootballPlayerData(
        full_name=player_name.text,
        club_teams=teams,
        national_teams=national_teams,
        player_instance=None,
        birthday=None,
        alias="",
    )
    return player
