# 📝 Note App - Django Web Application

A modern, user-friendly note-taking web application built with Django. This application allows users to create, read, update, and delete notes with a beautiful, responsive interface.

## ✨ Features

- **User Authentication**: Secure registration and login system
- **CRUD Operations**: Create, Read, Update, and Delete notes
- **Responsive Design**: Beautiful UI that works on desktop and mobile devices
- **User Dashboard**: Personalized homepage showing user's notes
- **Modern Interface**: Clean and intuitive user experience
- **SQLite Database**: Lightweight database for storing notes and user data

## 🛠️ Technology Stack

- **Backend**: Django 4.2.23
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Django Templates
- **Authentication**: Django's built-in authentication system

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rohanoza001/note-app.git
cd note-app
```

### 2. Create Virtual Environment

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
note-app/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── db.sqlite3               # SQLite database
├── note/                    # Main Django app
│   ├── __init__.py
│   ├── admin.py             # Admin interface configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # URL routing
│   ├── migrations/          # Database migrations
│   ├── templates/note/      # HTML templates
│   │   ├── homepage.html    # User dashboard
│   │   ├── login.html       # Login page
│   │   ├── register.html    # Registration page
│   │   └── note.html        # Note management page
│   └── static/              # Static files (CSS, JS, images)
└── project/                 # Django project settings
    ├── __init__.py
    ├── settings.py          # Project settings
    ├── urls.py              # Main URL configuration
    ├── asgi.py              # ASGI configuration
    └── wsgi.py              # WSGI configuration
```

## 🎯 Usage

### 1. Registration
- Visit the registration page at `/register/`
- Fill in your username, email, and password
- Click "Register" to create your account

### 2. Login
- Visit the login page at `/login/`
- Enter your username and password
- Click "Login" to access your account

### 3. Managing Notes
- **View Notes**: All your notes are displayed on the homepage
- **Create Note**: Click "Add New Note" to create a new note
- **Edit Note**: Click the edit button on any note to modify it
- **Delete Note**: Click the delete button to remove a note

## 🔧 Configuration

### Environment Variables
The application uses Django's default settings. For production deployment, consider setting:

- `DEBUG = False`
- `SECRET_KEY` (generate a new one)
- `ALLOWED_HOSTS` (add your domain)

### Database
The application uses SQLite by default. For production, consider using PostgreSQL or MySQL.

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment
1. Set `DEBUG = False` in `settings.py`
2. Configure your production database
3. Set up a web server (nginx, Apache)
4. Use a WSGI server (Gunicorn, uWSGI)
5. Configure static files serving

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Rohan Oza**
- GitHub: [@Rohanoza001](https://github.com/Rohanoza001)

## 🙏 Acknowledgments

- Django Documentation
- Django Community
- All contributors and supporters

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the [Issues](https://github.com/Rohanoza001/note-app/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

---

**Happy Note Taking! 📝✨** 