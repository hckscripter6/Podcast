# Generated by Django 2.1.1 on 2018-10-08 01:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import storages.backends.s3boto3


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, storage=storages.backends.s3boto3.S3Boto3Storage(bucket='podcast-app'), upload_to='')),
                ('recording', models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(bucket='podcast-app'), upload_to='')),
                ('slug', models.SlugField(unique=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='tags',
            field=models.ManyToManyField(to='collection.Tag'),
        ),
    ]
