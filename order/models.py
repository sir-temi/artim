from django.db import models
from accounts.models import UserProfile
from django.utils import timezone

class UserOrder(models.Model):
    customerorder = models.ForeignKey(UserProfile, related_name='customerorder', on_delete=models.CASCADE)
    artisanorder = models.ForeignKey(UserProfile, related_name='artisanorder', on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    order_price = models.DecimalField(decimal_places=2, max_digits=10)
    order_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)
    order_rejected = models.BooleanField(default=False)
    order_accepted = models.BooleanField(default=False)
    message = models.TextField(default=False)
    total_distance = models.CharField(max_length=100)
    walking_time = models.CharField(max_length=100)
    driving_time = models.CharField(max_length=100)
    bicycle_time = models.CharField(max_length=100)
    
    def completed(self):
        self.order_completed = True
        self.completed_date = timezone.now()
        self.save()
    
    def accepted(self):
        self.order_accepted = True
        self.save()

    def rejected(self):
        self.order_rejected = True
        self.save()

class Withdrawal(models.Model):
    artisanwithdrawal = models.ForeignKey(UserProfile, related_name='artisanwithdrawal', on_delete=models.CASCADE)
    withdrawal_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    method = models.CharField(max_length=20)