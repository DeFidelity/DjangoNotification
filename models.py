from django.contrib.auth.models import User
from django.db import models

class Notification(models.Model):
    LIKE = 'like'
    COMMENT = 'comment'
    COMMENT_REPLIES = 'comment_replies'

    CHOICES = (
        (LIKE = 'like'),
        (COMMENT = 'comment'),
        (COMMENT_REPLIES = 'comment_replies')
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_pk = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
