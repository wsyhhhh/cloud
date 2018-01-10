from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32, null=True)
    usbkey = models.CharField(max_length=30)
    kind = models.IntegerField(max_length=2,default=0)
    email = models.CharField(max_length=40)
    group_type = models.IntegerField(max_length=8, null=True, default=1)
    admin_type = models.IntegerField(max_length=11,default=0)
    reg_time = models.IntegerField(max_length=11, null=True)
    lastlogin = models.IntegerField(max_length=11, null=True)
    log_admin = models.CharField(max_length=30)

class user_log(models.Model):
    uid = models.IntegerField(max_length=11, null=True)
    start_time = models.IntegerField(max_length=11, null=True)
    end_time = models.IntegerField(max_length=11, null=True)

class group(models.Model):
    gname = models.CharField(max_length=10, null=True)
    gtype = models.IntegerField(max_length=2, null=True)