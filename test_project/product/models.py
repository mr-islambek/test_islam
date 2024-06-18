from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(upload_to='images/')
    website = models.TextField()
    # followers = models.ManyToManyField(Follow, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

class  Follow (models.Model):
    follower  = models.OneToOneField(User,  on_delete=models.CASCADE, related_name='follower')
    following = models.OneToOneField(User , on_delete=models.CASCADE, related_name='following')
    create_at = models.DateTimeField(auto_now_add= True )


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True )
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    hashtag = models.CharField(max_length=64)


    def number_of_likes(self):
        return self.likes.count()


class PostLike(models.Model):
    user  = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True )


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True )


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True )


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    video= models.FileField(upload_to='videos/', null=True, verbose_name="")
    created_at = models.DateTimeField(auto_now_add= True )
    # expires_at =

class Group(models.Model):
    name = models.CharField(max_length=124)
    description = models.TextField()
    creator  = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='creator')
    members = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='members')
    join_key = models.CharField(max_length=124)