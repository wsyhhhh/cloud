from django.conf.urls import url
from users import views

urlpatterns =[
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.register, name='regist'),
    #url(r'^username/$', views.logout, name='logout'),
    url(r'^username/$', views.username, name='username'),
]
