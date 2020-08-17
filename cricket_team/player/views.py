from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse


from player.models import Player
from player.forms import AddPlayerForm


def PlayerListView(request):
    model = Player
    object_ = Player.objects.all()

    return render(request, "player/player_list.html", {"object_list": object_})


class PlayerDetailView(DetailView):
    model = Player


def AddPlayer(request):
    form = AddPlayerForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            slug = obj.team.slug
            return redirect("team_detail", obj.team.slug)
    else:
        form = AddPlayerForm()
    return render(request, 'player/add_player.html', {'form': form})
