from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, UserRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Booking, Employee, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully. Hi {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'myapp/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mobile_no = form.cleaned_data['mobile_no']
            password = form.cleaned_data['password']
            user = authenticate(request, mobile_no=mobile_no, password=password)
            if user is not None:
                login(request, user)
                # Store consumer_no in session
                profile = Profile.objects.get(user=user)
                request.session['consumer_no'] = profile.consumer_no
                return redirect('home')
            else:
                error = 'Invalid mobile number or password'
    else:
        form = LoginForm()
        error = None
    return render(request, 'myapp/login.html', {'form': form, 'error': error})

def user_logout(request):
    logout(request)
    return redirect('home')

def book(request):
    success = False
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
        else:
            print(form.errors)
    else:
        form = BookingForm()
    return render(request, 'myapp/booking.html', {'form': form})

def booking_success(request):
    return render(request, 'myapp/booking_success.html')

def landing_page(request):
    return render(request, 'myapp/landing_page.html')

def home(request):
    return render(request, 'myapp/landing_page.html')

@login_required
def customer_orders(request):
    consumer_no = request.session.get('consumer_no')
    bookings = Booking.objects.filter(consumer_number=consumer_no)
    return render(request, 'myapp/customer_orders.html', {'bookings': bookings})

def admin_login(request):
    error = None
    if request.method == 'POST':
        emp_id = request.POST.get('empID')
        password = request.POST.get('password')
        try:
            employee = Employee.objects.get(employeeid=emp_id)
            if employee.employeeid == password:  # Password is the same as the employee ID
                request.session['employeeid'] = employee.employeeid
                return redirect('manage_orders')
            else:
                error = "Invalid Employee ID or Password"
        except Employee.DoesNotExist:
            error = "Invalid Employee ID or Password"

    return render(request, 'myapp/admin_login.html', {'error': error})

def manage_orders(request):
    if 'employeeid' not in request.session:
        return redirect('admin_login')

    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('status_'):
                booking_id = key.split('_')[1]
                try:
                    booking = Booking.objects.get(id=booking_id)
                    booking.status = value
                    booking.save()
                except Booking.DoesNotExist:
                    pass
        return redirect('manage_orders')

    bookings = Booking.objects.all()
    return render(request, 'myapp/manage_orders.html', {'bookings': bookings})

@login_required
def cancel(request):
    consumer_no = request.session.get('consumer_no')  # Get consumer number from session
    if not consumer_no:
        messages.error(request, 'Consumer number not found in session.')
        return redirect('customer_orders')

    current_booking = Booking.objects.filter(consumer_number=consumer_no, status__in=['booked', 'out-for-delivery']).first()

    if request.method == 'POST':
        if current_booking:
            current_booking.delete()
            messages.success(request, 'Your order has been successfully cancelled.')
            return redirect('customer_orders')
        else:
            messages.error(request, 'No current order to cancel.')

    return render(request, 'myapp/cancellation.html', {'current_booking': current_booking})

def forgot_password(request):
    if request.method == 'POST':
        mobile_no = request.POST['mobile_no']
        try:
            profile = Profile.objects.get(mobile_no=mobile_no)
            user = profile.user
            return redirect('reset_password', user_id=user.id)
        except Profile.DoesNotExist:
            return render(request, 'myapp/forgot_password.html', {'error': 'User not found'})
    return render(request, 'myapp/forgot_password.html')

def reset_password(request, user_id):
    if request.method == 'POST':
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            try:
                user = User.objects.get(id=user_id)
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                return render(request, 'myapp/reset_password.html', {'user_id': user_id, 'success': 'Password reset successful!'})
            except User.DoesNotExist:
                return render(request, 'myapp/reset_password.html', {'error': 'User not found', 'user_id': user_id})
        else:
            return render(request, 'myapp/reset_password.html', {'error': 'Passwords do not match', 'user_id': user_id})
    return render(request, 'myapp/reset_password.html', {'user_id': user_id})