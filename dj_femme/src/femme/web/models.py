from django.db import models

from django.utils.translation import gettext_lazy as _





# Create your models here.
class RegistrationClass(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    dob = models.DateField()
    message = models.TextField()

    class Meta:
        db_table = 'web_registration'
        verbose_name = _('registration')
        verbose_name_plural = _('registrations')

    def __unicode__(self):
        return self.name


class AboutClass(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to="web/about/")

    class Meta:
        db_table = 'web_about'
        verbose_name = _('about')
        verbose_name_plural = _('abouts')

    def __unicode__(self):
        return self.title

class IssuesClass(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to="web/issues/")

    class Meta:
        db_table = 'web_issues'
        verbose_name = _('issues')
        verbose_name_plural = _('issues')

    def __unicode__(self):
        return self.title

class WhyfemmeClass(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to="web/whyfemme/")

    class Meta:
        db_table = 'web_whyfemme'
        verbose_name = _('whyfemme')
        verbose_name_plural = _('whyfemmes')

    def __unicode__(self):
        return self.title


class TextClass(models.Model):
    title = models.CharField(max_length=128)
    content = models.ForeignKey(WhyfemmeClass, on_delete=models.CASCADE, related_name="whyfemme_text")

    class Meta:
        db_table = 'web_text'
        verbose_name = _('text')
        verbose_name_plural = _('texts')

    def __unicode__(self):
        return self.title


