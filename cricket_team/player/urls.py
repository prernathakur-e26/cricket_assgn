from django.conf.urls import url

from player.views import AddPlayer, PlayerListView, PlayerDetailView


urlpatterns = [
    url(r'^all/$', PlayerListView, name='player_list'),
    url(r'^add/$', AddPlayer, name='add_player'),
    url(r'^(?P<slug>[\w-]+)/$',
        PlayerDetailView.as_view(), name='player_detail'),
]
