from django.shortcuts import render

# Create your views here.
def getdata(request):
    data=Employee.objects.get(id=13)
    return  HttpResponse(data)
