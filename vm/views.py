from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from vm.models import *
from users.models import user
import time
import json

def virtualhost(request):
    #return render_to_response("virtualhost.html")
    #user = request.get_signed_cookie('username', salt="cloud")
    if request.get_signed_cookie('username', salt="cloud"):
        #登陆后才能申请否则跳回首页
        return render_to_response("virtualhost.html")
    else:
        #提醒用户登录后再申请
        return render_to_response("index.html")

#用户申请虚拟机
def apply_vm(request):
    if request.method == "POST":
        #获取创建虚拟机所需信息
        vm_region = request.POST.get('vm_region')
        vm_type = request.POST.get('vm_type')
        apply_time = request.POST.get('apply_time')
        password = request.POST.get('password')
        disk = request.POST.get('disk')
        memory = request.POST.get('memory')
        cpu = request.POST.get('cpu')
        # 获得网关ip
        gw_ip = workstation.objects.get(belong=int(vm_region))
        #根据cookie拿用户信息
        username = request.get_signed_cookie('username', salt="cloud")
        User = user.objects.get(username=username)
        if gw_ip:
            start_time = time.time()
            #apply_time为啥是360000
            #apply_time = apply_time*3600
            apply_time=360000
            os_version = vm_conf.objects.get(type=vm_type)
            #向vm表插入数据
            Vm = vm.objects.create(type = vm_type,cpu_cores=cpu,memory=memory,disk=disk,gateway_ip=gw_ip.gateway_ip,region=vm_region,os_version=os_version.os_version,user=User.id,apply_time=apply_time,start_time=int(start_time),state=0,password=password)
            Vm.save()
            if Vm.id:
                # 向vm_list表插入数据
                Vm_list=vm_list.objects.create(user_id=User.id,state=0,vm_id=Vm.id)
                Vm_list.save()
                if Vm_list.id:
                    # 向new_vm_apply表插入数据
                    New_vm_apply = new_vm_apply.objects.create(user_id=User.id,gateway_ip=gw_ip.gateway_ip,region=vm_region,vm_id=Vm.id,cpu_cores=cpu,memory=memory,disk=disk,os_version=os_version.os_version,lid=Vm_list.id,apply_time=int(time.time()),state=0,password=password)
                    New_vm_apply.save()
                    st = 1
                    return HttpResponse(json.dumps({"st": st}), content_type="application/json")
                else:
                    st = 2
                    return HttpResponse(json.dumps({"st": st}), content_type="application/json")
            else:
                st = 2
                return HttpResponse(json.dumps({"st": st}), content_type="application/json")
        else:
            st=2
            return HttpResponse(json.dumps({"st": st}), content_type="application/json")

    else:
        st = 2
        return HttpResponse(json.dumps({"st": st}), content_type="application/json")
