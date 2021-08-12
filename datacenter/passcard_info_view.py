from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    all_visits_of_a_person = Visit.objects.filter(passcard__passcode=passcode)
    
    this_passcard_visits = []
    for visit in all_visits_of_a_person:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': Visit.format_duration(visit),
                'is_strange': Visit.is_visit_long(visit)
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
