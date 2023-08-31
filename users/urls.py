from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.SignInAPIView.as_view()),
    path('branch-user/', views.UserBranchSerializer.as_view()),
    path('branch-list/', views.BranchListAPIView.as_view()),
    path('reset-password/', views.ResetPasswordAPIView.as_view()),
    path('forgot-password/', views.ForgotPasswordCreateAPIView.as_view()),
    path('get-username/', views.GetUserNameCreateAPIView.as_view()),

]
