from django.urls import path

from users.views import SignUpView, SignInView, UserView

urlpatterns = [
    path("/signup", SignUpView.as_view()),
    path("/signin", SignInView.as_view()),
    path("/user", UserView.as_view())
]