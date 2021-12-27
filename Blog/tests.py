import unittest
from django.test import Client

from Blog.models import Post

class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.posts = Post.objects.all()

    def test_home_and_blog_page(self):
        if Client().get("http://127.0.0.1:8000").status_code == 200 and Client().get("http://127.0.0.1:8000/blog").status_code == 200:
            print("home page loaded ok ...")
            print("blog page loaded ok ...")
            self.assertTrue(True,"home page loaded ok ...\nblog page loaded ok ...")
        else:
            self.assertTrue(False)



    def test_post_created(self):
        for post in self.posts:
            if Client().get(post.get_absolute_url()).status_code == 200:
                print(f"{post.title} is available\n")
            else:
                self.assertTrue(False)
        self.assertTrue(True)
