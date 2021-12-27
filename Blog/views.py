from django.shortcuts import render
from django.views.generic import ListView
from .models import Post,PostModule,Category

def details_post(request,id):
    post = Post.objects.get_active_post().filter(id=id).first()
    list_of_offer = PostModule.objects.filter(post_id=id)

    # dict_of_Avantages = {i.id:[] for i in list_of_offer}
    # dict_of_Disadvantages = {i.id:[] for i in list_of_offer}
    # for offer in list_of_offer:
    #     dict_of_Avantages[offer.id].append(AdvantagesModule.objects.filter(post_module_id=offer.id))
    #     dict_of_Disadvantages[offer.id].append(DisadvantagesModule.objects.filter(post_module_id=offer.id))



    context = {
        "post_details":post,
        "offers":list_of_offer,
        # "dict_of_Avantages":dict_of_Avantages,
        # "dict_of_Disadvantages":dict_of_Disadvantages,
    }
    return render(request,'details_post.html',context)


class Posts(ListView):
    template_name = "all_post.html"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.get_active_post()


