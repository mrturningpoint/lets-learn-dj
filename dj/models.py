from django.db import models
from django.utils import timezone 
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