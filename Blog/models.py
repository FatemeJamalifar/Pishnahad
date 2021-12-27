from django.conf import settings
from django.db import models
import os
from django.db.models import Q


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f'Posts/{instance.title}/{final_name}'



class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)


    def get_absolute_url(self):
        return f"/category/{self.id}/{self.slug}"

    def __str__(self):
        return self.title

class PostManager(models.Manager):
    def get_active_post(self):
        return self.get_queryset().filter(active=True)

    def get_post_by_id(self,post_id):
        return self.get_queryset().filter(id=post_id)

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(overview__icontains=query) | Q(category__title__icontains=query)
        return self.get_queryset().filter(lookup, active=True, ).distinct()

class Post(models.Model):
    auth = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image_path, null=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    active = models.BooleanField(default=False, null=True)

    objects = PostManager()

    def get_absolute_url(self):
        return f"/blog/{self.id}"

    def __str__(self):
        return self.title


class PostModule(models.Model):
    post = models.ForeignKey(Post, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image_path, null=True)
    url_price = models.URLField()
    advantages = models.TextField(null=True)
    disadvantages = models.TextField(null=True)
    info = models.TextField(null=True)

