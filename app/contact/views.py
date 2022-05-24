from django.shortcuts import render
from . models import Contact
from . forms import ContactForm
from django.http import HttpResponseRedirect , HttpResponse
from django.core.mail import send_mail

def contact(request):
    form_class = ContactForm
    form = form_class

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')

            data = {
                'name': name,
                'email': email,
                'subject' : subject
            }

            subject = ''' Nouveau Messsage {}
                          De {}
                      '''.format(data['subject'], data['email'])
            send_mail(data['subject'],subject, '', ['christmdev@gmail'])

            #enregistrement des données dans le base de donées admin 
            contact = Contact
            contact.name = name
            contact.email= email
            contact.subject = subject
            contact.save
            return HttpResponseRedirect('/contact/sucess')
    return render(request,'contact.html', {'form' : form})

def sucess(request): 
    return render(request,'sucess.html')
