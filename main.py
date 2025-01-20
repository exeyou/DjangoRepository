import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_lesson.settings")
django.setup()

from orm_test.models import Author, Post

author = Author.objects.create(name="Vasya", age=23, email="sshshlol1")
print(author)

authors = Author.objects.all()
print(authors.first())

filtered_authors = Author.objects.filter(age__gte=20)
print(filtered_authors)

post = Post.objects.create(title="POSITK", body="interesting text", author=author, published=False)
post.body = "NEWPOST!!1"
post.save()
print(author.posts.all())