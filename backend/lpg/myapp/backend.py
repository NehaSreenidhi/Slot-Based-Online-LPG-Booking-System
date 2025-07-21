from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend
from .models import Employee

class MobileNumberBackend:
    def authenticate(self, request, mobile_no=None, password=None):
        try:
            user = User.objects.get(profile__mobile_no=mobile_no)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class EmployeeIDBackend(BaseBackend):
    def authenticate(self, request, empID=None, password=None):
        try:
            employee = Employee.objects.get(employeeid=empID)
            if employee.employeeid == password:
                return employee
        except Employee.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employee.objects.get(pk=user_id)
        except Employee.DoesNotExist:
            return None