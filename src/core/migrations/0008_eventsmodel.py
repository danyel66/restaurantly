# Generated by Django 3.0 on 2020-12-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201214_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='events/%Y/%m/%d')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Event',
                'ordering': ('title',),
            },
        ),
    ]
