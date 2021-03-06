from django.contrib import admin

# Register your models here.
from .models import User, Accounts, Transaction

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','mobileNumber','created_at']

admin.site.register(User,UserAdmin)

class AccountsAdmin(admin.ModelAdmin):
    list_display = ['account_id','user','created_at','account_balance']

admin.site.register(Accounts,AccountsAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_id','transaction_timestamp','transaction_amount','account']
    
admin.site.register(Transaction,TransactionAdmin)

