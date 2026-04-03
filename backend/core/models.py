import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    User customizado com UUID.
    Previne IDOR (Insecure Direct Object Reference).
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    is_premium = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class QuizQuestion(models.Model):
    """
    Questões do Quiz com UUID.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    question_text = models.TextField()
    domain = models.IntegerField(
        help_text="Domínio do Security+ (1-5)"
    )
    correct_options_json = models.JSONField(
        help_text="Opções corretas em JSON"
    )
    explanation = models.TextField()

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'


class UserProgress(models.Model):
    """
    Progresso do usuário no Quiz.
    """
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    last_login = models.DateTimeField(auto_now=True)
    streak_days = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Progresso'
        verbose_name_plural = 'Progressos'


