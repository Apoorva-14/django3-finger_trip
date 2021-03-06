from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email


class Trip(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='trip/images/')
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    likes = models.ManyToManyField(User, related_name='trip_post' ,blank=True, default=None)
    slug = models.CharField(max_length=130)


    def __str__(self):
        return self.title

    #changed
    @property
    def total_likes(self):
        return self.likes.all().count()


#The first element in each tuple is the actual value to be set on the model,
#and the second element is the human-readable name.
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES , default='Like', max_length=10)


class Comment(models.Model):
    comment_text = models.TextField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
