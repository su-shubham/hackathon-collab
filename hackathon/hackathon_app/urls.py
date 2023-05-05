from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="API documentation",
    ),
    public=True,
)


urlpatterns = [
    path("hackathons/", views.HackathonList.as_view()),
    path("hackathons/<int:pk>/", views.HackathonDetail.as_view()),
    path("hackathons/<int:pk>/register/", views.HackathonRegistrationCreate.as_view()),
    path("hackathons/<int:pk>/submissions/", views.SubmissionList.as_view()),
    path("hackathons/submissions/<int:pk>/", views.SubmissionDetail.as_view()),
    path("hackathons/my-hackathons/", views.UserHackathonList.as_view()),
    path("hackathons/my-submissions/", views.UserSubmissionList.as_view()),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
