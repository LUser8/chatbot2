from django.db import models
from djongo import models as djongo_model


class ChatAssistent(djongo_model.Model):
    question = djongo_model.CharField(max_length=300)
    answer = djongo_model.TextField()

    def __str__(self):
        return self.question