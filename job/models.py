from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


JOB_TYPE = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Freelance', 'Freelance'),
    )
def image_upload (instance, filename):
     imagename , extension = filename.split(".")
     return "jobs/%s/%s.%s"%(instance.id,instance.id,   extension)


class Job(models.Model):  # table
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)  # column
    title = models.CharField(max_length=100)  # column
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)  # column
    description = models.TextField(max_length=1000)  # column
    published_at = models.DateTimeField(auto_now=True)  # column
    Vacancy = models.IntegerField(default=1)  # column
    image = models.ImageField(upload_to=image_upload)  # column 
    salary = models.IntegerField(default=0)  # column
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # column
    experience = models.IntegerField(default=1)  # column

    slug = models.SlugField(blank=True, null=True)



    def save(self,*args,**kwargs):
         ## logic
         self.slug = slugify(self.title)
         super(Job,self).save(*args, **kwargs)



    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)


    def __str__(self):
            return self.name


class Apply(models.Model):
     job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='apply_job')
     name = models.CharField(max_length=50)
     email = models.EmailField(max_length=100)
     website = models.URLField()
     cv = models.FileField(upload_to='apply/')
     cover_letter = models.TextField(max_length=500)
     created_at = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.name