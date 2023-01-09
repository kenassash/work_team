# Generated by Django 4.1.2 on 2022-10-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0006_category_notification_like_comment_articlecategory'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='articlecategory',
            constraint=models.UniqueConstraint(fields=('category_guid', 'article_guid'),
                                               name='articles_articlecategory_unique'),
        ),
    ]
