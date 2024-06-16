# Slot-Based-Online-LPG-Booking-System

This is my **first mini project**. 
It is a '**slot-based online LPG booking system**' that allows users to choose their preferred delivery times for gas cylinders. 
The frontend is created using **HTML, CSS, JavaScript and Bootstrap** for a user-friendly and attractive interface. The backend is powered by **Django**, a robust Python framework, and the database is managed with **MySQL** for reliable and efficient data storage.
The system also allows users to cancel bookings and view their order status (booked, out-for-delivery, delivered). 
Admins can manage orders by updating their status. 
This project is useful because it streamlines the booking process, providing users with flexible delivery options and ensuring timely delivery. This enhances overall customer satisfaction and reduces waiting times.

Here are **important commands and steps to be followed** which I used in different stages of my project.
1. Installing python and setting its path.
2. Installing pip
   $ python -m pip install -U pip
3. Setting up Virtual Environment
--> $ pip install virtualenv      (to install virtual environment)
--> $ virtualenv my_env           (to create your own virtual environment)
--> $ cd my_env
    $ Scripts\activate            (to activate your virtual environment)
--> (my_env)$ deactivate (to deactivate it)
4. Installing Django
--> $ pip install django
5. To start a new Django Project
--> $ django-admin startproject my_project
--> $ cd my_project
--> $ python manage.py runserver
6. To start an App
--> $ python manage.py startapp myApp
--> $ Navigate to settings.py -> go to Installed Apps and add 'myApp' to it.
7. Project level 'urls.py'
--> Add this code, 
  * from django.contrib import admin
    from django.urls import path, include
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myApp.urls')),
    ]
9. Creating app level 'urls.py'
-->  Add your code, 
  * from django.contrib import admin
    from django.urls import path, include
    urlpatterns = [
       // your paths,
    ]
10. Place the static and templates folders in 'myApp'
11. Now write respective codes for 
--> models.py
--> forms.py
--> views.py
--> backend.py 
12. To make changes reflect in your database
--> python manage.py makemigrations
--> python manage.py migrate
13. Do not forget to link your database in settings.py (default will be SQLite)
