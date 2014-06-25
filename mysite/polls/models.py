from django.db import models
from django.utils import timezone
import datetime
#from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
class Poll(models.Model):
  question = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __unicode__(self):  # Python 3: def __str__(self):
    return self.question

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
  poll = models.ForeignKey(Poll)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __unicode__(self):  # Python 3: def __str__(self):
    return self.choice_text
	
	
class Blog(models.Model):
  name = models.CharField(max_length=100)
  tagline = models.TextField()

    # On Python 3: def __str__(self):
  def __unicode__(self):
    return self.name

class Author(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()

    # On Python 3: def __str__(self):
  def __unicode__(self):
    return self.name

class Entry(models.Model):
  blog = models.ForeignKey(Blog)
  headline = models.CharField(max_length=255)
  body_text = models.TextField()
  pub_date = models.DateField()
  mod_date = models.DateField()
  authors = models.ManyToManyField(Author)
  n_comments = models.IntegerField()
  n_pingbacks = models.IntegerField()
  rating = models.IntegerField()

    # On Python 3: def __str__(self):
  def __unicode__(self):
    return self.headline