from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

        
"""class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('accounts/login'))
"""
@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('/registration/login'))