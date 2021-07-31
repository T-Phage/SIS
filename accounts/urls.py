from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'accounts'

urlpatterns = [
    path('changepassword/', views.changepassword, name='changepassword'),
    path('editprofile/', views.editprofile, name='editprofile'),
    # path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('login/', views.loginform, name='loginform'),
    # path('successfullysent/', views.successfullysent, name='successfullysent'),
    path('signup/', views.signupform, name='signupform'),
    path('gaurdian_ajax/', views.guardian_ajax, name='guardian_ajax'),
    path('student_ajax/', views.student_ajax, name='student_ajax'),
    path('signout/', views.signout, name='signout'),

    path('forgetpassword/', auth_views.PasswordResetView.as_view(template_name='accounts/forgetpassword.html'), name='forgetpassword'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/succesfullysent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_complete.html'), name='password_reset_complete'),

    path('doesuserexists/', views.doesuserexists, name='doesuserexists'),
    path('doesemailexists/', views.doesemailexists, name='doesemailexists'),
]
