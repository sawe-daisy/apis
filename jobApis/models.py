from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField

# Create your models here.



class User(AbstractUser):
    USER_TYPE = (
    ('JS',"Job Seeker"),
    ('EM',"Employer")
    )
    name = CharField(_("name"),blank=True, null=True,max_length=255)
    username = CharField(_("username"),blank=True, null=True,max_length=255, unique=True)
    email = CharField(_("Email"),blank=True, null=True,max_length=255, unique=True)
    user_type= models.CharField(choices = USER_TYPE,max_length=200,default=0)
    phone_no = PhoneNumberField(_("Phone Number"),blank=True,null=True)

    EMAIL_FIELD = 'email'

    def __str__(self) -> str:
        return self.email
   
    
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"name": self.email})

    @property
    def is_jobseeker(self):
        if str(self.user_type) == "JS":
            return True
        return False

    @property
    def is_employer(self):
        if str(self.user_type) == "EM":
            return True
        return False

    def  get_full_name(self):
        return self.name

class Job(models.Model):

    job_type = (
        ('FT',"Full-Time"),
        ('PT',"Part-Time"),
        ('CT',"Contract"),
        ('RT',"Remote"),
        ('IT',"Internship"),
       
    )
    country = (
        ('KE',"Kenya"),
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
    education_level = (
        ("Phd","PHD"),
        ("masters","Masters"),
        ("degree","Bachelors Degree"),
        ("diploma","Diploma"),
        ("certificate","Certificate"),
        ("other","Other"),
    
    )

    user = models.ForeignKey(User, related_name='employer', on_delete=models.CASCADE,null=True)
    function = models.CharField(max_length=300)
    slug = models.SlugField(max_length=5000,blank = True,null = True)
    description = models.CharField(max_length=500)
    country = CountryField(default = 'KE')
    location = models.CharField(max_length=20)
    notice = models.CharField(choices = Notice_time,max_length=200,default=0)
    salary = models.CharField(choices = salary,max_length=30, blank=True,null = True,default='confidential')
    edeucation_level = models.CharField(choices = education_level,max_length=200,default='entry')
    job_type = models.CharField(choices = job_type,max_length=200,default='Full-Time"')
    experience_length = models.CharField(choices = experience_length,max_length=200,default=0)
    interview = models.CharField(choices=Interview,max_length=20, default='walkin')

    def __str__(self):
        return self.function