from django.db import models

# Create your models here.

# My database : resharper_crud_database.crud_app_table_contents
class table_contents(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_no = models.BigIntegerField()