from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):

    def create_user(self, name,email, phone_number, role, password=None):
        if email is None:
            raise TypeError('Users should have a username')

        user = self.model(name=name, email=email, phone_number=phone_number,role=role)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name,email, phone_number, role, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(name, email, phone_number, role, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    role = (
        ('customer','CUSTOMER'),
        ('admin','ADMIN')
    )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True,db_index=True)
    phone_number = models.IntegerField(unique=True,db_index=True,blank=True, null=True)
    role = models.CharField(choices=role,max_length=50,default='customer')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_number', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email


class Todo(models.Model):
    task = models.CharField(max_length=225)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task