from django.db import models



class department(models.Model):
    dep_id=models.IntegerField(primary_key=True)
    dep_name=models.CharField(max_length=100)
    dep_img=models.ImageField(upload_to='pics')
    dep_details=models.TextField()

    def __str__(self):
        return self.dep_name

class course(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100)
    hod_img=models.ImageField(upload_to='pics')
    course_price=models.DecimalField(max_digits=8, decimal_places=2)
    dep=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name


class Application(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now_add=False)
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    course = models.ForeignKey(course,on_delete=models.CASCADE)
    purpose = models.CharField(max_length=50,
                               choices=[('Enquiry', 'Enquiry'), ('Place order', 'Place order'), ('Return', 'Return')])

    def __str__(self):
        return self.name