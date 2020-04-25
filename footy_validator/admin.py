from django.contrib import admin
from .models import FootballPlayer, NationalTeam, ClubTeam, UserSubmission
from django.db.models import Count


@admin.register(NationalTeam)
class NationalTeamAdmin(admin.ModelAdmin):
    fields = ("name",)
    search_fields = ("name",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ClubTeam)
class ClubTeamAdmin(admin.ModelAdmin):
    fields = ("name",)
    search_fields = ("name",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FootballPlayer)
class FootballPlayerAdmin(admin.ModelAdmin):
    fields = ("id", "created", "modified", "full_name", "national_teams", "club_teams")
    readonly_fields = (
        "id",
        "created",
        "modified",
    )
    search_fields = ("full_name",)
    list_display = (
        "full_name",
        "created",
        "no_of_occurrences",
    )
    list_filter = ("national_teams", "club_teams")
    autocomplete_fields = ["national_teams", "club_teams"]

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .annotate(no_of_occurrences=Count("user_submissions"))
        )

    def no_of_occurrences(self, obj):
        return obj.no_of_occurrences

    no_of_occurrences.admin_order_field = "no_of_occurrences"

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    fields = ("id", "created", "modified", "players", "reason_incorrect")
    readonly_fields = (
        "id",
        "created",
        "modified",
    )
    search_fields = ("players",)
    autocomplete_fields = [
        "players",
    ]
    list_display = ("id", "created", "is_correct")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
