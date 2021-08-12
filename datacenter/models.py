from django.db import models

from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_duration(self):
        if self.leaved_at:
            delta = self.leaved_at - self.entered_at
        else:
            delta = localtime() - self.entered_at
        return delta.total_seconds()

    def format_duration(self):
        time_in_seconds = self.get_duration()
        
        hours = time_in_seconds // 3600
        minutes = (time_in_seconds % 3600) // 60
        seconds = time_in_seconds - hours*3600 - minutes*60

        hours, minutes, seconds = map(int, (hours, minutes, seconds))
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    
    def is_visit_long(self, minutes=60):
        return self.get_duration() // 60 > minutes
