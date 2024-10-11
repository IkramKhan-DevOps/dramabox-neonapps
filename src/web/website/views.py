from django.shortcuts import render
from django.views.generic import TemplateView

from src.apps.whisper.main import NotificationService


# Create your views here.
class HomeView(TemplateView):
    template_name = 'website/index.html'

class AboutView(TemplateView):
    template_name = 'website/about.html'

class PricingView(TemplateView):
    template_name = 'website/pricing.html'

class ContactUs(TemplateView):
    template_name = 'website/contact.html'