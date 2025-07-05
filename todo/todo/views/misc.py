from django.shortcuts import redirect, render
from django.views.generic import View
__all__ = ('HomeView',)

class HomeView(View):
    """
    A simple view that renders the home page.
    """
    template_name = 'home.html'
    def get(self, request):
        """
        Handle GET requests to the home page.
        """
        return render(request, self.template_name, {
            'name': 'Birendra kumar',
            'occupation': 'software engineer',
        })