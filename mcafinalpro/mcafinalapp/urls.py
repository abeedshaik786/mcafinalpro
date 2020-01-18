from django.urls import path
from . import views

urlpatterns = [
    path('LoginForm',views.LoginForm),
    path('rigistration',views.rigistration,name='rigistration'),
    path('user_saving',views.user_saving,name='user_saving'),
    path('Login/',views.Login,name='Login'),
    path('CompanyRequrment',views.CompanyRequrment,name='CompanyRequrment'),
    path('jobapply',views.jobapply,name='jobapply')

]
