from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Entrepreneurship, Finance

# Create your views here.
def frontpage(request):
    entrepreneur = Entrepreneurship.objects.all()
    buying = Finance.objects.all()
    return render(request, 'index.html',{'entrepreneur': entrepreneur, 'buying':buying})

def entrepreneurship(request):
    entrepreneur = Entrepreneurship.objects.all()
    return render(request, 'entrepreneur.html',{'entrepreneur': entrepreneur})   

    

def finance(request):
    buying = Finance.objects.all()
    return render(request, 'finance.html', {'buying':buying})   

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n". join(text), content_type="text/plain")

