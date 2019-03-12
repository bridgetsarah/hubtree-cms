from django.shortcuts import render
from django.views.generic import TemplateView

# create views here ##                                                    #file pulls from urls

class dashboard_home_view(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dashboard.html', context=None)

class projects_view(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'projects.html', context=None )    

class analytics_view(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'analytics.html', context=None )  

class billing_view(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'billing.html', context=None )  




