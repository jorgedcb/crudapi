from django.urls import path
from django.views.generic import TemplateView

app_name = 'crud'

urlpatterns = [
    path('', TemplateView.as_view(template_name="crud/index.html")),
]