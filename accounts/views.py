from django.shortcuts import render, render_to_response
from django.urls  import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib import messages

from braces import views
# Create your views here.
from .models import User, Connection
from .forms import SignUpForm, UserChangeForm, ChangePasswordForm
from .funcs import get_logon_user

class SignUpView(generic.CreateView, views.FormValidMessageMixin):
    form_class = SignUpForm
    form_valid_message = 'Successfully created your account, ' \
                         'go ahead and login.'
    succcess_url = reverse_lazy('cloned:login')
    template_name = 'accounts/signup.html'


class DetailAccountView(views.LoginRequiredMixin, generic.DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg ='username'
    template_name = 'accounts/account_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailAccountView, self).get_context_data(**kwargs)
        username = self.kwargs.get('username')
        context['user'] = get_logon_user(self.request)
        context['username'] = username
        context['following'] = Connection.objects.filter(
            follower__username=username).count()
        context['followers'] = Connection.objects.filter(
            following__username=username).count()

        if username is not context['user'].username:
            result = Connection.objects.filter(
                follower__username=context['user'].username
            ).filter(
                following__username=username
            )

            context['connected'] = True if result else False

        return context



class UpdateAccountView(views.LoginRequiredMixin,
    generic.UpdateView,
    views.FormValidMessageMixin):
    model = User
    form_class = UserChangeForm
    form_valid_message = 'Successfully updated your account, ' \
                         'go ahead and login.'
    succcess_url = reverse_lazy('cloned:login')
    template_name = 'accounts/account_update.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

class ChangePasswordView(views.LoginRequiredMixin,
    generic.FormView,
    views.FormValidMessageMixin):
    form_class = ChangePasswordForm
    form_valid_message = 'Password was changed Successfully, ' \
                         'go ahead and login.'

    def form_valid(self, form):
        self.request.user.set_password(form.cleaned_data['new_password'])
        self.request.user.save()

        return super(ChangePasswordView, self).form_valid(form)


class FollowersListView(views.LoginRequiredMixin, generic.ListView):
    model = Connection
    template_name = 'accounts/connections.html'
    context_object_name = 'users'

    def get_queryset(self):
        username = self.kwargs['username']
        return Connection.objects.filter(following__username=username)

    def get_context_data(self):
        context = super(FollowersListView, self).get_context_data()
        context['mode'] = 'followers'
        return context

class FollowingListView(views.LoginRequiredMixin, generic.ListView):
    model = Connection
    template_name = 'accounts/connections.html'
    context_object_name = 'users'

    def get_queryset(self):
        username = self.kwargs['username']
        return Connection.objects.filter(following__username=username)

    def get_context_data(self):
        context = super(FollowersListView, self).get_context_data()
        context['mode'] = 'following'
        return context


