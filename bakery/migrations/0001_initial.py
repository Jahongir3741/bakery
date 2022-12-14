# Generated by Django 4.1.3 on 2022-11-17 13:31

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uspdate', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('text', models.TextField()),
                ('image', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='category.category')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breans', to='accounts.staff')),
            ],
        ),
        migrations.CreateModel(
            name='BreadItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uspdate', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveIntegerField()),
                ('bread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breads', to='bakery.bread')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breaditems', to='accounts.staff')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bakery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('uspdate', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('open_at', models.TimeField()),
                ('close_at', models.TimeField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bakeries', to='accounts.staff')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_bakery', to='accounts.diroctor')),
            ],
        ),
        migrations.AddConstraint(
            model_name='bread',
            constraint=models.UniqueConstraint(fields=('name', 'category'), name='name_and_category_unique'),
        ),
        migrations.AddConstraint(
            model_name='bakery',
            constraint=models.UniqueConstraint(fields=('name', 'location'), name='location'),
        ),
    ]
