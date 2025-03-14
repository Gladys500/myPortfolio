from django.shortcuts import render, redirect
from .models import ContactRequest

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def starter(request):
    return render(request,'starter.html')

def contact(request):
    if request.method == 'POST':
        mycontact = ContactRequest(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        
        mycontact.save()  # Call the save method
        return redirect('/showcontact')
    
    else:
        return render(request, 'contact.html')

def portfolio_details(request):
    return render(request,'portfolio_details.html')

def portfolio(request):
    return render(request,'portfolio.html')

def resume(request):
    return render(request,'resume.html')

def services(request):
    return render(request,'services.html')

def showcontact(request):
    mycontact = ContactRequest.objects.all()
    return render(request,'showcontact.html', {"ContactRequest":mycontact})

def delete(request, id):
    contact=ContactRequest.object.get(id=id)
    contact.delete()
    return redirect('/showcontact')

def edit(request, id):
    editcontact;id =ContactRequest.object.get(id=id)
    contact.edit()
    return redirect('/showcontact')