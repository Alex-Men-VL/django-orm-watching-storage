from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime

def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for person in visits:
        non_closed_visits.append(
            {
                'who_entered': person.passcard.owner_name,
                'entered_at': localtime(person.entered_at),
                'duration': Visit.format_duration(person),
                'is_strange': Visit.is_visit_long(person)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
