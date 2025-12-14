# FitPlanHub

A Django-based fitness planning platform where trainers can create and sell fitness plans, and users can subscribe to and manage their fitness subscriptions.

## Features

### Core Features
- **User Authentication**: Registration and login with role-based access (User/Trainer)
- **Fitness Plans**: Trainers can create, view, and manage fitness plans
- **Subscriptions**: Users can subscribe to fitness plans from trainers
- **Trainer Following**: Users can follow trainers to see their plans in a personalized feed
- **Home Page**: Browse all available fitness plans with subscription status

### User Roles
- **Regular User**: Browse plans, subscribe to plans, follow trainers, view personal feed
- **Trainer**: Create and manage fitness plans, view subscriptions

## Project Structure

```
FitPlanHub/
├── FitPlanHub/              # Main project settings
│   ├── settings.py          # Django configuration
│   ├── urls.py              # URL routing
│   ├── views.py             # Home page view
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── accounts/                # User authentication app
│   ├── models.py            # Custom User model with is_trainer flag
│   ├── views.py             # Sign up, login, logout views
│   └── admin.py             # Admin configuration
├── plans/                   # Fitness plans app
│   ├── models.py            # FitnessPlan model
│   ├── views.py             # Trainer dashboard, plan detail views
│   └── admin.py             # Admin configuration
├── subscriptions/           # Subscription management app
│   ├── models.py            # Subscription model
│   ├── views.py             # Subscribe view
│   └── admin.py             # Admin configuration
├── follows/                 # Trainer following app
│   ├── models.py            # Follow model
│   ├── views.py             # Follow, unfollow, feed views
│   └── admin.py             # Admin configuration
├── templates/               # HTML templates
│   ├── base.html            # Base template with navigation
│   ├── index.html           # Home page
│   ├── accounts/
│   │   ├── login.html       # Login page
│   │   └── signup.html      # Sign up page
│   └── plans/
│       ├── trainer_dashboard.html    # Trainer dashboard
│       ├── plan_detail.html          # Plan details page
│       └── user_feed.html            # User's personalized feed
├── static/                  # Static files (CSS, images)
│   ├── css/
│   │   └── style.css        # Custom styles
│   └── images/
├── db.sqlite3               # SQLite database
└── manage.py                # Django management script
```

## Models

### User (accounts.models)
```python
class User(AbstractUser):
    is_trainer: Boolean      # Flag to identify trainers
```

### FitnessPlan (plans.models)
```python
class FitnessPlan:
    trainer: ForeignKey(User)        # Trainer who created the plan
    title: CharField                 # Plan name
    description: TextField           # Detailed description
    price: IntegerField             # Cost in rupees
    duration: IntegerField          # Duration in days
```

### Subscription (subscriptions.models)
```python
class Subscription:
    user: ForeignKey(User)          # User who subscribed
    plan: ForeignKey(FitnessPlan)   # Plan subscribed to
```

### Follow (follows.models)
```python
class Follow:
    user: ForeignKey(User)          # User who is following
    trainer: ForeignKey(User)       # Trainer being followed
```

## Installation & Setup

### Requirements
- Python 3.8+
- Django 5.1.4
- SQLite3 (included with Python)

### Steps

1. **Clone the repository**
   ```bash
   cd FitPlanHub
   ```

2. **Install dependencies**
   ```bash
   pip install django
   ```

3. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Home: `http://localhost:8000/`
   - Admin: `http://localhost:8000/admin/`

## Usage

### For Regular Users
1. **Sign Up**: Create an account and select "User" as role
2. **Browse Plans**: View all available fitness plans on the home page
3. **Subscribe**: Click "Subscribe" to purchase a plan
4. **View Plan Details**: Access full plan details after subscription
5. **Follow Trainers**: Follow trainers to see their plans in your personalized feed
6. **View Feed**: Check your personalized feed with plans from followed trainers

### For Trainers
1. **Sign Up**: Create an account and select "Trainer" as role
2. **Create Plans**: Go to Trainer Dashboard and create fitness plans
3. **Manage Plans**: View and manage all your created plans
4. **Track Subscriptions**: See how many users have subscribed to your plans

## URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | home | Home page with all plans |
| `/signup/` | signup | User registration |
| `/login/` | user_login | User login |
| `/logout/` | logout_user | User logout |
| `/trainer-dashboard/` | trainer_dashboard | Trainer's dashboard |
| `/plan/<id>/` | plan_detail | Plan details page |
| `/subscribe/<plan_id>/` | subscribe | Subscribe to a plan |
| `/feed/` | user_feed | Personalized user feed |
| `/follow/<trainer_id>/` | follow_trainer | Follow a trainer |
| `/unfollow/<trainer_id>/` | unfollow_trainer | Unfollow a trainer |
| `/admin/` | admin | Django admin panel |

## API Views

### Home View
- **URL**: `/`
- **Method**: GET
- **Description**: Displays all fitness plans and user subscription status

### Trainer Dashboard
- **URL**: `/trainer-dashboard/`
- **Method**: GET, POST
- **Description**: GET displays trainer's plans; POST creates a new plan
- **Requires**: Login, is_trainer=True

### Plan Detail
- **URL**: `/plan/<id>/`
- **Method**: GET
- **Description**: Shows full plan details (restricted content for non-subscribers)
- **Requires**: Login

### Subscribe
- **URL**: `/subscribe/<plan_id>/`
- **Method**: POST
- **Description**: Subscribes user to a plan
- **Requires**: Login

### User Feed
- **URL**: `/feed/`
- **Method**: GET
- **Description**: Shows plans from followed trainers
- **Requires**: Login

### Follow/Unfollow Trainer
- **URL**: `/follow/<trainer_id>/`, `/unfollow/<trainer_id>/`
- **Method**: GET
- **Description**: Follow or unfollow a trainer
- **Requires**: Login

## Testing

The application includes comprehensive test coverage:

```bash
python manage.py check              # Run system checks
python manage.py migrate            # Apply migrations
python manage.py test --verbosity=2 # Run tests
```

### Features Tested
- Home view functionality
- User authentication (sign up, login, logout)
- Trainer dashboard
- Fitness plan creation and management
- Plan subscriptions
- Trainer following/unfollowing
- User feed display
- Model validation
- Template loading

## Security Features

- Django CSRF protection on all forms
- User authentication required for sensitive operations
- Role-based access control (trainer vs. regular user)
- Secure password hashing using Django's built-in authentication

## Database

The project uses SQLite3 by default, configured in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Static Files

- **CSS**: `static/css/style.css` - Custom styling
- **Images**: `static/images/` - Image assets
- **Bootstrap**: CDN-hosted Bootstrap 5.3.0

## Admin Panel

Access the Django admin at `/admin/` with your superuser credentials to:
- Manage users
- Create and edit fitness plans
- View subscriptions
- Manage follow relationships

## Configuration

Key settings in `FitPlanHub/settings.py`:
- `DEBUG = True` - Development mode (change to False for production)
- `ALLOWED_HOSTS = ['*']` - Allow all hosts (configure for production)
- `AUTH_USER_MODEL = 'accounts.User'` - Custom user model
- `DATABASES` - SQLite3 configuration
- `INSTALLED_APPS` - Registered Django apps

## Common Issues & Solutions

### Issue: Template not found error
**Solution**: Ensure template files are in the correct directory structure under `templates/`

### Issue: ALLOWED_HOSTS error
**Solution**: Update `ALLOWED_HOSTS` in settings.py to include your domain/IP

### Issue: Database migration errors
**Solution**: Run `python manage.py migrate` to apply all migrations

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic` and ensure STATIC_URL is configured

## Future Enhancements

- Payment gateway integration for subscriptions
- Email notifications for new plans from followed trainers
- Review and rating system for plans
- Progress tracking for subscribed users
- Workout logging and analytics
- Mobile app
- Advanced search and filtering
- Plan expiration and renewal management

## Support & Contribution

For issues or contributions, please contact the development team or submit a pull request.

## License

This project is for educational purposes.

## Version

**Current Version**: 1.0.0

---

**Last Updated**: December 2025
"# college-fits-plane" 
