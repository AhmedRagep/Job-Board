# Generated by Django 4.2.1 on 2023-05-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('wepsite', models.URLField()),
                ('cv', models.FileField(upload_to='aplly/')),
                ('cover_letter', models.TextField(max_length=1000)),
            ],
        ),
    ]
