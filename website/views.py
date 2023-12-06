from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    categories = ProjectCategory.objects.all()
    projects = Project.objects.all()
    print(projects)
    context = {
        'categories': categories,
        'projects': projects,
    }
    return render(request, 'website/home.html', context)

def contact(request):
    
    if request.method == "POST":
        
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_sent = request.POST['message']
        message = "From :" + message_name + "\n\n" + "Main message:\n" + message_sent + "\n\n" + "Email: " + message_email
        print(message)
        context = {'message_name': message_name,
				   'message_email': message_email,
				   'message': message,
  				  }
        request.session['context_data'] = context
        # send an email
        try:
            send_mail(
                subject='Contact Form',
                message=message,
                from_email=message_email,
                recipient_list=['josephagwuh@gmail.com', 'josephcagwuh@gmail.com'],
                fail_silently=False
            )
            messages.success(request, "Your Message has been Sent.")
            
        except smtplib.SMTPConnectError:
            print('Could not connect to the SMTP server.')
        except smtplib.SMTPAuthenticationError:
            print('Invalid SMTP username or password.')
        except smtplib.SMTPSenderRefused:
            print('Recipient address is invalid.')
        except smtplib.SMTPRecipientsRefused:
            print('Recipient addresses are invalid.')
        else:
            print('Email sent successfully.') 
        return HttpResponseRedirect(f"{reverse('home')}#contact")
    else:
        return render(request, 'website/home.html', {})
    

def components(request):
	return render(request, 'website/components.html', {})

def projects(request):
	return render(request, 'website/projects.html', {})

