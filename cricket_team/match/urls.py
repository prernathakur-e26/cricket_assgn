from django.conf.urls import url

from match.views import add_match, MatchDetailView, MatchListView

urlpatterns = [
    url(r'^add/$', add_match, name='add_match'),
    url(r'^$', MatchListView, name='match_list'),
    url(r'^(?P<pk>\d+)/$', MatchDetailView.as_view(), name='match_detail'),
]
