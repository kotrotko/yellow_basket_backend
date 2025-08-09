# Yellow Basket Backend

Django REST API for flower shop management.

## Setup

1. Install dependencies (from project root):
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations from the **outer** `backend/` directory:
   ```bash
   cd backend
   python manage.py migrate
   ```

3. Start server from the **outer** `backend/` directory:
   ```bash
   ./manage.py runserver
   ```

## API

- Admin: `http://localhost:8000/admin/`
- API: `http://localhost:8000/api/`

## Tech Stack

- Django 5.1+
- Django REST Framework  
- SQLite database