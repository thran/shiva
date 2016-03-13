# coding=utf-8
import uuid

from constance import config
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os
from unidecode import unidecode
from shiva import settings


def update_filename(instance, filename):
    path = "faces"
    ext = instance.photo.url.split(".")[-1]
    file = "{0}.{1}".format(uuid.uuid4(), ext)
    return os.path.join(path, file)


class Face(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Jméno")
    alternatives = models.CharField(max_length=255, verbose_name=u"Alternativní jména, oddělená středníkem", blank=True, null=True)
    hint = models.CharField(max_length=255, verbose_name=u"Nápověda", blank=True, null=True)
    photo = models.ImageField(upload_to=update_filename)
    photo_thumb = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def is_solved(self):
        return 0 < self.guess_set.filter(correct=True).count()

    def guess_name(self, guess):
        if unidecode(self.name.lower()) == unidecode(guess.lower()):
            return True

        return unidecode(guess.lower()) in unidecode(self.alternatives.lower()).split(";")


class Guess(models.Model):
    face = models.ForeignKey(Face)
    text = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    correct = models.BooleanField()

    def __unicode__(self):
        return self.text


class Chat(models.Model):
    text = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Face)
def make_thumb(instance, **kwargs):
    size_thumb = 100
    size = 500

    path_to_media = ".." if settings.ON_VIPER else "."

    img = Image.open(path_to_media + instance.photo.url)
    size2 = 1. * size_thumb * max(img.size) / min(img.size)
    img.thumbnail((size2, size2), Image.ANTIALIAS)
    img = img.crop((
        (img.size[0] - 100) / 2,
        (img.size[1] - 100) / 2,
        100 + (img.size[0] - 100) / 2,
        100 + (img.size[1] - 100) / 2,
    ))

    url = os.path.join("faces", "small", instance.photo.name.split("/")[-1])
    if config.DISTORT:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save(os.path.join(settings.MEDIA_ROOT, url))
    instance.photo_thumb = url

    post_save.disconnect(make_thumb, Face)
    instance.save()
    post_save.connect(make_thumb, Face)

    if config.DISTORT:
        img = Image.open(path_to_media + instance.photo.url)
        img.thumbnail((size, size), Image.ANTIALIAS)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img.save(path_to_media + instance.photo.url)

