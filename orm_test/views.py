from django.shortcuts import render
from orm_test.models import Author, Post
# Create your views here.
def main_page(request):

    return render(request, "main_page.html")

def show_authors(request):
    authors = Author.objects.all()
    return render(request, "show_authors.html", {'authors': authors})

def posts_view(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'posts_page.html', {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post_detail.html", {"post": post})