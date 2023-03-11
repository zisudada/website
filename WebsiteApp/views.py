from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from WebsiteApp.models import UserInfo
def index(req):
  if req.method == "POST":
    q = req.POST.get("q")
    return redirect(f'https://cn.bing.com/search?q={q}')

  return render(req,'index.html')

def login(req):
  if req.method == "POST":
    user = UserInfo.objects.filter(user_name=req.POST.get("user"))
    if user.exists():
      _user = user.first()
      if _user.user_password == req.POST.get("password"):
        return HttpResponse('ok')
    pass
  return render(req,'login.html')