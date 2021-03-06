# Generated by Django 3.1.2 on 2021-03-18 20:23

import account.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50, verbose_name='name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_recruitment_applicant', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', account.models.MyAccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='SandArtReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True, verbose_name='Team Name')),
                ('college', models.CharField(max_length=50, verbose_name='College/University Name')),
                ('mem1', models.CharField(max_length=30, verbose_name='First Member Name')),
                ('mem2', models.CharField(blank=True, max_length=30, verbose_name='Second Member Name')),
                ('mem3', models.CharField(blank=True, max_length=30, verbose_name='Third Member Name')),
                ('mem4', models.CharField(blank=True, max_length=30, verbose_name='Fourth Member Name')),
                ('mem5', models.CharField(blank=True, max_length=30, verbose_name='Fifth Member Name')),
                ('mem6', models.CharField(blank=True, max_length=30, verbose_name='Sixth Member Name')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^(?:(?:\\+|0{0,2})91(\\s*[\\-]\\s*)?|[0]?)?[789]\\d{9}$')], verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('roll_number', models.CharField(max_length=9, unique=True, verbose_name='Roll Number')),
                ('hostel_block', models.CharField(choices=[('First Block', 'First Block'), ('Second Block', 'Second Block'), ('Third Block', 'Third Block'), ('Fourth Block', 'Fourth Block'), ('Fifth Block', 'Fifth Block'), ('Seventh Block', 'Seventh Block'), ('Mega Tower 1', 'Mega Tower 1'), ('Mega Tower 2', 'Mega Tower 2'), ('Mega Tower 3', 'Mega Tower 3'), ('GH1', 'GH1'), ('GH3', 'GH3'), ('GH4', 'GH4'), ('GH5', 'GH5')], max_length=30)),
                ('batch', models.CharField(choices=[('first_year', 'First Year'), ('second_year', 'Second Year'), ('third_year', 'Third Year'), ('final_year', 'Final Year'), ('pg', 'PG')], default='firstYear', max_length=20, verbose_name='Batch')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^(?:(?:\\+|0{0,2})91(\\s*[\\-]\\s*)?|[0]?)?[789]\\d{9}$')], verbose_name='Phone Number')),
                ('event', models.CharField(blank=True, choices=[('Engineer', 'Engineer'), ('Incident', 'Incident'), ('Major Project', 'Major Project')], max_length=20, verbose_name='event')),
            ],
        ),
        migrations.CreateModel(
            name='RecruitmentApplicant',
            fields=[
                ('application_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='application id')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('roll_number', models.CharField(max_length=10, unique=True)),
                ('batch', models.CharField(choices=[('firstYear', 'First Year'), ('secondYear', 'Second Year'), ('thirdYear', 'Third Year'), ('fourthYear', 'Final Year'), ('PostGraduate', 'PG')], max_length=20, verbose_name='Batch')),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science'), ('IT', 'Information Technology'), ('ECE', 'Electronics and Communication'), ('EEE', 'Electronics and Electrical'), ('MECH', 'Mechanical'), ('CV', 'Civil'), ('CH', 'Chemical'), ('META', 'Metallurgy and Materials')], max_length=20, verbose_name='Branch')),
                ('status', models.CharField(choices=[('written', 'Written Test'), ('interview', 'Selected for Interview'), ('selected', 'Selected')], default='written', max_length=20, verbose_name='Status')),
                ('phoneNumber', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Incorrect phone number format', regex='^(?:(?:\\+|0{0,2})91(\\s*[\\-]\\s*)?|[0]?)?[789]\\d{9}$')], verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('recruitmentYear', models.CharField(default=2021, max_length=4)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
