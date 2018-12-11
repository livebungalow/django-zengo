# Generated by Django 2.1.4 on 2018-12-11 01:03

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import konst.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('zendesk_id', models.BigIntegerField(unique=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('public', models.BooleanField()),
                ('created', models.DateTimeField()),
                ('notified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_data', models.TextField()),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('processed', models.BooleanField(default=False)),
                ('error', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('zendesk_id', models.BigIntegerField(unique=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('status', konst.models.fields.ConstantChoiceCharField(choices=[('new', 'new'), ('open', 'open'), ('pending', 'pending'), ('hold', 'hold'), ('solved', 'solved'), ('closed', 'closed')], max_length=8)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZendeskUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('zendesk_id', models.BigIntegerField(unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='zendesk_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zengo.ZendeskUser'),
        ),
        migrations.AddField(
            model_name='event',
            name='actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zengo.ZendeskUser'),
        ),
        migrations.AddField(
            model_name='event',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zengo.Ticket'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zengo.ZendeskUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zengo.Ticket'),
        ),
    ]
