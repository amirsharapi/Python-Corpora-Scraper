# Generated by Django 2.0.4 on 2018-05-06 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movichome', '0003_remove_pagescrape_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagescrape',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]