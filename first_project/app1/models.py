from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=25)
    mobile = models.BigIntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "test_model"




# create table TestModel (name varchar(100), age int default)