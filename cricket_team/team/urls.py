from django.conf.urls import url

from team.views import TeamListView, TeamDetailView, AddTeam


urlpatterns = [
    url(r'^add/$', AddTeam, name='add_team'),
    url(r'^$', TeamListView.as_view(), name='team_list'),
    url(r'^(?P<slug>[\w-]+)/$', TeamDetailView.as_view(), name='team_detail'),
]
