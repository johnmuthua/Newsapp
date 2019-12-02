# Generated by Django 2.2.8 on 2019-12-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('urlToImage', models.URLField()),
                ('publishedAt', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]