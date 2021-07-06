from django.db import models
from django.db.models import signals
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

SCHEDULE_TYPE={
    'Minutes':IntervalSchedule.MINUTES,
    'Hours':IntervalSchedule.HOURS,
    'Days':IntervalSchedule.DAYS,
    'Seconds':IntervalSchedule.SECONDS
}


def create_sites(sender, instance, created, **kwargs):
    schedule,created =IntervalSchedule.objects.get_or_create(
        every=instance.value,period=SCHEDULE_TYPE.get(instance.type,"Minutes")
    )

    PeriodicTask.objects.create(
        interval=schedule,
        name=instance.name+" "+instance.url,
        task='sitetesting.tasks.update_website_status',
        args=json.dumps([instance.url])
    )

    print("instance",instance.url)
    
    pass

# Create your models here.

class Sites(models.Model):
    type_choices=(('Minutes', 'Minutes'),('Hours', 'Hours'),('Days', 'Days'))
    website_choices=(('Up','Up'),('Down','Down'))
    name=models.CharField(max_length=20)
    url=models.URLField(max_length=255)
    type=models.CharField(max_length=255,choices=type_choices)
    value=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    website_type=models.CharField(max_length=10,choices=website_choices)


signals.post_save.connect(receiver=create_sites, sender=Sites)