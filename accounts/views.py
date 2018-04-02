from django.shortcuts import render, render_to_response
from django.urls  import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from django.views import generic
# Create your views here.
from .models import User
from .forms import SignUpForm

class SignUp(generic.CreateView):
	form_class = SignUpForm
	succcess_url = reverse_lazy('cloned:login')
	template_name = 'signup.html'

# def login_user(request):
# 	logout(request)
# 	username = password = ''
# 	if username.POST:
# 		username = request.POST['username']
# 		password = request.POST['password']

# 		user = authenticate(username=username, password=password)
# 		if user is not None:
# 			if user.is_active:
# 				login(request, user)
# 				return reverse_lazy('cloned:home')
# 	return render_to_response('accounts:login', context_instance=RequestContext(request))