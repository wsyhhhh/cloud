from django.db import models

# Create your models here.
class domain(models.Model):
    domain = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=20, null=True)
    gw_ip = models.CharField(max_length=32)
    port = models.IntegerField(max_length=11)
    user = models.CharField(max_length=20, null=True)
    pwd = models.CharField(max_length=20, null=True)
    file_name = models.CharField(max_length=10, null=True)
    state = models.SmallIntegerField(max_length=1, null=True, default=1)
    feature = models.IntegerField(max_length=11, default=0)
    run = models.IntegerField(max_length=11, default=0)
    apply_time = models.IntegerField(max_length=11, null=True, default=0)

class new_apply(models.Model):
    user_id = models.IntegerField(max_length=10)
    type = models.IntegerField(max_length=10)
    vm_id = models.IntegerField(max_length=10)
    ip = models.CharField(max_length=32)
    password = models.CharField(max_length=30)
    lid = models.IntegerField(max_length=10)
    apply_time = models.IntegerField(max_length=10)
    state = models.SmallIntegerField(max_length=1, default=0)
    log_admin = models.CharField(max_length=30)

class new_vm_apply(models.Model):
    user_id = models.IntegerField(max_length=11)
    gateway_ip = models.CharField(max_length=20)
    region = models.IntegerField(max_length=11, default=0)
    vm_id = models.IntegerField(max_length=11)
    os_version = models.CharField(max_length=50)
    cpu_cores = models.IntegerField(max_length=2)
    memory = models.IntegerField(max_length=10)
    disk = models.IntegerField(max_length=10)
    password = models.CharField(max_length=50)
    lid = models.IntegerField(max_length=11)
    apply_time = models.IntegerField(max_length=11)
    state = models.IntegerField(max_length=2)
    log_admin = models.CharField(max_length=30)

class vm(models.Model):
    belong = models.IntegerField(max_length=10, null=True, default=0)
    uuid = models.CharField(max_length=60, null=True)
    name_label = models.CharField(max_length=50, null=True)
    type = models.IntegerField(max_length=5, null=True, default=1)
    cpu_cores = models.IntegerField(max_length=3, default=0)
    memory = models.IntegerField(max_length=3, default=0)
    disk = models.IntegerField(max_length=10, default=0)
    ip = models.CharField(max_length=15, null=True)
    gateway_ip = models.CharField(max_length=15, null=True)
    region = models.IntegerField(max_length=11)
    os_version = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=100)
    user = models.IntegerField(max_length=10, null=True)
    apply_time = models.IntegerField(max_length=11, null=True, default=0)
    start_time = models.IntegerField(max_length=11, null=True, default=0)
    power_state = models.CharField(max_length=20, null=True)
    state = models.SmallIntegerField(max_length=1, null=True, default=0)
    delete = models.SmallIntegerField(max_length=1, null=True,default=1)
    log_admin = models.CharField(max_length=30)

class vm_conf(models.Model):
    type = models.IntegerField(max_length=11)
    os_version = models.CharField(max_length=30, null=True)

class vm_list(models.Model):
    user_id = models.IntegerField(max_length=11, null=True)
    vm_id = models.CharField(max_length=32, null=True)
    des_ip = models.CharField(max_length=32, null=True)
    local_port = models.IntegerField(max_length=10, null=True)
    gw_ip = models.CharField(max_length=32, null=True)
    port = models.IntegerField(max_length=10, null=True)
    state = models.SmallIntegerField(max_length=1, null=True, default=0)
    timeout = models.SmallIntegerField(max_length=1, null=True, default=0)

class workstation(models.Model):
    host_name = models.CharField(max_length=20, null=True)
    ip = models.CharField(max_length=15, null=True)
    gateway_ip = models.CharField(max_length=15, null=True)
    user = models.CharField(max_length=20, null=True)
    pwd = models.CharField(max_length=20, null=True)
    belong = models.IntegerField(max_length=11, null=True)

class ws_conf(models.Model):
    live = models.CharField(max_length=10)
    cpuNumber = models.IntegerField(max_length=32)
    cpuSpeed = models.IntegerField(max_length=32)
    totalMemory = models.IntegerField(max_length=32)
    overheadMemory = models.IntegerField(max_length=32)
    freeMemory = models.IntegerField(max_length=32)
    physicalDisk = models.IntegerField(max_length=32)
    virtualAllocation = models.IntegerField(max_length=32)
    physicalUtilisation = models.IntegerField(max_length=32)

#class Vm_m:
    #def select_vm(self,region,type,apply_time,password,disk,memory,cpu):

