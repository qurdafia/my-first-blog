from django.db import models
from django.utils import timezone



#def upload_loc(post, filename):
    #return "%s/%s" %(post.id, filename)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.ImageField(
        #upload_to='/home/mormash/mysite/images',
        blank=True, null=True,
        height_field='height_field',
        width_field='width_field',
    )
    height_field = models.IntegerField(blank=True, null=True)
    width_field = models.IntegerField(blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

#Comment Model

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
