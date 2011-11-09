# Create your views here.
from django.core.context_processors import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.utils import simplejson
from src.pair_stairs.models import Programmer, PairStairs, increase_pair_times

def view_stairs(request):
    pair_stairs = list(PairStairs.objects.all())
    programmers = list(Programmer.objects.all())
    return render_to_response('stairs.html', RequestContext(request,
                            {'programmers': programmers,
                             'pair_stairs': pair_stairs}))

def add_programmer(request):
    if request.method == 'POST':
        new_programmer = request.POST['programmer_name']
        all_programmer = Programmer.objects.all()
        for programmer in all_programmer:
            if programmer:
                if programmer.name == new_programmer:
                    response_render = render_to_response("programmer_exist.html",RequestContext(request))
                    return response_render

        for programmer in all_programmer:
            PairStairs(first = programmer.name, second = new_programmer, times = 0).save()
        Programmer(name = new_programmer).save()
        return redirect(view_stairs)

    return render_to_response('add_programmer.html', RequestContext(request))



def update_times(request, pairs):
    data = {'result':'success'}
    members = pairs.split('_')
    increase_pair_times(first = members[0], second = members[1])
    return HttpResponse(simplejson.dumps(data), mimetype="text/json")



