from django.contrib import admin
from users.models import Profile,Address,transaction

# Register your models here.
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(transaction)