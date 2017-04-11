from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/n/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/n/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/n/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
