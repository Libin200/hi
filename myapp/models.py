from django.db import models


# Create your models here.
class employee (models.model):
    eid=models.CharField(max_length=14)
class meta:
    db_table="employee"
