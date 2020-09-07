from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)

    enrollment_years = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
    )

    student_interests = (
            ('coding', 'Coding'),
            ('reading', 'Reading'),
            ('sports', 'Sports'),
            ('music', 'Music'),
            ('dance', 'Dance'),
            ('data science', 'Data Science'),
            ('ai/ml', 'AI/ML'),
            ('iot', 'IoT'),
            ('cyber security', 'Cyber Security'),
            ('video development', 'Video Development'),
            ('databases', 'Databases'),
            ('python', 'Python'),
            ('java', 'Java'),
            ('open source', 'Open Source'),
            ('others', 'Others'),
    )

    branch = models.CharField(
        verbose_name="Branch",
        blank=True, 
        max_length=100,
    )

    enrollment_year = models.CharField(
        verbose_name="Enrollment Year",
        choices=enrollment_years, 
        blank=True, 
        max_length=5,
    )
    preferred_lang = models.CharField(
        verbose_name="Preferred Language",
        blank=True, 
        max_length=100,
    )

    preferred_multimedia = models.CharField(
        verbose_name="Preferred Multimedia",
        blank=True, 
        max_length=100,
    )

    interests = models.CharField(
        verbose_name="Your Interests",
        choices=student_interests,
        blank=True,
        max_length=100,
    )


