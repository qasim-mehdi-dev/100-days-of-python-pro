# Full Stack Blog CMS 🌐

A complete blog platform with user auth,
admin controls, commenting and Gravatar
avatars — the mega capstone project.

## Features
- User registration with hashed passwords
- Login/logout with Flask-Login sessions
- Admin-only post creation and deletion
  (user id=1 = admin)
- Rich text posts via CKEditor
- Comments on posts (login required)
- Gravatar avatars on comments
- 403 Forbidden for unauthorized access
- Full CRUD on blog posts

## Setup
1. pip install -r requirements.txt
2. python main.py
3. Register first → you become admin (id=1)
4. Visit http://localhost:5001

## Database relationships
User → BlogPost (one to many)
User → Comment (one to many)
BlogPost → Comment (one to many)

## Technologies
Python, Flask, SQLAlchemy, Flask-Login,
Flask-WTF, CKEditor, Bootstrap5, Gravatar,
Werkzeug Security