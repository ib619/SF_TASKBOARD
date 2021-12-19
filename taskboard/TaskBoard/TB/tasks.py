from celery import shared_task
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from .models import Article, Response
import datetime as DT
from django.contrib.auth.models import User


@shared_task
def latest_news():
    all_posts = Article.objects.all().order_by('-date')
    length = len(all_posts)
    post_list = []

    all_users = User.objects.all()

    for i in range(length):
        week_ago = DT.date.today() - DT.timedelta(days=7)
        condition = all_posts[i].date.date() > week_ago
        if condition:
            post_list.append(all_posts[i])
        else:
            break

    for user in all_users:
        html_content = render_to_string(
            'celery_weekly_mail.html',
            {
                'articles': post_list,
                'sub_name': user.username,
            }
        )

        msg = EmailMultiAlternatives(
            subject="Here's whats you've missed this week",
            body=f'Hello, {user.username}! These are the articles you missed last week!',
            from_email='igorbodnarprog@yandex.ru',
            to=[user.email],
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=True)



@shared_task
def send_notification(response_id):
    response = Response.objects.get(pk=response_id)
    target = response.article.author

    send_mail(f'Good news, {target.username}!',
              f'{response.author.username} has responded to your article {response.article.title}!',
              'igorbodnarprog@yandex.ru',
              [target.email],
              fail_silently=True)
