import os

import django
from django.utils.timezone import localtime
from django.utils import timezone
from datetime import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit

if __name__ == '__main__':
    # Программируем здесь
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    active_passcards = Passcard.objects.filter(is_active=True)
    # print('Активных пропусков:', len(active_passcards))
    person = active_passcards[0].owner_name
    print(person)
    all_visit = Visit.objects.all()
    person_visit = Visit.objects.filter(passcard__owner_name=person)
    print(len(person_visit))
    print(person_visit)

















    filter_visit = Visit.objects.filter(leaved_at__isnull=True)
    print(filter_visit)
    for i in filter_visit:
        pass_card = i.passcard
        print(pass_card.owner_name)

































    # for line in all_visit:
    #     print('Зашёл в хранилище, время по Москве:')
    #     print(localtime(line.entered_at), end='\n\n')
    #
    #     print('Находится в хранилище:')
    #     start_time = line.entered_at
    #     end_time = line.leaved_at or timezone.now()
    #     delta = end_time - start_time
    #     all_seconds = int(delta.total_seconds())
    #     hours = all_seconds // 3600
    #     minutes = (all_seconds % 3600) // 60
    #     seconds = all_seconds % 60
    #     time_string = f"{hours}:{minutes}:{seconds}"
    #     data_and_time = datetime.strptime(time_string, "%H:%M:%S")
    #     print(data_and_time.time(), end='\n\n')