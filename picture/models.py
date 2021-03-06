from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField
    picture_name = models.CharField(max_length=50)
    description = models.TextField(default="")
    location = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    city = models.CharField(max_length=30, default="")
    state = models.CharField(max_length=30, default="")
    posted_by = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images', default="")
    views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default="")

    def __str__(self):
        name = f"{self.state} | {self.area} | {self.location} | {self.picture_name}"
        return name

class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Review(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    title = models.CharField(max_length=50, default="")
    message = models.TextField()
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} | {self.email}"

class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images', default="")
    description = models.TextField()
    designation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} | {self.designation}"