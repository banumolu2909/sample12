from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

# Route is the App name, eg: crimsonboard web app
# view is the view name, eg: crimsonboard app's view?
# name is the name of the function in the views.py
# urlpatterns = [
#     path(route='api/login', view=views.login, name='crimsonboard_login'),
#     path(route='api/sign_up', view=views.sign_up, name='crimsonboard_signup'), 
# ]

urlpatterns = [
# path('login/',views.login, name='login'),
path('login/', views.Login, name='login'),
path('logout/', views.Logout, name='logout'),
path('',views.home,name="home"),
path('signup/',views.signup, name='signup'),
path('profile/',views.profile, name='profile'),
path('admin/', admin.site.urls),
# path('login/',views.login, name='login'),
]