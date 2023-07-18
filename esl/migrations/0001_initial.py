# Generated by Django 4.2.1 on 2023-07-11 13:23

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import esl.validators
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[(1, "admin"), (2, "instructor"), (3, "learner")],
                        default=1,
                        max_length=10,
                    ),
                ),
                ("picture", models.ImageField(default=False, upload_to="user_pic")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Dictionary",
            fields=[
                ("signId", models.AutoField(primary_key=True, serialize=False)),
                ("signImage", models.ImageField(upload_to="pics")),
                ("textForSign", models.TextField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="VideoLecture",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("caption", models.CharField(max_length=100)),
                (
                    "video",
                    models.FileField(
                        upload_to="video_lecture", validators=[esl.validators.file_size]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IntermediateVideo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=20)),
                (
                    "video",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="esl.videolecture",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Intermediate",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=20)),
                (
                    "dictionary",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="esl.dictionary"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Instructor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.BooleanField(default=False)),
                ("description", models.TextField(max_length=255)),
                (
                    "phoneNo",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("document", models.FileField(upload_to="doc_pic")),
                ("id_pic", models.ImageField(upload_to="id_pic")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedBackLearner",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("feedback", models.TextField()),
                ("feedback_reply", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "Learner_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedBackInstructor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("feedback", models.TextField()),
                ("feedback_reply", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "Instructor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BeginnerVideo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=20)),
                (
                    "video",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="esl.videolecture",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Beginner",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=20)),
                (
                    "dictionary",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="esl.dictionary"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AdvancedVideo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=20)),
                (
                    "video",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="esl.videolecture",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Advanced",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.CharField(max_length=20)),
                (
                    "dictionary",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="esl.dictionary"
                    ),
                ),
            ],
        ),
    ]
