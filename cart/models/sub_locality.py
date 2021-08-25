from django.db import models



class Sub_locality(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
              return self.name

    @staticmethod
    def get_all_sublocalities():
             sub_localities = Sub_locality.objects.all()
             return(sub_localities)
