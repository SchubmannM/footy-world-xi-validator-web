# Generated by Django 4.1.2 on 2022-10-27 14:27

import uuid

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "footy_validator",
            "0002_alter_clubteam_options_alter_footballplayer_options_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="TemporarySubmissionPlayers",
            fields=[
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="footballplayer",
            name="profile_picture_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="footballplayer",
            name="profile_url",
            field=models.URLField(blank=True),
        ),
        migrations.CreateModel(
            name="TemporaryUserSubmission",
            fields=[
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "players",
                    models.ManyToManyField(
                        related_name="temporary_user_submission",
                        through="footy_validator.TemporarySubmissionPlayers",
                        to="footy_validator.footballplayer",
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="temporarysubmissionplayers",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="footy_validator.footballplayer",
            ),
        ),
        migrations.AddField(
            model_name="temporarysubmissionplayers",
            name="temp_user_submission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="footy_validator.temporaryusersubmission",
            ),
        ),
    ]
