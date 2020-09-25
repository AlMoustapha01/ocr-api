from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import User
# Create your models here.
class UsersManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,first_name,last_name,email,created_at,updated_at,created_by,updated_by, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('The given username must be set')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=self.model.normalize_username(username),
            email=self.normalize_email(email),
            created_at=created_at,
            updated_at=updated_at,
            created_by= created_by,
            updated_by=updated_by,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, first_name,last_name,email,created_at,updated_at,created_by,updated_by, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            created_at=created_at,
            updated_at=updated_at,
            created_by= created_by,
            updated_by=updated_by,
            username=self.model.normalize_username(username),
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name,last_name,email,created_at,updated_at,created_by,updated_by, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            created_at=created_at,
            updated_at=updated_at,
            created_by= created_by,
            updated_by=updated_by,
            username=self.model.normalize_username(username),
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    objects=UsersManager()
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','email','created_at','updated_at','created_by','updated_by'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.last_name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

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
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
        

    class Meta:
        managed = 'True'
        db_table = 'users'