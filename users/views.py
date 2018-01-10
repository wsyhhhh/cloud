#coding=utf-8
from django.views.generic.base import View
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from users.models import user
import time
import json
# Create your views here.


class IndexView(View):
    def get(self,request):
        #取得cookie中的用户名
        #user = request.get_signed_cookie('username',salt="cloud")
        #return render_to_response("index.html",{'username':user})
        return render_to_response("index.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        userResult = user.objects.filter(username=username,password=password)
        if (len(userResult)>0):
            #登陆成功
            st = 1
            response = HttpResponse(json.dumps({"st": st}), content_type="application/json")
            #设置cookies,加盐，后续考虑加密
            response.set_signed_cookie('username', username,salt="cloud",expires=3600,max_age=3600)
            return response
        else:
            st = 0
            # 返回登陆失败页面
            response = HttpResponse(json.dumps({"st": st}), content_type="application/json")
            return response

    else:
        st = 2
        return render_to_response("login.html",{"st": st})

#登出
def logout(request):
    response = render_to_response("login.html")
    response.delete_cookie('username')
    return response

#用户名重复
def username(request):
    #GET方法获取表单
    if request.method == "GET":
        user_rec = request.GET.get('fieldId')
        user_name=request.GET.get('fieldValue')
        filterResult = user.objects.filter(username=user_name)
        result=[0,0,0]
        result[0]=user_rec
        #用户名存在
        if len(filterResult) > 0:
            result[1] = False
            print(result)
            result=json.dumps(result)
            return HttpResponse(result, content_type="application/json")
        else:
            #用户名不存在
            result[1] = True
            print(result)
            result = json.dumps(result)
            return HttpResponse(result, content_type="application/json")
    else:
        result = [0,0,0]
        result[1] = False
        result = json.dumps(result)
        return HttpResponse(result, content_type="application/json")
        #uf = UserForm()
        #return render_to_response("registe.html", {'uf': uf})

#注册
def register(request):
    #curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());
    curtime = time.time()
    if request.method == "POST":
        #获取表单信息
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        reg_time = curtime
        #检查用户名是否重复
        filterResult = user.objects.filter(username=username)
        #用户名重复返回错误
        if len(filterResult) > 0:
            st = 0
            return HttpResponse(json.dumps({"st": st}), content_type="application/json")
        else:
            #写数据库
            User = user.objects.create(username=username,password=password,email=email,reg_time=reg_time)
            print(User.id)
            User.save()
            st=1
            # 返回注册成功页面
            return HttpResponse(json.dumps({"st":st}),content_type="application/json")
    else:
        st=2
        return render_to_response('registe.html',{'st':st})



