from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_contact_us_email(form_data):
    message = f'''
            Email from: {form_data["contact_to_email"]}
            Name: {form_data["full_name"]}

            Message: {form_data["message"]}
            '''
    sender = 'fenderoksp@gmail.com'
    send_mail(
        'Contact Us',
        message,
        sender,
        [sender],
        fail_silently=False,
    )


@shared_task
def debug():
    debug_message = ('DEBUG ' * 10)
    return debug_message
