from django.db import models

# Create your models here.

class Breeds(models.Model):
    ID = models.AutoField(primary_key=True, serialize=False)
    Raza = models.CharField(max_length=100, null=False)
    ImageURL = models.CharField(max_length=200, null=False)

    def __str__(self):
        return '%s, %s, %s' %(self.ID, self.Raza, self.ImageURL)