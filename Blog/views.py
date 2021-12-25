from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

def details_post(request,id):
    post = Post.objects.get_active_post().filter(id=id).first()



    context = {
        "post_details":post
    }
    return render(request,'details_post.html',context)


class Posts(ListView):
    template_name = "all_post.html"
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.get_active_post()
