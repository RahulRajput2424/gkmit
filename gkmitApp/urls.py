from django.contrib import admin
from django.urls import path, include
from gkmitApp.views import UserSignupView, UserLoginView, OpenAccount, DepositMoney, WithdrawAmount

urlpatterns = [
    path('user-signup-view/',UserSignupView.as_view()),
    path('user-login-view/',UserLoginView.as_view()),
    path('open-account/',OpenAccount.as_view()),
    path('deposit-money/',DepositMoney.as_view()),
    path('withdraw-money/',WithdrawAmount.as_view()),
]