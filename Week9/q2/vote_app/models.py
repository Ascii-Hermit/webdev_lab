from django.db import models

class Vote(models.Model):
    GOOD = 'Good'
    SATISFACTORY = 'Satisfactory'
    BAD = 'Bad'

    VOTE_CHOICES = [
        (GOOD, 'Good'),
        (SATISFACTORY, 'Satisfactory'),
        (BAD, 'Bad'),
    ]

    vote_choice = models.CharField(max_length=15, choices=VOTE_CHOICES)

    def __str__(self):
        return self.vote_choice
