from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
User= settings.AUTH_USER_MODEL
# Create your models here.


class Job(models.Model):

    category = (
        ('FT',"Full-Time"),
        ('PT',"Part-Time"),
        ('CT',"Contract"),
        ('RT',"Remote"),
        ('IT',"Internship"),
       
    )
    country = (
        ('kenya',"Kenya"),
    )
    experience_length = (
        ("no","No Experience"),
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
    )
    Notice_time = (
        ("0","0weeks"),
        ("1","1 week"),
        ("2","2 weeks"),
        ("3","3 weeks"),
        ("4","4 weeks"),
        ("5","more than a month")
    )
    salary = (
        ('confidential','Confidential'),
        ('0-5000','0-5000'),
        ('5100-10000','5100-10000'),
        ('10001-20000','10001-20000'),
        ('20001-30000','20001-30000'),
        ('30001-40000','30001-40000'),
        ('40001-50000','40001-50000'),
        ('50001 and above','50001 and above'),
    )
    Interview = (

        ("walkin", "Walk-in"),
        ("remotely", "remotely"),
    )

    user = models.ForeignKey(User, related_name='employer', on_delete=models.CASCADE,null=True)
    function = models.CharField(max_length=300)
    slug = models.SlugField(max_length=5000,blank = True,null = True)
    description = models.CharField(max_length=500)
    country = CountryField(default = 'KE')
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.function