from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.SignInAPIView.as_view()),
    path('branch-user/', views.BranchListAPIView.as_view()),
    path('branch-list/', views.UserBranchSerializer.as_view()),
    path('reset-password/', views.ResetPasswordAPIView.as_view())
]
