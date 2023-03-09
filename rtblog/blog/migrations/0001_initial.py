# Generated by Django 3.2.17 on 2023-03-02 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Url', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='category/')),
                ('Add_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Post_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Content', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('Images', models.ImageField(upload_to='post/')),
                ('Cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]