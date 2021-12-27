from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, PostModule


def details_post(request, id):
    post = Post.objects.get_active_post().filter(id=id).first()
    list_of_offer = PostModule.objects.filter(post_id=id)

    context = {
        "post_details": post,
        "offers": list_of_offer,
    }
    return render(request, 'details_post.html', context)


class Posts(ListView):
    template_name = "all_post.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.get_active_post()
