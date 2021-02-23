# Generated by Django 3.1.3 on 2021-02-23 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_forum_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='forum',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.section'),
        ),
    ]
