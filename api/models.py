from django.db import models

class Staff(models.Model):
    staff_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email=models.EmailField(blank=True, null=True)
    telephone=models.CharField(max_length=250, blank=True, null=True)
    certified = models.BooleanField(default=True)

    # def __str__(self):
    #     return str(self.staff_name)
    
    # def json(self):
    #     ret = {}
    #     ret['staff_name'] = self.staff_name
    #     ret['email']=self.email
    #     ret['telephone']=self.telephone
    #     ret['certified']=self.certified
    #     return ret
