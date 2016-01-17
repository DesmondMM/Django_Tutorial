from django.conf.urls import include,url
from django.contrib import admin

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^question_list/$', views.QuestionList.as_view(), name='index'),
    url(r'^choice_list/$', views.ChoiceList.as_view()),
    url(r'^question_detail/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(), name='detail'),
    url(r'^choices/(?P<pk>[0-9]+)/$', views.ChoiceDetail.as_view(), name ='choice_text'),
     url(r'^create_choice/$', views.CreateChoice.as_view()),
     url(r'^create_user/$', views.UserCreate.as_view()),
]
