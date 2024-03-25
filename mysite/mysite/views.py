from django.shortcuts import render
from posts.models import Post
from  products.models import Product

def home(request):
    return render(request,'homepage.html')
def second(request):
    post = Post.objects.all()
    product = Product.objects.all()
    return render(request, 'secondpage.html', {
        "product":product,
        "post": post,
    })
