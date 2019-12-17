from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return '({}, {})'.format(self.username, self.email)
    class Meta :
        verbose_name = 'costumer'



class Salesman(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=12)
    activityDescription = models.TextField()
    activityFields = models.CharField(max_length=300) # ???
    approved = models.BooleanField()
    location = models.CharField(max_length=300)
    profileImage = models.ImageField(upload_to='salesman_profile', blank=True)
    identificationImage = models.ImageField(upload_to='salesman_identification_image', blank=True)
    registrationTime = models.DateTimeField(auto_now_add=True) # ???
    suspend = models.BooleanField()

    def __str__(self):
        return '({}, {})'.format(self.username, self.email)
    class Meta:
        verbose_name = 'salesman'


class Basket(models.Model):
    STATE_CHOICES = [
        ('pr', 'processing'),
        ('se', 'sending'),
        ('de', 'delivered')
    ]

    customer = models.ForeignKey(Customer , on_delete=models.CASCADE, related_name='baskets')
    paymentStatus = models.CharField(max_length=2, choices=STATE_CHOICES, default='pr')
    payTime = models.DateTimeField()
    recordTime = models.DateTimeField(auto_now_add=True) # ???
    trackingCode = models.CharField(max_length=300)


# class Color(models.Model):
#     name = models.CharField(max_length=10, primary_key=True)


# class Category(models.Model):
#     name = models.CharField(max_length=20, primary_key=True)


class Product(models.Model):
    category = models.CharField(max_length=50)
    color =models.CharField(max_length=30 )
    count = models.IntegerField()
    description = models.TextField()
    isStock = models.BooleanField(default=False)
    name = models.CharField(max_length=300)
    Price = models.IntegerField()
    salesman = models.ForeignKey(Salesman , on_delete=models.CASCADE, related_name='products')
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products' , null=True)
    # color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name='products' , null=True)
    recordTime = models.DateTimeField(auto_now_add=True) # ???
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    imageContent = models.ImageField(upload_to='product', blank=True)


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    count = models.IntegerField()
    state = models.CharField(max_length=20) # ???


