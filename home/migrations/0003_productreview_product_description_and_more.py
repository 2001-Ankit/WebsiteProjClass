# Generated by Django 4.1.3 on 2022-11-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=400)),
                ('username', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=100)),
                ('review', models.TextField(blank=True)),
                ('star', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(choices=[('in stock', 'In stock'), ('out of stock', 'Out of stock')], max_length=100),
        ),
    ]
