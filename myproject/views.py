from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view

from myapp.models import Blog, Team
from api.serializers import BlogSerializer


def index(request):
    return render(request, "index.html")


def blog(request):
    posts = Blog.objects.all()
    return render(request, "blog.html", {"posts": posts})


def detail(request, id):
    post = Blog.objects.get(id=id)
    return render(request, "detail.html", {"post": post})


def about(request):
    return render(request, "about.html")


def testimonial(request):
    return render(request, "testimonial.html")


def service(request):
    return render(request, "service.html")


def team(request):
    members = Team.objects.all()
    return render(request, "team.html", {"members": members})


def price(request):
    return render(request, "price.html")

 

@api_view(['GET'])
def blog_api(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
New Contact Form Message:

Name: {name}
Email: {email}

Subject: {subject}

Message:
{message}

------------------------------------
Sent from SafeCam Website Contact Page
"""

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")

            