from django.shortcuts import render,redirect
# Create your views here.
def index(req):
  if req.method == "POST":
    q = req.POST.get("q")
    return redirect(f'https://cn.bing.com/search?q={q}')

  return render(req,'index.html')

  #return redirect('/')