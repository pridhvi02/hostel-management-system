from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Hostels
from django.core import serializers

# Create your views here.


# def index(request):
#     indexdict = {'index_insert': 'INDEX PAGE INSERTED'}
#     return render(request, 'index.html', context=indexdict)

def index(request):
    return render(request, 'index.html')

# def hostels(request):
#     indexdict = {'hostel_insert': 'HOSTEL PAGE INSERTED'}
#     return render(request, 'hostels.html', context=indexdict)


def hostels(request):
    return render(request, 'hostels.html')


def gents(request):

    dic_gents = {
        'gents_hostels': Hostels.objects.filter(hostel_type='G'),
    }
    return render(request, 'gents.html', dic_gents)


def ladies(request):
    dic_ladies = {
        'ladies_hostels': Hostels.objects.filter(hostel_type='L'),
    }
    return render(request, 'ladies.html', dic_ladies)


def moreinfo(request):

    if request.method == 'GET':
        id_py = request.GET.get('id')
        
        results = Hostels.objects.filter(id=id_py)

        # dic_info = {
        #     'infos': results
        # }
        
        dic_info = serializers.serialize("json", results)
        return JsonResponse(dic_info,safe=False)
        # print("dic info is here\n"+dic_info)
        # return HttpResponse(dic_info, content_type='application/json')
        # return JsonResponse({'infos':Hostels.objects.filter(id=id_py)})
        # return render(request, 'moreinfo.html', dic_info)
        # return render(request, 'moreinfo.html', dic_info)



