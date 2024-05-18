# myapp/middleware.py

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        # Check if the requested URL requires authentication
        if not request.user.is_authenticated and request.path != reverse('login') and not request.path.startswith(settings.STATIC_URL):
            # Redirect to the login page
            return HttpResponseRedirect(reverse('login'))
        return None
