from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data (request):
    D={'Name':'Ramis Khan','Age': 22,'DOB': '29-3-2001'}
    return render(request,'data.html',context=D)

def string (request):
    return HttpResponse ('<center> <h2> Login Sucessfull <h2> </center>')

