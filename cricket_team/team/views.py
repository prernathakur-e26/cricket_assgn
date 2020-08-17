from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from team.models import Team
from player.models import Player
from team.forms import AddTeamForm


class TeamListView(ListView):
    model = Team
    queryset = Team.objects.all()
    # template_name = "team/list.html"


class TeamDetailView(DetailView):
    model = Team

    def get_context_data(self, *args, **kwargs):
        context = super(TeamDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        players = Player.objects.filter(team=obj)
        context["players"] = players
        return context


def AddTeam(request):
    form = AddTeamForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            return redirect("team_list")
    else:
        form = AddTeamForm()
    return render(request, 'team/add_team.html', {'form': form})
