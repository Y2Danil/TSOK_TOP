# Generated by Django 3.0.6 on 2020-06-11 04:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('create_author', models.CharField(max_length=100, verbose_name='Автор идеи')),
                ('title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст статьие')),
                ('created_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, db_index=True, null=True)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60, verbose_name='Автор комментария')),
                ('comment_text', models.TextField(max_length=500, verbose_name='Текст комметария')),
                ('pub_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Top.Article')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Top.Rubric', verbose_name='Рубрика'),
        ),
    ]
