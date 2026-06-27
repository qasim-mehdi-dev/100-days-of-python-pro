## Day 64 - My Top 10 Movies Website (Capstone)

### Concepts Covered
- Full stack Flask application combining all learned concepts
- SQLAlchemy ORM with nullable and required fields
- Live API integration with The Movie Database (TMDB)
- Two step add flow: search → select → rate
- Dynamic ranking system based on user ratings
- Flask-WTF forms with Bootstrap5 styling
- Full CRUD: Create, Read, Update, Delete

### Project
A personal movie ranking website where you search real movies from TMDB, add them to your collection, rate and review them, and they automatically rank themselves by rating

### Architecture
- Movie model stores title, year, description, rating, ranking, review, poster image
- Search flow: user types title → API returns options → user selects → movie saved → rating form shown
- Rankings recalculated on every home page load