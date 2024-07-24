from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinValueValidator

STATE_CHOICE = (
    ('Select Your State', 'Select Your State'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),

)


class Customer(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default=" ")
    locality = models.CharField(max_length=200, default=" ")
    city = models.CharField(max_length=90, default=" ")
    zipcode = models.IntegerField(default=247001)
    state = models.CharField(choices=STATE_CHOICE, max_length=80, default=STATE_CHOICE[0])

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES = (
    ('Mobile', 'Mobile'),
    ('Laptop', 'Laptop'),
    ('ElectronicAccessories', 'Electronic Accessories'),
    # ('BW', 'Bottom Wear'),
)

class Brand(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30, default=None)
    def __str__(self):
        return (self.name)
    


class Product(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discounted_prie = models.FloatField()
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    product_image = models.ImageField(upload_to='productimg', null=False , blank=False)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def totalCost(self):
        return self.quantity * self.product.discounted_prie


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=60, choices=STATUS_CHOICES, default='Pending')

    @property
    def totalCost(self):
        return self.quantity * self.product.discounted_prie


# Create your models here.
class Verification(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	token = models.CharField(max_length=150)
	verify = models.BooleanField(default=False)

class ContactUs(models.Model):
    name = models.CharField(max_length=50, default=" ")
    email = models.EmailField(default=" ")
    contactno = models.CharField(max_length=10, default=" ")
    description = models.CharField(max_length=500 ,default="")

    def __str__(self):
        return str(self.name)