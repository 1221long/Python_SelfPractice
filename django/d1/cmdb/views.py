from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models
# Create your views here.

'''
user_list = [
    {"name":"1", "pwd":"a"},
    {"name":"2", "pwd":"b"},
]
'''

def index(request):
    #request.POST
    #request.GET
    #return HttpResponse("Hello world!")
    
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
        #uinfo = {"name":username, "pwd":password}
        #user_list.append(uinfo)
        models.UserInfo.objects.create(user=username,pwd=password)
        
    user_list = models.UserInfo.objects.all()

    return render(request, "index.html",{"data": user_list, "tmp":"fredy"})
