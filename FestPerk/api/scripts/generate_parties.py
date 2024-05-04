def generate_parties():
    import random
    from typing import Dict, List

    from django.utils import timezone
    from api.models import Travel, Party, Participant, Club

    today = timezone.now().date()
    travels_today = Travel.objects.filter(
        ini_date__lte=today, end_date__gte=today
    ).order_by("city__name")
    parties = []
    participants = []
    clubs: Dict[str, List[Club]] = Club.objects.get_clubs_by_city()
    current_party = None
    count = 5
    for travel in travels_today:
        if count > 4 or current_party.club.city != travel.city:
            club = random.choice(clubs[travel.city.name])
            current_party = Party(club=club, date=today)
            parties.append(current_party)
            count = 0
        else:
            count += 1
        # Participant
        participants.append(Participant(party=current_party, traveler=travel.traveler))
    Party.objects.bulk_create(parties)
    Participant.objects.bulk_create(participants)


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    generate_parties()
