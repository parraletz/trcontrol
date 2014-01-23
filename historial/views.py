from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

def home(request):
    return HttpResponseRedirect("/admin/")


def index(request):
    msg = "Hola este es un mensaje"
    ctx = {'msg': msg}
    return render_to_response('web/index.html', ctx, context_instance=(RequestContext(request)))


