from django.contrib import admin
from django.urls import path
from myproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('price/', views.price, name='price'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('detail/', views.detail, name='detail'),
    path('api/blogs/', views.blog_api, name='blog_api'),
    path('contact/', views.contact, name='contact'),
 
]
