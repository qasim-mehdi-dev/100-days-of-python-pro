## Day 67 - Blog Content Management System

### Concepts Covered
- Flask-CKEditor for rich text blog content
- Jinja filters (| pipe syntax) for value transformation
- Reusable form pattern for both Create and Edit
- Text column type for long-form content
- Pre-populated forms using existing model data

### Project
A full blog CMS allowing creation, editing and deletion of posts with a rich text editor, dynamic post pages and full CRUD functionality

### Key Pattern
Single CreatePostForm class powers both /new-post and /edit-post routes — edit_post pre-fills the form with existing data, demonstrating form reusability