from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
CATEGORY = (
    ('0', ("articles")),
    ('1', ("Academics")),
    ('2', ("Career")),
    ('3', ("Science & Technology")),
    ('4', ('Lifestyle')),

)


class Article(models.Model):
    category = models.CharField(max_length= 30, choices = CATEGORY, default= 0)
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Author ")
    title = models.CharField(max_length = 200,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    article_image = models.FileField(blank = True,null = True,verbose_name="Image")
    article_image2 = models.FileField(blank=True, null= True, verbose_name = "Image 2")
    slug = models.SlugField(unique=True, max_length=100, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)        

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "Comment Author")
    comment_content = models.CharField(max_length = 200,verbose_name = "Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
