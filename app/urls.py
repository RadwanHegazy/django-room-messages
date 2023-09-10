from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views


urlpatterns = [


    # chating
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),


    # authentication
    path('login',LoginView.as_view(template_name='auth/login.html'),name='login'),
    path('register',views.register,name='register'),
    path('logout',LogoutView.as_view()),
]