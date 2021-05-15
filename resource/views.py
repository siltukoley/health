from django.shortcuts import render,HttpResponse
from resource.models import Post
from django.contrib import messages

# Create your views here.
def home(request): 
    return render(request,'index.html')

def contact(request):

    return HttpResponse("This is contact")

def about(request): 
    return HttpResponse('This is about')

def handleresource(request):
    if request.method == "POST":
        name = request.POST['name']
        phone=request.POST['phone']
        area = request.POST['area']
        catagory=request.POST['catagory']
        details =request.POST['details']
        if len(name)<2 or len(phone)<10 or len(area)<2 or len(details)<4: 
            messages.error(request, "Please fill the form correctly")
        else:
            resource = Post(name=name, phone=phone, area=area, catagory=catagory, details=details)
            resource.save()
            messages.success(request, "Your message submitted successfully")
    return render(request,'index.html')