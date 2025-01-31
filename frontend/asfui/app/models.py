# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from os import path
import sys
import os
import re

# Create your models here.

class vdTarget(models.Model):
    name = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=100, default='Me')
    lastdate = models.DateTimeField(auto_now=True)
    itemcount = models.IntegerField(default=0)
    type = models.CharField(max_length=100, default='DOMAIN')
    tag = models.CharField(max_length=100, default='DEFAULT')
    
    def __str__(self):
        return self.name.lower()

class vdInTarget(models.Model):
    name = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=100, default='Me')
    lastdate = models.DateTimeField(auto_now=True)
    itemcount = models.IntegerField(default=0)
    type = models.CharField(max_length=100, default='DOMAIN')
    tag = models.CharField(max_length=100, default='DEFAULT')
    
    def __str__(self):
        return self.name.lower()

class vdResult(models.Model):
    name = models.CharField(max_length=150, unique=True)
    type = models.CharField(max_length=30, default="DOMAIN")
    source = models.CharField(max_length=60, default="")
    ipv4 = models.CharField(max_length=20, default="")
    ipv6 = models.CharField(max_length=150, default="")
    lastdate = models.DateTimeField(auto_now=True)
    itemcount = models.IntegerField(default=0)
    tags = models.CharField(max_length=250, default="")
    info = models.CharField(max_length=250, default="")
    
    def __str__(self):
        return self.name.lower()
    
    def getList(self):
        return {'name':self.name, 'type':self.type, 'source':self.source, 'ipv4': self.ipv4, 'ipv6':self.ipv6, 'lastdate':str(self.lastdate), 'itemcount':self.itemcount, 'tags':self.tags, 'info':self.info}
    
class vdServices(models.Model):
    name = models.CharField(max_length=150, unique=True)
    nname = models.CharField(max_length=150, default="unknown")
    type = models.CharField(max_length=30, default="DOMAIN")
    source = models.CharField(max_length=60, default="")
    ipv4 = models.CharField(max_length=20, default="")
    ipv6 = models.CharField(max_length=150, default="")
    lastdate = models.DateTimeField(auto_now=True)
    itemcount = models.IntegerField(default=0)
    tags = models.CharField(max_length=250, default="")
    ports = models.CharField(max_length=250, default="")
    full_ports = models.TextField(default="")
    service_ssh = models.CharField(max_length=250, default="")
    service_rdp = models.CharField(max_length=250, default="")
    service_telnet = models.CharField(max_length=250, default="")
    service_ftp = models.CharField(max_length=250, default="")
    service_smb = models.CharField(max_length=250, default="")
    nuclei_http = models.TextField(default="")
    info = models.TextField(default="")
    info_gnmap = models.TextField(default="")
    nse_vsanrce = models.CharField(max_length=250, default="")
    
    def __str__(self):
        return self.name.lower()

class vdInServices(models.Model):
    name = models.CharField(max_length=150, unique=True)
    nname = models.CharField(max_length=150, default="unknown")
    type = models.CharField(max_length=30, default="DOMAIN")
    source = models.CharField(max_length=60, default="")
    ipv4 = models.CharField(max_length=20, default="")
    ipv6 = models.CharField(max_length=150, default="")
    lastdate = models.DateTimeField(auto_now=True)
    itemcount = models.IntegerField(default=0)
    tags = models.CharField(max_length=250, default="")
    ports = models.CharField(max_length=250, default="")
    full_ports = models.TextField(default="")
    service_ssh = models.CharField(max_length=250, default="")
    service_rdp = models.CharField(max_length=250, default="")
    service_telnet = models.CharField(max_length=250, default="")
    service_ftp = models.CharField(max_length=250, default="")
    service_smb = models.CharField(max_length=250, default="")
    nuclei_http = models.TextField(default="")
    info = models.TextField(default="")
    info_gnmap = models.TextField(default="")
    nse_vsanrce = models.CharField(max_length=250, default="")
    
    def __str__(self):
        return self.name.lower()
    
class vdRegExp(models.Model):
    name = models.CharField(max_length=150, unique=True)
    regexp = models.CharField(max_length=250, default=".*")
    exclude = models.CharField(max_length=250, default="")
    tags = models.CharField(max_length=250, default="")
    info = models.TextField(default="")
    def __str__(self):
        return self.name.lower()

class vdJob(models.Model):
    name = models.CharField(max_length=150, unique=True)
    input = models.CharField(max_length=64, default="amass")
    regexp = models.CharField(max_length=250, default="")
    exclude = models.CharField(max_length=250, default="")
    module = models.CharField(max_length=250, default="error")
    tags = models.CharField(max_length=250, default="")
    info = models.TextField(default="")
    def __str__(self):
        return self.name.lower()
