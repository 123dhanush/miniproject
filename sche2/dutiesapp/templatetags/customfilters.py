

from django import template
from django.shortcuts import render
from django.template.defaultfilters import stringfilter
from django.template import loader
from django.template import Template
glob=3
flag=0
register=template.Library()
@register.filter
def trueflag(val):
    if val==1:
        globals()['flag']=1
        return globals()['flag']
    elif val==2:
        globals()['flag']=0
        return globals()['flag']

    else:
        return globals()['flag']




def disp(val):
    return flag+6



register.filter('trueflag',trueflag)
register.filter('disp',disp)
