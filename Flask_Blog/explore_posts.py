from flaskblog import app
from flaskblog.models import db, Post

with app.app_context():

    print("\n=== ALL POSTS ===")
    posts = Post.query.all()
    for post in posts:
        print(post)

    print("\n=== PAGINATION: page=1, per_page=5 ===")
    page1 = Post.query.paginate(page=1, per_page=5)
    for post in page1.items:
        print(post)

    print("\n=== PAGINATION: page=2, per_page=5 ===")
    page2 = Post.query.paginate(page=2, per_page=5)
    for post in page2.items:
        print(post)

    print("\n=== PAGINATION ATTRIBUTES ===")
    print("Total posts:", page1.total)
    print("Current page:", page1.page)
    print("Posts per page:", page1.per_page)
    print("Has next page:", page1.has_next)
    print("Has previous page:", page1.has_prev)

# final commands running with cli only: 
# from flaskblog import app
# from flaskblog.models import db, Post

# with app.app_context():
#     posts = Post.query.paginate(page=1, per_page=5)
#     for post in posts.items:
#         print(post)

#     print(posts.page)
#     print(posts.total)
