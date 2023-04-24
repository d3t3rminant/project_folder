from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"Blog(title='{self.title}', author='{self.author}')"

    def create_post(self, title, content):
        post = Post(title, content)
        self.posts.append(post)
        return post

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.__dict__ for post in self.posts]
        }

