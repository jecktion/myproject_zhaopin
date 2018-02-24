from django.db import models

# Create your models here.
class Zhilian(models.Model):
    url = models.CharField(max_length=255)
    pname = models.CharField(max_length=16)
    smoney = models.CharField(max_length=16)
    emoney = models.CharField(max_length=16)
    location = models.CharField(max_length=255)
    syear = models.CharField(max_length=16)
    eyear = models.CharField(max_length=16)
    degree = models.CharField(max_length=16)
    ptype = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    date_pub = models.CharField(max_length=32)
    advantage = models.CharField(max_length=255)
    jobdesc = models.CharField(max_length=255)
    jobaddr = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    crawl_time = models.CharField(max_length=32)
    num = models.CharField(max_length=16)

    class Meta:
        db_table = "qiji_job_t"