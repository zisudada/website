from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import SecretKeys
# Create your views here.
@csrf_exempt
def dockLinkTheWorldKey(req):
    if req.method == 'POST':
        get_data = req.POST.get('data')
        data = SecretKeys.objects.filter(name="LinkTheWorld")
        if data[0].key == get_data:
            return JsonResponse({"resp":"okokok"})
        else:
            return JsonResponse({"resp":"nook"})

def index(req):
    return render(req,'index.html')

def novels(req):
    return render(req,'novels.html')
