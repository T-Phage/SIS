# from re import T
# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.http.request import split_domain_port

# Create your models here.
class Guardian(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    othername = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255, null=True, default="")
    email = models.EmailField()
    profession = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    gps = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def _str__(self):
        return self.fullname


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

GENDER = [('male','male'),
        ('female','female')]
StudentLevel = [('Basic 1','Basic 1'),
                ('Basic 2','Basic 2'),
                ('Basic 3','Basic 3'),
                ('Basic 4','Basic 4'),
                ('Basic 5','Basic 5'),
                ('Basic 6','Basic 6'),
                ('Basic 7','Basic 7'),
                ('Basic 8','Basic 8'),
                ('Basic 9','Basic 9')]

GROUP = [('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D')]
class MyUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(
        verbose_name='firstname',
        max_length=255,
        null=True,
        unique=True
    )
    phone = models.CharField(
        verbose_name='mobile number',
        max_length=15,
        null=True,
    )
    # othername = models.CharField(
    #     verbose_name='othernames',
    #     max_length=255,
    #     null=True,
    #     blank=True,
    # )
    gender = models.CharField(
        verbose_name='gender',
        max_length=255,
        null=True, default='null',
        choices=GENDER,
    )
    date_of_birth = models.DateField(
        auto_now_add=True
    )
    group = models.CharField(
        max_length=2,
        null=True, choices=GROUP
    )
    level = models.CharField(
        max_length=10, null=True,
        choices=StudentLevel
    )
    yearOfadmission = models.CharField(
        max_length=10, null=True,
        default='null'
    )
    classAdmitted = models.CharField(
        max_length=10, null=True, choices=StudentLevel
    )
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    guardian = models.ForeignKey(Guardian, blank=True, null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_full_name(self):
        # The user is identified by their email address
        return self.firstname + " " + self.surname

    class Meta:
        verbose_name_plural = 'Users'


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5, unique=True)
    title = models.CharField(max_length=20)
    period = models.IntegerField(default=20)
    # teacher = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


LEVEL =[('Basic 1 Term 1','Basic 1 Term 1'),
        ('Basic 1 Term 2','Basic 1 Term 2'),
        ('Basic 1 Term 3','Basic 1 Term 3'),
        ('Basic 2 Term 1','Basic 2 Term 1'),
        ('Basic 2 Term 2','Basic 2 Term 2'),
        ('Basic 2 Term 3','Basic 2 Term 3'),
        ('Basic 3 Term 1','Basic 3 Term 1'),
        ('Basic 3 Term 2','Basic 3 Term 2'),
        ('Basic 3 Term 3','Basic 3 Term 3'),
        ('Basic 4 Term 1','Basic 4 Term 1'),
        ('Basic 4 Term 2','Basic 4 Term 2'),
        ('Basic 4 Term 3','Basic 4 Term 3'),
        ('Basic 5 Term 1','Basic 5 Term 1'),
        ('Basic 5 Term 2','Basic 5 Term 2'),
        ('Basic 5 Term 3','Basic 5 Term 3'),
        ('Basic 6 Term 1','Basic 6 Term 1'),
        ('Basic 6 Term 2','Basic 6 Term 2'),
        ('Basic 6 Term 3','Basic 6 Term 3'),
        ('Basic 7 Term 1','Basic 7 Term 1'),
        ('Basic 7 Term 2','Basic 7 Term 2'),
        ('Basic 7 Term 3','Basic 7 Term 3'),
        ('Basic 8 Term 1','Basic 8 Term 1'),
        ('Basic 8 Term 2','Basic 8 Term 2'),
        ('Basic 8 Term 3','Basic 8 Term 3'),
        ('Basic 9 Term 1','Basic 9 Term 1'),
        ('Basic 9 Term 2','Basic 9 Term 2'),
        ('Basic 9 Term 3','Basic 9 Term 3')]

# class Level(models.Model):
#     level = models.CharField(max_length=17, unique=True, null=True)

#     def __str__(self):
#         return str(self.level)

class Results(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    classScore = models.IntegerField()
    examscore = models.IntegerField()
    totalscore = models.IntegerField()
    position = models.CharField(max_length=10, null=True)
    level = models.CharField(max_length=17, null=False, blank=False)
    # term = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Results'
        # ordering = ['-level']


class Final(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    year = models.CharField(max_length=8)
    aggregate = models.FloatField(default=0.0)
    average = models.FloatField(default=0.0)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    transaction_id = models.IntegerField()
    amount = models.FloatField()
    currency = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)
    flw_ref = models.CharField(max_length=20)
    tx_ref = models.CharField(max_length=20, default="hooli-tx-1920bbtyt")

    class Meta:
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.status

class Fees(models.Model):
    pass