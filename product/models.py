from datetime import datetime
import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.core.files.storage import default_storage
from django.db import models
from django.utils import timezone
from django_softdelete.models import SoftDeleteModel


def upload_to(instance, filename):
    name, extension = filename.split(".")
    now = datetime.today().strftime('%Y-%m-%d')
    file_list = {
        "photo": ['jpg', 'png'],
        "file": ['docx', 'pdf', 'xlsx'],
        "other": "",
    }

    for file in file_list:
        if extension in file_list[file]:
            # if default_storage.exists(f"upload/{file}/{now}/{instance.id}/{filename}"):
            #     default_storage.delete(f"upload/{file}/{now}/{instance.id}/{filename}")
            return f'upload/{file}/{now}/{instance.id}/{filename}'


class Product(SoftDeleteModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    media = models.FileField(upload_to=upload_to, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = "Product"
        verbose_name_plural = "Products"


# class Media(SoftDeleteModel):
#     # customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
#     object_model = models.CharField(max_length=255)
#     object_id = models.PositiveBigIntegerField()
#     file = models.FileField(upload_to=upload_to)
#     extension = models.CharField(max_length=255)
#     file_name = models.CharField(max_length=255)
#     file_path = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True, blank=True)
#     is_deleted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.object_model
#
#     class Meta:
#         ordering = ['id']


# class CustomerManager(BaseUserManager):
#     def create_superuser(self, email, phone, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.'
#             )
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.'
#             )
#
#         return self.create_user(email, phone, password, **extra_fields)
#
#     def create_user(self, email, phone, password, **extra_fields):
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#
#         user = self.model(email=email, phone=phone, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class Customer(AbstractUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     phone = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     name = models.CharField(max_length=255, null=True, blank=True)
#     gender = models.BooleanField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True, blank=True)
#     is_deleted = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone']
#
#     objects = CustomerManager()
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         ordering = ['id']


# class Config(SoftDeleteModel):
#     key = models.CharField(max_length=255)
#     value = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True, blank=True)
#     is_deleted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.key
#
#     class Meta:
#         ordering = ['id']
