from django.conf.urls import url
from vm import views

urlpatterns =[
    #url(r'^$', views.login, name='login'),
    url(r'^virtualhost/$', views.virtualhost, name='virtualhost'),
    url(r'^apply_vm/$', views.apply_vm, name='apply_vm'),
]
