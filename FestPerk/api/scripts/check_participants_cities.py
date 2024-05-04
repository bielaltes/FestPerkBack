def check_participants_cities():
    from api.models import Travel, Participant

    participants = Participant.objects.all()
    for participant in participants:
        party_city = participant.party.club.city
        traveler_cities = [travel.city for travel in Travel.objects.filter(traveler=participant.traveler)]
        if party_city not in traveler_cities:
            print(f"{participant.party.uuid} is not in the same city as {participant.traveler.user.username}")
            return
    print("Every city is ok")


if __name__ == "__main__":
    from api.scripts.django_setup import django_setup

    django_setup()
    check_participants_cities()
