from django.shortcuts import render

# Create your views here.

def other(request):
    return render(request,"temp/other.html")


def index(request):
    my_dictionary={'k1':'How Are u Saad','K2':"I a'm Fine",'K3':100}
    return render(request,"temp/index.html",context=my_dictionary)

def base(request):
    return render(request,"temp/base.html")

def relative(request):
    return render(request,"temp/relative.html")
