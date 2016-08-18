from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Game
from .forms import GameForm
import wikipedia

# Create your views here.

def home(request):
    first5games = Game.objects.all()[0:5]
    template = 'base.html'
    return render(request, template, {'first5games' : first5games})


def new_game(request):
	if request.method == 'POST':
		form = GameForm(request.POST, request.FILES)
		if form.is_valid():
			game = form.save()
			game.cover = request.FILES['cover']
			form.cleaned_data
			game.save()
			return redirect("/")
	else:
		form = GameForm()
	return render(request, 'new_game.html', {'form': form})

def game_profile(request, name):
	game_profiles = get_object_or_404(Game, name=name)
	user = request.user
	game_users = game_profiles.users.all()
	if(request.POST.get('add')):
		game_profiles.users.add(user)
		# This is a redirect to the same page. Needs AJAX
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	if(request.POST.get('del')):
		game_profiles.users.remove(user)
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	return render(request, 'game_profile.html', locals())

def profile(request):
	user = request.user
	games = Game.objects.all()
	game_list = []
	number_of_games = 0
	for x in games:
		if user in x.users.all():
			game_list.append(x)
			number_of_games += 1
	return render(request, 'profile.html', locals())

def all_profiles(request, username):
	profiles = get_object_or_404(User, username=username)
	if request.user.username == username:
		return HttpResponseRedirect("/accounts/profile")
	else:
		return render(request, 'user_profile.html', {'profiles': profiles})

def wiki_test(request):
	page = wikipedia.page("Jurassic Park", preload=True)
	img_link = page.images
	contents = page.summary
	print(img_link)
	return render(request, 'wiki.html', locals())


