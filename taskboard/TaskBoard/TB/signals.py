from .models import Response
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail


@receiver(post_save, sender=Response)
def check_delete_condition(sender, instance, **kwargs):
    if instance.decision == 'reject':
        instance.delete()

    if instance.decision == 'accept':
        send_mail(f'Good news, {instance.author.username}!',
                  f'{instance.article.author.username} has accepted your response to article {instance.article.title}!',
                  'igorbodnarprog@yandex.ru',
                  [instance.author.email],
                  fail_silently=True)
