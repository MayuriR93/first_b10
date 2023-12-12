from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mob_number = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    salary = models.IntegerField(default= 28000)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Product(models.Model):              # -- aaplyala ekhada table create karaycha nasel tr tya class sathi class Meta define karne aani tyat abstract = True hi condition dyavi, jenekarun table create honar nahi.
    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
        
        
        
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.first_name}"
    
# one to one madhe relationship aapan kontyahi eka table madhe thewu shakto pan one to many madhe aaplyala relationship many jithe asel tithe thewaych aahe    
    
class Address(models.Model):
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True) #-- one to one relationship sathi aapan OneToOneField dila tasach one to many sathi ForeignKey yet
# jr person delete zala tr address cha record delete nahi honar fakt person_id null houn jail SET_NULL mule

    def __str__(self):
        return f"{self.street}"
    
    class Meta:                  # workbench madhe je tables tayar hotat tyanche names aap che name _ mg table name as asta for ex. app_Profile. aapan class Meta use karun table name change karu shakto.
        db_table = "address"     #
    
    
    
    
class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)   #-- person aani profile che one to one relationship aapan profile madhe define kela aahe tech aapan person madhe suddha karu shakto.
    bio = models.TextField()
    birthdate = models.DateField()
    
    def __str__(self):
        return f"{self.bio}"
    
    
# ORM ----- object relational mapper ----- object oriented API ----- Django ORM 