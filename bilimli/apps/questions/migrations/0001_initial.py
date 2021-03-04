# Generated by Django 3.0.7 on 2020-08-02 14:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('preview', models.CharField(max_length=50, verbose_name='Preview')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 8, 2, 14, 30, 3, 920857, tzinfo=utc), verbose_name='Publiced Date')),
                ('solved', models.BooleanField(default=False, verbose_name='solved')),
                ('comnum', models.IntegerField(verbose_name='Comment number')),
                ('answer', models.CharField(max_length=50, verbose_name='Answer')),
                ('solver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Comment text')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 8, 2, 14, 30, 3, 921638, tzinfo=utc), verbose_name='Comment pubdate')),
                ('correct', models.BooleanField(default=False, verbose_name='Correct')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]