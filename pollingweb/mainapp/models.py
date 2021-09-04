from django.db import models
from django_mysql.models import ListCharField

# Create your models here.
class polls(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=70)
    option_two = models.CharField(max_length=70)
    option_three = models.CharField(max_length=70)
    option_four = models.CharField(max_length=70)
    option_one_count = models.IntegerField(default = 0)
    option_two_count = models.IntegerField(default = 0)
    option_three_count = models.IntegerField(default = 0)
    option_four_count = models.IntegerField(default = 0)
    user_name = models.CharField(max_length=50)
    uservote = ListCharField(
        base_field= models.CharField(max_length=30),
        size=20,
        max_length=(200 * 11)  # 6 * 10 character nominals, plus commas
    )
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count