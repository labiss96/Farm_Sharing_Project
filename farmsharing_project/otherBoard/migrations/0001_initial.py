# Generated by Django 2.2.7 on 2019-11-29 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('region', models.CharField(max_length=200, null=True)),
                ('joined_people', models.IntegerField(default=0)),
                ('current_joined', models.BooleanField(default=True, max_length=200)),
                ('active_period_start', models.CharField(default=0, max_length=200)),
                ('active_period_end', models.CharField(default=0, max_length=200)),
                ('purpose', models.CharField(max_length=200, null=True)),
                ('body', models.CharField(max_length=200, null=True)),
                ('pub_date', models.DateTimeField(null=True, verbose_name='Date published')),
                ('scrap', models.ManyToManyField(blank=True, related_name='Profile_scrap', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('body', models.CharField(max_length=200, null=True)),
                ('picture', django_fields.fields.DefaultStaticImageField(blank=True, upload_to='picture/')),
                ('score', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(null=True, verbose_name='Date published')),
                ('like', models.ManyToManyField(blank=True, related_name='Profile_like', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review_comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otherBoard.Review')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Join_comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('join', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otherBoard.Join')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
