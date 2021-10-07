from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Notification

@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_pk = request.GET.get('notification', 0)
    extra_pk = request.GET.get('extra_pk', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_pk)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.LIKE:
            return redirect('[url of the page to view the liked post]', post_pk=notification.extra_pk)
        elif notification.notification_type == Notification.COMMENT:
            return redirect('[name of the url to view the post user commented on]', post_pk=notification.extra_pk)
        elif notification.notification_type == Notification.COMMENT_REPLIES:
            return redirect('[name of the url to view comment that got replied to]', comment_pk=notification.extra_pk)
    # this can be increase to the length you desired
    return render(request, 'notification/notifications.html')
