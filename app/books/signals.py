from books.models import Author
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


@receiver(pre_save, sender=Author)
def pre_save_edit_first_name_author(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=Author)
def pre_save_edit_last_name_author(sender, instance, **kwargs):
    instance.last_name = instance.last_name.capitalize()


@receiver(pre_delete, sender=Author)
def pre_delete_author(sender, instance, **kwargs):
    raise Exception('Deleting prohibited')
