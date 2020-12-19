from django.contrib import admin
from django.urls import path, include
from gkmitApp.views import UserSignupView

urlpatterns = [
    path('user-signup-view/',UserSignupView.as_view()),

]