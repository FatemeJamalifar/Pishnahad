from django.urls import path
from .views import details_post, Posts

urlpatterns = [
    path('<int:id>', details_post),
    path('', Posts.as_view())
]
