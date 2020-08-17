from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from match.forms import AddMatchForm
from match.models import Points, Match
# Create your views here.

# class MatchListView(ListView):
#     model = Match
#     queryset = Match.objects.all()
#     template_name = "match/match_list.html"

def MatchListView(request):
    model = Match
    object_ = Match.objects.all()

    return render(request, "match/match_list.html", {"object_list":object_})


class MatchDetailView(DetailView):
    model = Match

def add_match(request):
    form = AddMatchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            team1_score = form.cleaned_data["team_1_score"]
            team2_score = form.cleaned_data["team_2_score"]
            obj = form.save()
            if team1_score > team2_score:
                obj.winner = obj.team_1
            else:
                obj.winner = obj.team_2
            
            score = Points()
            score.team1 = team1_score
            score.team2 = team2_score
            score.save()

            obj.score = score
            obj.save()

            return redirect("match_list")
    else:
        form = AddMatchForm()
    return render(request, 'match/add.html', {'form': form})



