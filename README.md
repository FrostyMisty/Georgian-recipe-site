
1. Install dependencies:
   ```
   pip install django
   ```
2. Run migrations:
   ```
   python manage.py migrate
   ```
3. Create a superuser (admin):
   ```
   python manage.py createsuperuser
   ```
4. Run the development server:
   ```
5.   python manage.py runserver
   ```
python manage.py runserver
## Static Files

- Place images in `static/images/`.
- Main CSS is in `static/style.css`.

## Templates

- All HTML templates are in the `templates/` folder.
- Uses Django template inheritance with `base.html`.

## Admin Access

- Go to `http://127.0.0.1:8000/admin/`
- Login with your superuser credentials.

## Default Admin User

- **Username:** frosty
- **Password:** 1234



