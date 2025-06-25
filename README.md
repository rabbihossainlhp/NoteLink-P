# Noteshare Project

Noteshare is a Django-based application designed for sharing notes among users. This project includes a custom user model, authentication backend, and structured organization for templates and static files.

## Project Structure

```
Noteshare
├── manage.py
├── Noteshare
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── backends.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── migrations
│       └── __init__.py
├── notes
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── migrations
│       └── __init__.py
├── templates
│   ├── base.html
│   ├── registration
│   │   ├── login.html
│   │   └── signup.html
│   ├── notes
│   │   ├── note_list.html
│   │   └── note_detail.html
│   └── users
│       └── profile.html
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── main.js
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd Noteshare
   ```

2. **Create a Virtual Environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install django
   ```

4. **Run Migrations**
   ```
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```
   python manage.py runserver
   ```

## Features

- Custom user model with email and roll number authentication.
- Ability to create, view, and manage notes.
- User profiles to manage personal information.
- Organized templates and static files for easy maintenance.

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Admin panel available at `http://127.0.0.1:8000/admin/`.

## License

This project is licensed under the MIT License.