from django.shortcuts import render
from django.views.generic import ListView

from Blog.models import Post, Category


def home_page(request):
    post = Post.objects.get_active_post().order_by("created")

    three_new_post = post[post.count() - 4:post.count()]

    cats = Category.objects.all()

    post_order_by_cats = {}

    for i in cats:
        post_order_by_cats[i] = post.filter(category__title=i.title).all()
        print(i, " ", post.filter(category__title=i.title).all())

    context = {
        "posts": post,
        "three_new_post": three_new_post,
        "cats": cats,
        "post_order_by_cats": post_order_by_cats,
    }
    return render(request, "home_page.html", context)


class SearchPostsView(ListView):
    template_name = 'all_post.html'

    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')

        if query is not None:
            return Post.objects.search(query)
        else:
            return Post.objects.get_active_couses()
