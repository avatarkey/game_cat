from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
import PIL

# Create your models here.

class Genre(models.Model):
	name = models.CharField(verbose_name="Name", unique=True, max_length=50, blank=False, null=True)

	class Meta:
		verbose_name = "Genre"
		verbose_name_plural = "Genres"

	def __str__(self):
		return self.name

class Developer(models.Model):
	name = models.CharField(verbose_name="Name", max_length=100, null=True)
	founded = models.DateField(verbose_name="Founded", null=True, blank=True)
	description = models.TextField(verbose_name="Description", null=True, blank=True)

	class Meta:
		verbose_name = "Developer"
		verbose_name_plural = "Developers"

	def __str__(self):
		return self.name

class Game(models.Model):
	name = models.CharField(verbose_name="Name", max_length=100, null=True)
	date = models.DateField(verbose_name="Release Date", null=True, blank=True)
	cover = models.ImageField(verbose_name="Cover", upload_to="covers", null=True, blank=True)
	developer = models.ForeignKey(Developer, verbose_name="Developer", null=True, blank=True)
	genre = models.ManyToManyField(Genre, verbose_name="Genre")
	users = models.ManyToManyField(User, verbose_name="Users")
	
	
	class Meta:
		verbose_name = "Game"
		verbose_name_plural = "Games"

	def __str__(self):
		return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    avatar = models.ImageField(verbose_name="Avatar", upload_to="avatars", null=True, blank=True)
    friends = models.ManyToManyField(User, verbose_name="Friends")
 
    def __str__(self):
        return "{}'s profile".format(self.user.username)
 
    class Meta:
        db_table = 'user_profile'
 
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False
 
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

