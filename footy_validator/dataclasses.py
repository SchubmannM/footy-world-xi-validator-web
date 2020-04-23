from dataclasses import dataclass, field
from typing import List, Optional
from .models import ClubTeam, FootballPlayer, NationalTeam, UserSubmission


@dataclass
class ClubTeamData:
    name: Optional[str]

    def to_instance(self) -> ClubTeam:
        team, _ = ClubTeam.objects.get_or_create(name=self.name)
        return team


@dataclass
class NationalTeamData:
    name: Optional[str]

    def to_instance(self) -> NationalTeam:
        team, _ = NationalTeam.objects.get_or_create(name=self.name)
        return team


@dataclass
class FootballPlayerData:
    player_instance: Optional[FootballPlayer]
    full_name: Optional[str]
    birthday: Optional[str]
    alias: Optional[str]

    club_teams: List[ClubTeamData] = field(default_factory=list)
    national_teams: List[NationalTeamData] = field(default_factory=list)

    @classmethod
    def from_instance(cls, player: FootballPlayer) -> "FootballPlayerData":
        return FootballPlayerData(
            player_instance=player,
            full_name=player.full_name,
            birthday=player.birthday,
            alias=player.alias,
            club_teams=list(player.club_teams.values_list("name", flat=True)),
            national_teams=list(player.national_teams.values_list("name", flat=True)),
        )

    def to_instance(self) -> FootballPlayer:
        player, created = FootballPlayer.objects.get_or_create(full_name=self.full_name)
        if created:
            club_teams = [team.to_instance() for team in self.club_teams]
            national_teams = [team.to_instance() for team in self.national_teams]
            player.club_teams.add(*club_teams)
            player.national_teams.add(*national_teams)
        return player


@dataclass
class UserSubmissionValidation:
    reason_incorrect: Optional[str]


@dataclass
class UserSubmissionData:
    players: List[FootballPlayerData] = field(default_factory=list)

    def to_instance(self) -> UserSubmission:
        user_submission_instance = UserSubmission.objects.create()
        for player in self.players:
            if player.player_instance:
                user_submission_instance.players.add(player.player_instance)
            else:
                player_instance = player.to_instance()
                user_submission_instance.players.add(player_instance)
        user_submission_instance = UserSubmission.validate(user_submission_instance)
        return user_submission_instance
