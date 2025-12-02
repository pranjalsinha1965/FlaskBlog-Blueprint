import json
from flaskblog import app, db
from flaskblog.models import Post

json_path = r"C:\Users\KIIT\Desktop\flaskBlog\Flask_Blog\posts.json"

with app.app_context():

    # Load JSON data
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Insert posts into DB
    for item in data:
        post = Post(
            title=item["title"],
            content=item["content"],
            user_id=item.get("user_id", 1)
        )
        db.session.add(post)

    db.session.commit()

    print("✅ JSON data imported successfully!")
