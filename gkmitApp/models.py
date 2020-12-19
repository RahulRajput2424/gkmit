import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(db_index=True, unique=True)
    mobileNumber = models.CharField(null=True,max_length=18, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Accounts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    account_id = models.CharField(unique=True,editable=False,default=uuid.uuid4(),max_length=18,)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
       
class Transaction(models.Model):
    transaction_id = models.UUIDField(unique=True,editable=False,default=uuid.uuid4)
    transaction_timestamp = models.DateTimeField(auto_now=True)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE, default=None, null=True)
