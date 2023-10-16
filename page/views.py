from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from django.conf import settings
# from django.template.loader import render_to_string
# from django.http import HttpResponse
# from django.contrib.auth.models import User

def index(request):
    return render( request, 'index.html')

def login(request):
    return render (request, 'login.html')

# def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with the provided email exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            # If the user exists, authenticate and login
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                print("User logged in. Calling send_signup_email...")
                send_signup_email(user.email)  # Send the signup email
                return redirect('home')

    return render(request, 'login.html')

# # Function to send the signup email
# def send_signup_email(user_email):
#     subject = 'Thanks for signing up'
#     message = render_to_string('email_template.html', {'user_email': user_email})
#     sender_email = settings.EMAIL_HOST_USER
#     recipient_email = [user_email]

#     send_mail(subject, message, sender_email, recipient_email, fail_silently=False)

#     return HttpResponse("Signup email sent successfully!")


# // Import those packages
from django.core.mail import send_mail
from django.conf import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import ssl


# function that handles sending your email
def SendEmail(email_subject, email_message, email_reciever):
    sender_email = settings.EMAIL_HOST_USER  # Set the sender's email address
    receiver_email = email_reciever  # Set the recipient's email address
    password = settings.EMAIL_HOST_PASSWORD  # Set the password for the sender's email account

    message = MIMEMultipart("alternative")  # Create a MIME multipart message
    message["Subject"] = "Django test"  # Set the email subject
    message["From"] = "adesewalola2006@gmail.com"  # Set the sender of the email
    message["To"] = "shopadeomolara@gmail.com"  # Set the recipient of the email

    # Create the plain-text and HTML version of the email message
    text = email_message

    # Turn the plain-text version into a plain MIMEText object
    part1 = MIMEText(text, "plain")

    # Add the plain-text part to the MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)

    try:
        # Create a secure connection with the email server and send the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)  # Log in to the email server
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )  # Send the email
    except Exception as error:
        print('Exception Occurred', error)  # Print any exceptions that occur during the process



subject = "Hello from Assistant"
message = "This is a test email sent using the SendEmail function."
receiver = "shopadeomolara@gmail.com"

SendEmail(subject, message, receiver)