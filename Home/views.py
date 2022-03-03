from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from Home.forms import SignUpForm, LoginForm, EditUserForm
from Home.models import Profile


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            profile = Profile.objects.get_or_create(user=request.user)
            return HttpResponseRedirect(reverse('Home:home'))
    else:
        form = SignUpForm()
    return render(request, 'Home/sign_up.html', {'form': form})


def login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                error = 'username or password is wrong'
            else:
                login(request, user)
                return HttpResponseRedirect(reverse('Game:home'))
    else:
        form = LoginForm()
    context = {'form': form, 'error': error}
    return render(request, 'Home/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Game:home'))


@login_required
def edit_user(request):
    user = request.user
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Game:home'))
    else:
        form = EditUserForm(instance=request.user)
    return render(request, 'Home/edit_user.html', {'user': user, 'form': form})
