from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='trip/images/')
    #changed(added updated field)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    likes = models.ManyToManyField(User, related_name='trip_post' ,blank=True, default=None)

    def __str__(self):
        return self.title

    #changed
    @property
    def total_likes(self):
        return self.likes.all().count()

#addition
#The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name.
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


#NEW ADDITION
class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES , default='Like', max_length=10)
