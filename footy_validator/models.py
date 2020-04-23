from django_extensions.db.models import TimeStampedModel
from django.db import models
import uuid


class NationalTeam(TimeStampedModel):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=300)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]


class ClubTeam(TimeStampedModel):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=300)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]


class FootballPlayer(TimeStampedModel):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    full_name = models.CharField(max_length=300)
    birthday = models.DateField(null=True)
    alias = models.CharField(max_length=300, blank=True)
    national_teams = models.ManyToManyField(NationalTeam, related_name="players")
    club_teams = models.ManyToManyField(ClubTeam, related_name="players")

    def __str__(self):
        return self.full_name

    class Meta:
        indexes = [
            models.Index(fields=["full_name"]),
            models.Index(fields=["alias"]),
        ]


class UserSubmission(TimeStampedModel):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    players = models.ManyToManyField(FootballPlayer, related_name="user_submissions")
    reason_incorrect = models.TextField(blank=True)

    @property
    def is_correct(self):
        if self.reason_incorrect:
            return False
        return True

    @classmethod
    def validate(cls, instance):
        from .logic.squad_validation import validate_user_submission

        user_submission_instance = UserSubmission.objects.prefetch_related(
            "players__club_teams", "players__national_teams"
        ).filter(id=instance.id)[0]
        validations: List[UserSubmissionValidation] = validate_user_submission(
            user_submission_instance
        )
        user_submission_instance.reason_incorrect = "<br />".join(
            validation.reason_incorrect for validation in validations
        )
        user_submission_instance.save(update_fields=["modified", "reason_incorrect"])
        return user_submission_instance
