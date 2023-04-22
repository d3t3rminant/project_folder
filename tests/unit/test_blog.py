from blog import Blog
from post import Post

from unittest import TestCase

class TestBlog(TestCase):
    def setUp(self):
        self.blog = Blog("Blog Title", "Blog Author")

    def test_create_empty_blog(self):
        b = Blog("Blog Title", "Blog Author")
        self.assertEqual(b.title, "Blog Title")
        self.assertEqual(b.author, "Blog Author")
        self.assertListEqual(b.posts, [])
        self.assertEqual(len(b.posts), len([]))

    def test_repr_blog(self):
        self.assertEqual(self.blog.__repr__(), f"Blog(title='Blog Title', author='Blog Author')")


    def test_post_in_blog(self):
        self.blog.posts = ["Post1"]
        self.assertEqual(self.blog.posts[0], "Post1")

    def test_blog_json_no_posts(self):
        expected_dict = {
            "title": "Blog Title",
            "author": "Blog Author",
            "posts": [
            ],
        }
        self.assertDictEqual(self.blog.json(), expected_dict)


