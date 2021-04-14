from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = f"{'https://djangovueattackapplice3.herokuapp.com/reset-password-new'}?token={reset_password_token.key}"

    send_mail(
        # title:
        "Password Reset for {title} {usernames}".format(title="Some website title", usernames=reset_password_token.user.username),
        # message:
        f'{email_plaintext_message} \n {reset_password_token.user.username}',
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

    # print("reset_password_token.user", reset_password_token.user.username)


class Life(models.Model):
    number = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} {self.number}'
