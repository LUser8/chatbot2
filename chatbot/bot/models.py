# Project Model

# for mysql, postgres, oracle databases
# from django.db import models

# for mongodb
from djongo import models


# Class for Model
class ChatAssistant(models.Model):
    """ChatAssistant model for storing questions and answers for the app."""

    question = models.CharField(max_length=300)
    answer = models.TextField()

    # object representation
    def __str__(self):
        return self.question
