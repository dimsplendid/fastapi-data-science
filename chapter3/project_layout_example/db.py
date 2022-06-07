from project_layout_example.models import user, post

class DummyDatabase:
    users: dict[int, user.User] = {}
    posts: dict[int, post.Post] = {}


db = DummyDatabase()