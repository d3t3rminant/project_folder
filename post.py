class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        return {"title":self.title, "content":self.content}  # Basically to same jako bych udelal post.__dict__


