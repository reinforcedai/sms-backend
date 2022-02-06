# Generated by Django 4.0.1 on 2022-02-06 09:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentportal', '0003_remove_student_nin_alter_student_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Performances',
            },
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, choices=[('1', 'First Term'), ('2', 'Second Term'), ('3', 'Third Term')], max_length=32, null=True)),
                ('remark', models.CharField(blank=True, choices=[('PASS', 'PASS'), ('FAIL', 'FAIL')], max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name="Instructor's name")),
                ('signature', models.FileField(blank=True, help_text='upload signature of the instructor', upload_to='')),
                ('remark_in_pdf', models.FileField(blank=True, help_text='upload remark in PDF format', upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Remark on the student',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='student',
        ),
        migrations.RemoveField(
            model_name='result',
            name='current_class',
        ),
        migrations.RemoveField(
            model_name='student',
            name='level',
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendance',
            field=models.CharField(blank=True, choices=[('P', 'Present'), ('A', 'Absence')], max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='parent',
            name='email',
            field=models.EmailField(default=1, max_length=255, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Parent or Guardian'),
        ),
        migrations.AddField(
            model_name='parent',
            name='phone_number',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='average_score',
            field=models.FloatField(blank=True, default=0, max_length=32, null=True, verbose_name='Average score'),
        ),
        migrations.AddField(
            model_name='result',
            name='class_arm',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Class arm'),
        ),
        migrations.AddField(
            model_name='result',
            name='class_average_score',
            field=models.FloatField(blank=True, default=0, max_length=32, null=True, verbose_name='Class average score'),
        ),
        migrations.AddField(
            model_name='result',
            name='class_highest_score',
            field=models.FloatField(blank=True, default=0, max_length=32, null=True, verbose_name='Class highest score'),
        ),
        migrations.AddField(
            model_name='result',
            name='class_lowest_score',
            field=models.FloatField(blank=True, default=0, max_length=32, null=True, verbose_name='Class highest score'),
        ),
        migrations.AddField(
            model_name='result',
            name='class_position',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Position in class'),
        ),
        migrations.AddField(
            model_name='result',
            name='continuous_assessment',
            field=models.FloatField(blank=True, default=0, max_length=32, null=True, verbose_name='Continuous assessment score'),
        ),
        migrations.AddField(
            model_name='result',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='result',
            name='result_in_pdf',
            field=models.FileField(blank=True, help_text='upload result in PDF format', upload_to=''),
        ),
        migrations.AddField(
            model_name='result',
            name='total_students_number',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total number of students in class'),
        ),
        migrations.AddField(
            model_name='result',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='last modified date'),
        ),
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, help_text='upload profile photo', upload_to=''),
        ),
        migrations.AlterField(
            model_name='result',
            name='exam_score',
            field=models.FloatField(blank=True, default=0, max_length=32, null=True, verbose_name='Exam score'),
        ),
        migrations.AlterField(
            model_name='result',
            name='session',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Academic session'),
        ),
        migrations.AlterField(
            model_name='result',
            name='term',
            field=models.CharField(blank=True, choices=[('1', 'First Term'), ('2', 'Second Term'), ('3', 'Third Term')], max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='test_score',
            field=models.FloatField(blank=True, default=0, max_length=32, null=True, verbose_name='Test score'),
        ),
        migrations.DeleteModel(
            name='NominalRoll',
        ),
        migrations.DeleteModel(
            name='Transcript',
        ),
        migrations.AddField(
            model_name='remark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.student'),
        ),
        migrations.AddField(
            model_name='performance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.student'),
        ),
        migrations.AddField(
            model_name='performance',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentportal.subject'),
        ),
    ]