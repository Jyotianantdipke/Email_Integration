
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def sendmail(request):

    if request.method=='POST':
        email=request.POST.get('email')
        subject='Welcome to django'
        message= 'Hi, This is a Demo of how you can send email in django'
        email_from= settings.EMAIL_HOST_USER
        recipient_list= [email]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,'SendMail/dashboard.html',{'recipient_list':recipient_list})
    return render(request,'SendMail/sendmail.html')



