from django.urls import path
from .views import details_post,Posts

urlpatterns = [
    path('details/<int:id>',details_post),
    path('',Posts.as_view())
]