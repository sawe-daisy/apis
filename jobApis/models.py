from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _

# Create your models here.

USER_TYPE = (
    ('JS',"Job Seeker"),
    ('EM',"Employer")
)

class User(AbstractUser):
    firstname = CharField(_("Firstname"),blank=True, null=True,max_length=255)
    lastname = CharField(_("Lastname"),blank=True, null=True,max_length=255)
    email = CharField(_("Email"),blank=True, null=True,max_length=255)
    phone_no = PhoneNumberField(_("Phone Number"),blank=True,null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self) -> str:
        return self.username
   
    
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

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
        return self.firstname + ' ' + self.lastname