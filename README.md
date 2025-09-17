# Blog Application

A modern, full-featured Django-based blog application with user authentication, article management, image uploads, categories, comments, likes, and REST API support.

## 🚀 Features

### Core Functionality
- **User Authentication**: Registration, login, and logout system
- **Article Management**: Create, read, update, and delete blog articles
- **Rich Text Editor**: TinyMCE integration for article content
- **Image Upload**: Unique image per article with title overlay
- **Categories**: Organize articles by categories with slug-based URLs
- **Comments System**: Users can comment on articles
- **Like System**: Users can like/unlike articles
- **Featured Posts**: Mark articles as featured for special display
- **Admin Interface**: Comprehensive admin panel with image previews

### Technical Features
- **REST API**: Django REST Framework integration
- **Responsive Design**: Bootstrap 5 with Crispy Forms
- **Database**: PostgreSQL support (configurable)
- **Media Handling**: Proper image upload and serving
- **Pagination**: Built-in pagination for article lists
- **Security**: CSRF protection, user authentication, and permission checks

## 📁 Project Structure

```
Blog_APP/
├── blog/                          # Main blog application
│   ├── models.py                  # Article, Category, Comment, ImageModel
│   ├── views.py                   # Class-based views for all blog functionality
│   ├── urls.py                    # URL routing for blog features
│   ├── forms.py                   # Image upload and comment forms
│   ├── admin.py                   # Admin interface configuration
│   ├── serializers.py             # REST API serializers
│   ├── context_processors.py      # Global context processors
│   └── templates/blog/            # HTML templates
│       ├── base.html              # Base template
│       ├── index.html             # Home page with all articles
│       ├── featured.html          # Featured articles page
│       ├── blog_post.html         # Individual article detail
│       ├── category_detail.html   # Category-specific articles
│       ├── blog_delete.html       # Article deletion confirmation
│       ├── upload.html            # Image upload interface
│       └── nav.html               # Navigation component
├── users/                         # User authentication app
│   ├── models.py                  # User model extensions
│   ├── views.py                   # Registration and user management
│   ├── forms.py                   # User registration form
│   ├── serializers.py             # User REST API serializers
│   ├── urls.py                    # User-related URL patterns
│   └── templates/users/           # Authentication templates
│       ├── register.html          # User registration
│       ├── login.html             # User login
│       └── logout.html            # User logout
├── tags/                          # Tagging system (in development)
│   ├── models.py                  # Tag model
│   └── views.py                   # Tag-related views
├── blogsite/                      # Project configuration
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py                    # WSGI configuration
│   └── asgi.py                    # ASGI configuration
├── media/                         # Uploaded files
│   └── images/                    # Article images
├── requirements.txt               # Python dependencies
└── manage.py                      # Django management script
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- PostgreSQL (or SQLite for development)
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd Blog_APP
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
   
   **For PostgreSQL (recommended):**
   - Install PostgreSQL
   - Create a database named `blog_web`
   - Update `blogsite/settings.py` with your database credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'blog_web',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': '127.0.0.1',
           'PORT': '5432'
       }
   }
   ```
   
   **For SQLite (development only):**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser account:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the application:**
   - Blog Homepage: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/
   - REST API: http://localhost:8000/api/

## 📚 Usage Guide

### For Regular Users
1. **Registration**: Create an account at `/accounts/register/`
2. **Login**: Access your account at `/accounts/login/`
3. **Browse Articles**: View all articles on the homepage
4. **Read Articles**: Click on any article to read the full content
5. **Like Articles**: Click the like button on articles you enjoy
6. **Comment**: Add comments to articles (requires login)
7. **Browse Categories**: Filter articles by category
8. **Featured Posts**: View specially marked articles

### For Content Creators
1. **Admin Access**: Use the admin panel to create and manage content
2. **Create Articles**: Add new blog posts with rich text content
3. **Upload Images**: Attach unique images to each article
4. **Manage Categories**: Create and organize article categories
5. **Moderate Comments**: Review and manage user comments

### For Developers
1. **REST API**: Access API endpoints for categories and users
2. **Admin Interface**: Manage all content through Django admin
3. **Custom Views**: Extend functionality with additional views
4. **Template Customization**: Modify Bootstrap-based templates

## 🔧 Configuration

### Key Settings in `blogsite/settings.py`

- **Database**: PostgreSQL configuration
- **Media Files**: Image upload handling
- **Static Files**: CSS, JavaScript, and other assets
- **Authentication**: Login/logout redirects
- **Crispy Forms**: Bootstrap 5 integration
- **TinyMCE**: Rich text editor configuration
- **REST Framework**: API pagination and permissions

### Environment Variables (Optional)
For production deployment, consider using environment variables for:
- `SECRET_KEY`
- `DEBUG`
- Database credentials
- `ALLOWED_HOSTS`

## 📊 Database Models

### Article Model
- `title`: Article title (CharField, max 255 chars)
- `content_field`: Rich text content (HTMLField)
- `created_date`: Auto-generated creation date
- `author`: Foreign key to User model
- `featured`: Boolean flag for featured articles
- `likes`: Many-to-many relationship with users
- `categories`: Many-to-many relationship with categories
- `image`: One-to-one relationship with ImageModel

### Category Model
- `name`: Category name (CharField, max 200 chars)
- `slug`: URL-friendly slug (auto-generated)

### Comment Model
- `post`: Foreign key to Article
- `author`: Foreign key to User
- `text`: Comment content (TextField)
- `date_posted`: Auto-generated posting date

### ImageModel
- `title`: Image title (CharField, max 50 chars)
- `image`: Image file (ImageField)
- `uploaded_at`: Upload timestamp

## 🌐 API Endpoints

### REST API Features
- **Categories API**: Full CRUD operations for categories
- **Users API**: User management endpoints
- **Authentication**: Token-based authentication
- **Pagination**: 10 items per page by default

### Available Endpoints
- `/api/categories/` - Category management
- `/api/users/` - User management
- `/api-auth/` - Authentication endpoints

## 🎨 UI/UX Features

### Design System
- **Bootstrap 5**: Modern, responsive framework
- **Crispy Forms**: Beautiful form rendering
- **Card-based Layout**: Consistent article display
- **Image Overlays**: Title badges on article images
- **Responsive Design**: Mobile-friendly interface

### Template Features
- **Base Template**: Consistent layout across all pages
- **Navigation**: User-friendly navigation bar
- **Pagination**: Easy browsing of article lists
- **Image Handling**: Proper image display and fallbacks

## 🔒 Security Features

- **CSRF Protection**: Cross-site request forgery prevention
- **User Authentication**: Secure login/logout system
- **Permission Checks**: Author-only article deletion
- **Input Validation**: Form validation and sanitization
- **File Upload Security**: Safe image upload handling

## 📦 Dependencies

### Core Dependencies
- **Django 5.2.5**: Web framework
- **djangorestframework 3.16.1**: REST API support
- **psycopg2-binary 2.9.10**: PostgreSQL adapter

### UI/UX Dependencies
- **crispy-bootstrap5 2025.6**: Bootstrap 5 integration
- **django-crispy-forms 2.4**: Form rendering
- **django-tinymce 4.1.0**: Rich text editor

### Development Dependencies
- **django-extensions 4.1**: Development utilities
- **pillow 11.3.0**: Image processing
- **pycurl 7.45.6**: HTTP client library

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure proper `ALLOWED_HOSTS`
3. Set up static file serving
4. Configure media file serving
5. Use environment variables for sensitive data
6. Set up proper database (PostgreSQL recommended)
7. Configure web server (Nginx + Gunicorn)

### Environment Setup
```bash
# Install production dependencies
pip install gunicorn

# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate

# Start production server
gunicorn blogsite.wsgi:application
```
