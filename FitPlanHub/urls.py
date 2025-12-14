"""
URL configuration for FitPlanHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import signup, user_login, logout_user
from plans.views import trainer_dashboard, plan_detail
from subscriptions.views import subscribe
from follows.views import user_feed, follow_trainer, unfollow_trainer
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),

    path('trainer-dashboard/', trainer_dashboard, name='trainer_dashboard'),
    path('plan/<int:id>/', plan_detail, name='plan_detail'),

    path('subscribe/<int:plan_id>/', subscribe, name='subscribe'),
    path('feed/', user_feed, name='user_feed'),

    path('follow/<int:trainer_id>/', follow_trainer, name='follow_trainer'),
    path('unfollow/<int:trainer_id>/', unfollow_trainer, name='unfollow_trainer'),
]
