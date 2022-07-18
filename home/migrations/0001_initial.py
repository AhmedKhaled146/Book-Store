# Generated by Django 4.0.2 on 2022-06-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('image', models.ImageField(upload_to='review_image')),
                ('review', models.TextField(max_length=500)),
                ('rate', models.IntegerField(default=1)),
            ],
        ),
    ]
