from blog import Blog
from post import Post

from unittest import TestCase

class TestBlog(TestCase):
    def setUp(self):
        self.blog = Blog("Blog Title", "Blog Author")

    def test_blog_create_post(self):
        self.blog.create_post("Post Title", "Post Content")

        self.assertEqual(self.blog.posts[0].title, "Post Title")
        self.assertEqual(self.blog.posts[0].content, "Post Content")

    def test_blog_json(self):
        self.blog.create_post("Post Title", "Post Content")
        expected_dict = {
            "title": "Blog Title",
            "author": "Blog Author",
            "posts": [{'content': 'Post Content', 'title': 'Post Title'}
            ],
        }
        self.assertDictEqual(self.blog.json(), expected_dict)

    def test_blog_json_no_post(self):
        expected_dict = {
            "title": "Blog Title",
            "author": "Blog Author",
            "posts": [],
        }

    def test_blog_post_added_list(self):
        post = self.blog.create_post("Post Title", "Post Content")
        self.assertIn(post, self.blog.posts)