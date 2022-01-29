
from django.shortcuts import HttpResponseRedirect
from main.models import ContactUs
from django.shortcuts import render
# Create your views here.
def home(request):
    data = ContactUs.objects.all()
    return render(request, 'index.html', {'data':data})

def sendMessage(request):
    if request.method == 'POST':
        send_message = ContactUs()
        send_message.name = request.POST.get("name")
        send_message.email = request.POST.get("email")
        send_message.adress = request.POST.get("adress")
        send_message.message = request.POST.get("message")
        send_message.save()
        return HttpResponseRedirect('/')