import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string

class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "ko"
    
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, _("English")),
        (LANGUAGE_KOREAN, _("Korean")),
    )
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, _("USD")),
        (CURRENCY_KRW, _("KRW")),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, _("Email")),
        (LOGIN_GITHUB, _("Github")),
        (LOGIN_KAKAO, _("Kakao")),
    )

    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
       _("gender") ,choices=GENDER_CHOICES, max_length=10,blank=True
    )
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(_("language"),choices=LANGUAGE_CHOICES,max_length=5, blank=True, default=LANGUAGE_KOREAN)
    currency = models.CharField(_("currency"),choices=CURRENCY_CHOICES, max_length=5, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=100, default="", blank=True)
    login_method = models.CharField(_("login_method"),choices=LOGIN_CHOICES, max_length=20, default=LOGIN_EMAIL )

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            # uuid 랜덤한 임의의숫자를 구현하기위해서 사용함
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret":secret}
            )
            send_mail(
                _("Verify Mybnb Account"),
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message = html_message,
            )
            self.save()
        return
