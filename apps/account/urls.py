from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import logout_then_login, LoginView

app_name = "account"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signout/", logout_then_login, name="signout"),
    path(
        "signin/", LoginView.as_view(template_name="account/signin.html"), name="signin"
    ),
]
