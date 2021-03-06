# Generated by Django 4.0.2 on 2022-02-16 13:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='???????? ????????????????')),
                ('profession', models.CharField(blank=True, help_text='??????????????????', max_length=150, verbose_name='??????????????????')),
                ('about', models.TextField(blank=True, help_text='?? ????????', verbose_name='?? ????????')),
                ('photo', models.ImageField(blank=True, upload_to='media/img/user_img/%Y/%m/%d/', verbose_name='????????')),
                ('summary', models.FileField(blank=True, upload_to='media/doc/user_doc/%Y/%m/%d/', verbose_name='????????????')),
                ('Phone', models.CharField(blank=True, help_text='??????????????', max_length=15, verbose_name='??????????????')),
                ('skills', models.TextField(blank=True, help_text='????????????', verbose_name='????????????')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '????????????????????????',
                'verbose_name_plural': '????????????????????????',
                'ordering': ['-date_joined'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperiance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(help_text='????????????????', max_length=150, verbose_name='????????????????')),
                ('position', models.CharField(help_text='??????????????????', max_length=150, verbose_name='??????????????????')),
                ('responsibilities', models.TextField(blank=True, help_text='??????????????????????', verbose_name='??????????????????????')),
                ('date_of_employment', models.DateField(blank=True, verbose_name='???????? ???????????? ???? ????????????')),
                ('date_of_dismissal', models.DateField(blank=True, verbose_name='???????? ????????????????????')),
                ('custom_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='????????????????????????')),
            ],
            options={
                'verbose_name': '???????? ????????????',
                'verbose_name_plural': '???????? ????????????',
                'ordering': ['-date_of_employment'],
            },
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_link_name', models.CharField(help_text='???????????????? ???????????????????? ????????', max_length=150, verbose_name='???????????????? ???????????????????? ????????')),
                ('link_value', models.CharField(help_text='????????????', max_length=150, verbose_name='????????????')),
                ('custom_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='????????????????????????')),
            ],
            options={
                'verbose_name': '???????????????????? ????????',
                'verbose_name_plural': '???????????????????? ????????',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_study', models.CharField(help_text='?????????? ??????????', max_length=150, verbose_name='?????????? ??????????')),
                ('degree', models.CharField(blank=True, help_text='??????????????', max_length=150, verbose_name='??????????????')),
                ('date_of_admission', models.DateField(blank=True, verbose_name='???????? ??????????????????????')),
                ('date_of_graduation', models.DateField(blank=True, verbose_name='???????? ??????????????????')),
                ('custom_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='????????????????????????')),
            ],
            options={
                'verbose_name': '??????????????????????',
                'verbose_name_plural': '??????????????????????',
                'ordering': ['-date_of_admission'],
            },
        ),
    ]
