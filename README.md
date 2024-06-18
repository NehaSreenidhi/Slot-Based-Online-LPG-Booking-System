# Slot-Based-Online-LPG-Booking-System

This is my **first mini project**.<br /> 
It is a '**slot-based online LPG booking system**' that allows users to choose their preferred delivery times for gas cylinders. <br />
The frontend is created using **HTML, CSS, JavaScript and Bootstrap** for a user-friendly and attractive interface. The backend is powered by **Django**, a robust Python framework, and the database is managed with **MySQL** for reliable and efficient data storage.<br />
The system also allows users to cancel bookings and view their order status (booked, out-for-delivery, delivered). <br />
Admins can manage orders by updating their status. <br />
This project is useful because it streamlines the booking process, providing users with flexible delivery options and ensuring timely delivery. This enhances overall customer satisfaction and reduces waiting times.<br />

Here are **important commands and steps to be followed** which I used in different stages of my project.
1. Installing python and setting its path.<br />
2. Installing pip<br />
   $ python -m pip install -U pip<br />
3. Setting up Virtual Environment<br />
   $ pip install virtualenv      (to install virtual environment)<br />
   $ virtualenv my_env           (to create your own virtual environment)<br />
   $ cd my_env<br />
   $ Scripts\activate            (to activate your virtual environment)<br />
   (my_env)$ deactivate          (to deactivate it)<br />
5. Installing Django<br />
   $ pip install django<br />
6. To start a new Django Project<br />
   $ django-admin startproject my_project<br />
   $ cd my_project<br />
   $ python manage.py runserver<br />
7. To start an App<br />
   $ python manage.py startapp myApp<br />
   $ Navigate to settings.py -> go to Installed Apps and add 'myApp' to it.<br />
8. Project level 'urls.py'<br />
   Add this code, <br />
  * from django.contrib import admin<br />
    from django.urls import path, include<br />
    urlpatterns = [<br />
        path('admin/', admin.site.urls),<br />
        path('', include('myApp.urls')),<br />
    ]<br />
9. Creating app level 'urls.py'<br />
Add your code, <br />
  * from django.contrib import admin<br />
    from django.urls import path, include<br />
    urlpatterns = [<br />
       // your paths,<br />
    ]<br />
10. Place the static and templates folders in 'myApp'<br />
11. Now write respective codes for <br />
models.py, forms.py, views.py, backend.py <br />
12. To make changes reflect in your database<br />
    python manage.py makemigrations<br />
    python manage.py migrate<br />
13. Do not forget to link your database in settings.py (default will be SQLite)<br />
