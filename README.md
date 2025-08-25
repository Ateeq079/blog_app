# Blog_APP

A modern, full-featured Django-based blog application with user authentication, article management, unique image uploads per post, categories, REST API support, and a visually consistent, responsive Bootstrap UI.

## Features
- User registration, login, and logout
- Create, view, like, and delete blog articles
- **Unique image per article** with badge/title overlay
- Article categories and featured posts
- Image upload and management (with admin and user-facing display)
- REST API endpoints for categories and users
- **Visually consistent, modern templates** using Django and Bootstrap
- Admin interface for managing content with image previews

## Project Structure
- `blog/` - Main blog app (articles, categories, images, views, templates)
- `users/` - User authentication and registration
- `tags/` - Tagging system (WIP)
- `blogsite/` - Project settings and configuration
- `media/` - Uploaded images
- `requirements` - Python dependencies

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL (or update `settings.py` for your DB)
- pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Blog_APP
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure the database:**
   - Update `blogsite/settings.py` with your PostgreSQL credentials or use SQLite for testing.
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the app:**
   - Blog: [http://localhost:8000/](http://localhost:8000/)
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Usage
- Register a new user or log in.
- Create, view, and like articles.
- Upload a unique image to each article (with image title badge overlay in all views).
- Browse articles by category or featured status.
- Use the admin panel to manage users, articles, images, and categories (with image previews).
- Access REST API endpoints at `/api/` (see `blog/urls.py` and `users/views.py`).

## Image Handling & UI Consistency
- Each article can have a unique image, managed via the admin or upload form.
- Images are displayed with a badge overlay showing the image title (if present) on all article cards and detail pages.
- All templates (index, featured, category, detail, delete, upload) use a consistent Bootstrap card-based layout, spacing, and meta info styling for a modern, unified look.
- No-image placeholders are shown where appropriate.

## Dependencies
- Django 5.2.5
- djangorestframework
- crispy_forms, crispy_bootstrap5
- tinymce
- django_extensions
- PostgreSQL (default, can be changed)

## License
MIT License (add your license here)

---
*This project is a Django blog platform with REST API, unique image handling, and a modern, visually consistent UI. Contributions welcome!*
