from unittest import TestCase
from post import Post


class TestPost(TestCase):
    def test_create_post(self):
        p = Post("Titulek", "Obsah")
        self.assertEqual(p.title, "Titulek")
        self.assertEqual(p.content, "Obsah")

    def test_post_to_json(self):
        p = Post("Titulek", "Obsah")
        self.assertDictEqual(p.json(), {"content":"Obsah", "title":"Titulek"})
