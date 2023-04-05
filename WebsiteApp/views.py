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
    user = req.POST.get('user')
    password = req.POST.get('password')
    try:
        _user = UserInfo.objects.filter(user=user_name).first
    except:
        return HttpResponse('错了')
    if _user.user_password == password:
        return HttpResponse('对了')
  return render(req,'login.html')

def blogs(req):
    """blog html

    :function: TODO
    :returns: TODO

    """
    return render(req,'blogs.html')

def stories(req):
    """stories html

    :function: TODO
    :returns: TODO

    """
    return render(req,'stories.html')

def page_not_found(req, exception):
    return render(req, 'err/404_page.html')

def page_error(req):
    return render(req, 'err/500_page.html')
