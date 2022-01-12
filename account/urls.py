from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.rps, name='rps'),
    path('register/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='account/login.html')),
    path('logout/', LogoutView.as_view()),
    path('rps_play', views.rps_play)
]