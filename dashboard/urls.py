from django.urls import path

from . import views

# URL Path patterns for Dashboard (Admin area)

urlpatterns = [
    path('dashboard/account, views.dashboard_account'),
    path('dashboard/analytics, views.dashboard_analytics'),
    path('dashboard/projects, views.dashboard_projects'),
    path('dashboard/biling, views.dashboard_billing'),
    path('dashboard/users, views.dashboard_users'),
]

# URL Path patterns for Dashboard Client (area)
urlpatterns = [
    path('dashboard/client, views.dashboard/client'),
    path('dashboard/client/analytics, views.dashboard/client/analytics'),
    path('dashboard/client/projects, views.dashboard/client/projects'),
    path('dashboard/client/biling, views.dashboard/client/billing'),
    path('dashboard/client/user, views.dashboard/client/user'),
]