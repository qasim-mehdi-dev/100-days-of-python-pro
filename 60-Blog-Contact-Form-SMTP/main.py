import os
from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv

load_dotenv()

posts = [
    {
        "id": 1,
        "title": "The Life of Cactus",
        "subtitle": "Cacti are beautiful plants that can survive in harsh conditions.",
        "author": "Angela Yu",
        "date": "June 24, 2026",
        "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce taro dulse nori jícama bitterleaf aubergine guandong.",
        "image": "https://images.unsplash.com/photo-1509423350716-97f9360b4e0f?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80"
    },
    {
        "id": 2,
        "title": "Top 5 Hiking Trails",
        "subtitle": "Discover the most breathtaking views around the globe.",
        "author": "Qasim Mehdi",
        "date": "June 24, 2026",
        "body": "Frittilla cellery quandong chickpea ginger potato. Soko radischio bitterleaf water spinach rutabaga. Parsley winter purslane courgette courgette lettuce garbanzo coriander quandong green bean.",
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80"
    }
]
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
