from django.contrib import admin
from django.urls import path, include
from gkmitApp.views import UserSignupView, UserLoginView, OpenAccount

urlpatterns = [
    path('user-signup-view/',UserSignupView.as_view()),
    path('user-login-view/',UserLoginView.as_view()),
    path('open-account/',OpenAccount.as_view()),

]