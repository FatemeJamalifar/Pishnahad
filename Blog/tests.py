from django.test import TestCase

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

from Blog.models import Post

class SeleniumTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ### set config for selenium
        super().setUpClass()
        cls.path = os.path.dirname(os.path.abspath(__file__))
        cls.address = os.path.join(cls.path, "chromedriver")
        cls.driver = webdriver.Chrome(executable_path=cls.address)
        cls.driver.delete_all_cookies()
        cls.driver.get('http://127.0.0.1:8000/login/')
        cls.posts = Post.objects.all()

    @classmethod
    def tearDownClass(cls):
        ### distroying
        cls.driver.quit()
        super().tearDownClass()

    def test_course_created(self):
        self.driver.
