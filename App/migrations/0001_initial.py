# Generated by Django 2.2.1 on 2021-04-09 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=128)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]