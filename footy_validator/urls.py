from django.urls import path

from .views import index, UserSubmissionView

urlpatterns = [
    path("", index, name="index"),
    path(
        "submission/<uuid:id>",
        UserSubmissionView.as_view(),
        name="user-submission-view",
    ),
]
