from django.http import HttpResponse
from django.shortcuts import render
from .models import Data
import json
import math
from django.template import loader


def data(request):
    with open('friends.json', 'r') as file:
        friends_list = json.load(file)
        for obj in friends_list:
            b = Data()
            b.name = obj['name']
            b.longitude = obj["longitude"]
            b.latitude = obj['latitude']
            b.user_id = obj['user_id']
            b.save()
        return render(request, 'new/index.html')


all_names = Data.objects.all()


def calculations(request):
    if request.method == 'POST':
        latitude = float(request.POST.get('Latitude', None))
        longitude = float(request.POST.get('Longitude', None))
        distance = float(request.POST.get('Distance', None))
        required_names = []
        for entry in all_names:
            dis = math.sqrt((entry.longitude - longitude) ** 2 + (entry.latitude - latitude) ** 2)
            if dis <= distance:
                required_names.append([entry.user_id, entry.name])
        return render(request, 'new/invitees.html', {'names': required_names})
