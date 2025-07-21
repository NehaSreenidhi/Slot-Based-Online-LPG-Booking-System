# Slot-Based Online LPG Booking System

This is my **first mini project** — a **Django-based web application : Slot-based online LPG booking system** that allows users to book LPG cylinders by selecting preferred delivery slots. 
It **streamlines the booking process** by providing users with flexible delivery options and helps ensure timely delivery, reduces waiting times, and improves customer satisfaction.

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Backend:** Django (Python Framework)  
- **Database:** MySQL  

---

## Features

### Users can:
  - Book LPG cylinders by selecting preferred delivery slots
  - Cancel bookings
  - View order status: `Booked`, `Out-for-Delivery`, `Delivered`

### Admins can:
  - Manage user orders
  - Update and track order statuses

---

## Setup Instructions
> Make sure Python and MySQL are installed on your system.

### 1. Clone the repository
```bash
git clone https://github.com/NehaSreenidhi/Slot-Based-Online-LPG-Booking-System.git
cd Slot-Based-Online-LPG-Booking-System
```

### 2. Set Up Virtual Environment
```bash
pip install virtualenv
virtualenv mini
mini\Scripts\activate          # On Windows
```

### 3. Install dependencies
```bash
pip install django python-dotenv mysqlclient
```
### 4. Configure environment variables
Create a .env file in the project root and add your secret key and database credentials

### 5. Apply database migrations

To apply model changes to the database:
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```
---

## Project Structure

```
  backend/lpg/
  ├── lpg/            # Django project folder (settings.py, urls.py, etc.)
  │   ├── settings.py
  │   ├── urls.py
  │   └── ...
  ├── myapp/          # Django app
  │   ├── models.py
  │   ├── views.py
  │   ├── urls.py
  │   ├── templates/
  │   └── static/
  ├── manage.py

```
---

### Note:
> Link your MySQL database in `settings.py`.  
> (By default, Django uses SQLite)

---
