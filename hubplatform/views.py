from django.urls import path
from django.views.generic import TemplateView


# Dashboard Patterns
urlpatterns = [
    path('dashboard/', TemplateView.as_view(template_name="about.html")),
    path('dashboard/admin', TemplateView.as_view(template_name="admin.html")),
    path('dashboard/account', TemplateView.as_view(template_name="account.html")),
    path('dashboard/analytics', TemplateView.as_view(template_name="analytics.html")),
    path('dashboard/billing', TemplateView.as_view(template_name="billing.html")),
    path('dashboard/user', TemplateView.as_view(template_name="users.html")),
]
# Client Dashboard Patterns
urlpatterns = [
    path('dashboard/user/dash', TemplateView.as_view(template_name="about.html")),
    path('dashboard/user/project', TemplateView.as_view(template_name="about.html")),
    path('dashboard/user/anayltics', TemplateView.as_view(template_name="about.html")),
    path('dashboard/user/billing', TemplateView.as_view(template_name="about.html")),
    path('dashboard/user/user', TemplateView.as_view(template_name="about.html")),
]