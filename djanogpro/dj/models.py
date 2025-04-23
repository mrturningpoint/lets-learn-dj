from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
# Create your models here.
class chaivariety (models.Model):
    chai_type_choice=[('ML','MASALA'),('GR','GINGER'),('KL','KIWI'),('PL','PLAIN'),('EL','ELAICHI'),]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added= models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=chai_type_choice)
    description=models.TextField(default="")
    def __str__(self):
        return self.name

#one to many
class chaireview(models.Model):
    chai=models.ForeignKey(chaivariety,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating =models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
#many to many
class store(models.Model):
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    chai_varietiess=models.ManyToManyField(chaivariety,related_name='stores')

    def __str__(self):
         return self.name

#ome to one
class chaicert(models.Model):
    chai= models.OneToOneField(chaivariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number= models.CharField(max_length=100)
    issue_date=models.DateTimeField(default=timezone.now)
    valid_until=models.DateTimeField()

    def __str__(self):
         return f'certificate for{self.name.chai}'