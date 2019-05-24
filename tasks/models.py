from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

STATUS_CHOICES = (
    ('inprogress', 'In Progress'),
    ('close', 'Close'),
    ('cancelled', 'Cancelled'),
)


class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inprogress')
    completion_date = models.DateTimeField(default=datetime.now()+timedelta(days=20))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Task)
def task_mail(sender, instance, **kwargs):
    if kwargs['created']:
        user_email = instance.user.email
        subject = f'New Task Assigned: {instance.title}'
        from_email = 'asad.manzoor@arbisoft.com'
        text_content = instance.content

        # This functionality is working on local environment & commented for heroku app (missing add-ons issues)
        # send_mail(subject, text_content, from_email, [user_email], fail_silently=False)
