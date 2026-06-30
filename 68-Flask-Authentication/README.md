## Day 68 - User Authentication & Security

### Concepts Covered
- Password hashing and salting with Werkzeug
- pbkdf2:sha256 hashing method
- Flask-Login for session management
- UserMixin for login functionality
- @login_required decorator for protected routes
- Flash messages for user feedback
- send_from_directory for protected file downloads

### Security Implementation
- Passwords hashed with salt before storage (never stored in plain text)
- Login verification via hash comparison, not decryption
- Protected secrets page and file download (login required)

### How Password Verification Works
1. User registers → password is hashed + salted → stored hash in database
2. User logs in → entered password is hashed using same method
3. New hash compared against stored hash → match = access granted
4. Original password is never decoded or retrievable