from typing import Optional
from uuid import UUID

from footy_validator import models
from footy_validator.converters import convert_user_submission
from footy_validator.dataclasses import UserSubmissionData
from footy_validator.repository import BaseDjangoRepository


class UserSubmissionRepository(BaseDjangoRepository):
    def get_by_id(self, id: UUID) -> Optional[UserSubmissionData]:
        user_submission = (
            models.TemporaryUserSubmission.objects.prefetch_related(
                "players", "players__club_teams", "players__national_teams"
            )
            .filter(id=id)
            .first()
        )
        if not user_submission:
            return None

        return convert_user_submission(user_submission)
