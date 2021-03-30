# Generated by Django 3.1.6 on 2021-02-03 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Blog_content', models.TextField()),
                ('Image', models.ImageField(upload_to='')),
                ('Date_blog', models.DateField()),
                ('Approval_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('From_email', models.EmailField(max_length=254)),
                ('To_email', models.EmailField(max_length=254)),
                ('Message_content', models.TextField(default='Nil')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=200)),
                ('Last_name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Registration_date', models.DateField()),
                ('Num_of_courses_enrolled', models.IntegerField(default=0)),
                ('Num_of_courses_completed', models.IntegerField(default=0)),
                ('Qualification', models.TextField()),
                ('Introduction_brief', models.TextField()),
                ('Image', models.ImageField(upload_to='media')),
                ('Num_of_enrolled_students', models.IntegerField()),
                ('Average_review_rating', models.IntegerField()),
                ('Num_of_reviews', models.IntegerField()),
                ('About_website', models.TextField()),
                ('User_role', models.CharField(max_length=200)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject_title', models.CharField(max_length=200)),
                ('Course_title', models.CharField(max_length=200)),
                ('Course_brief', models.TextField()),
                ('Course_duration', models.IntegerField()),
                ('Num_of_chapters', models.IntegerField()),
                ('Course_fee', models.FloatField()),
                ('Language', models.CharField(max_length=200)),
                ('Chapter_title', models.CharField(max_length=200)),
                ('Num_of_assignments', models.IntegerField()),
                ('Chapter_Content_name', models.ImageField(null=True, upload_to='media')),
                ('Chapter_text_content', models.TextField()),
                ('Chapter_Content_type', models.CharField(max_length=200)),
                ('Chapter_Content_Is_mandatory', models.BooleanField()),
                ('Chapter_Content_Time_required_in_sec', models.IntegerField()),
                ('Chapter_Content_Is_open_for_free', models.BooleanField()),
                ('Sub_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('User_category', models.CharField(max_length=200)),
                ('Old_password', models.CharField(max_length=200)),
                ('New_password', models.CharField(max_length=200)),
                ('Req_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Learning_progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=200)),
                ('Student_email', models.EmailField(max_length=254)),
                ('Subject_name', models.CharField(max_length=200)),
                ('Course_name', models.CharField(max_length=200)),
                ('Course_chapter_name', models.CharField(max_length=200)),
                ('Course_chapter_content_name', models.ImageField(null=True, upload_to='media')),
                ('Begin_timestamp', models.DateTimeField(auto_now_add=True)),
                ('Completion_timestamp', models.DateTimeField(auto_now=True)),
                ('Status', models.CharField(max_length=200)),
                ('Teacher_email', models.EmailField(max_length=200, null=True)),
                ('Learn_p_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=200)),
                ('Student_email', models.EmailField(max_length=254)),
                ('Teacher_name', models.CharField(max_length=200)),
                ('Teacher_email', models.EmailField(max_length=254)),
                ('Subject_name', models.CharField(max_length=200)),
                ('Course_name', models.CharField(max_length=200)),
                ('Rating_score', models.IntegerField()),
                ('Feedback_text', models.TextField(default='Nil')),
                ('Submission_date', models.DateField()),
                ('Feed_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=200)),
                ('Student_email', models.EmailField(max_length=200)),
                ('Teacher_name', models.CharField(max_length=200)),
                ('Subject_name', models.CharField(max_length=200)),
                ('Total_marks', models.IntegerField()),
                ('Acquired_marks', models.IntegerField()),
                ('Grade', models.CharField(max_length=200)),
                ('Time_stop', models.DateTimeField(auto_now=True)),
                ('Exam_res_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=200)),
                ('Student_email', models.EmailField(max_length=254)),
                ('Teacher_name', models.CharField(max_length=200)),
                ('Subject_name', models.CharField(max_length=200)),
                ('Course_name', models.CharField(max_length=200)),
                ('Question', models.TextField()),
                ('Option1', models.TextField()),
                ('Option2', models.TextField()),
                ('Option3', models.TextField()),
                ('Correct_answer', models.TextField()),
                ('Lock', models.CharField(max_length=200)),
                ('Time_start', models.DateTimeField()),
                ('Time_stop', models.DateTimeField()),
                ('Exam_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=200)),
                ('Student_email', models.EmailField(max_length=254)),
                ('Subject_name', models.CharField(max_length=200)),
                ('Course_name', models.CharField(max_length=200)),
                ('Teacher_name', models.CharField(max_length=200)),
                ('Teacher_email', models.EmailField(max_length=254)),
                ('Attendance', models.IntegerField()),
                ('Pending_days', models.IntegerField()),
                ('Enrollment_date', models.DateField(auto_now_add=True)),
                ('Teacher_response', models.CharField(max_length=200)),
                ('Paid_amount', models.FloatField()),
                ('Certificate', models.CharField(max_length=200)),
                ('Is_paid_subscription', models.BooleanField()),
                ('notify', models.CharField(max_length=200, null=True)),
                ('enrol_reg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='learn.registration')),
            ],
        ),
    ]
