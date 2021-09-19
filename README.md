
# Email Send in Django

    In this repo , i have described how we can send Email 
    in django with very simple steps, so lets start!
    


## Installation

you have to create a new Project and then virtual environment 
is created, activate the environment if not activate by default 
then perform following steps

Install using pip install django



```bash
  pip install django
  django-admin startproject Email_Integration
  cd Email_Integration
  py manage.py startapp EmailSending
    
```
  ## Settings

    Add your app in installed apps in settings.py

```bash
  INSTALLED_APPS = {

    ...
    'EmailSending',
    ...
  
  }
    
```
Then make following changes in settings.py file


```bash
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = #sender's email-id
EMAIL_HOST_PASSWORD = #password associated with above email-id
 
```
## Implementation

now move to views.py and import settings and send_mail function as below


```bash
from django.conf import settings
from django.core.mail import send_mail
 
```


create a view which will responsible for sending a mail to a specified email address
for this we have to take input from user that exactly on which email address he wants to send mail
and then call a fumction send_mail() which takes 4 parameter as follow
   subject (string),
   message (string), 
   from_email (string), 
   recipient_list (list),








## Demo


```bash
email = 'xyz@gmail.com'
subject = 'welcome'
message = 'This is a demo of how you can send email in django'
email_from = settings.EMAIL_HOST_USER
recipient_list = [email]
send_mail( subject, message, email_from, recipient_list )
 
```

now what happens here is email refers to the recipient email address,
subject is the subject of email , message is actual body of email,
email_from refers to the senders information which we have already specidied in settings.py
and then recipient_list is the list of the receivers.

```bash
send_mail( subject, message, email_from, recipient_list )
 
```

all this parameters passed to the function send mail which we have imported from django.core.mail, 
here we have done with sending mail in django

## run the project 

using following command
```bash
  py manage.py runserver
```
and your mail is sent successfully to receipient 

## Contributing

Please feel free to fix bugs, improve things, Just send a pull request, Thanks!!!
