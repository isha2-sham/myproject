from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

# GET all blogs + POST new blog
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# GET single blog + PUT + DELETE
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer