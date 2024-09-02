from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Train, Availability, Station


# Create your views here.
def home(request):
    return render(request, "home.html")

def search_trains(request):
    if request.method == 'POST':
        start_journey = request.POST['start_journey']
        end_journey = request.POST['end_journey']
        journey_date = request.POST['journey_date']
        trains = Train.objects.filter(
            start_journey__station_name=start_journey,
            end_journey__station_name=end_journey
        )

        availability = {train.Train_no: Availability.objects.filter(train_no=train).first() for train in trains}
        return render(request, 'search_result.html', {
            'start_journey': start_journey,
            'end_journey': end_journey,
            'journey_date': journey_date,
            'trains': trains,
            'availability': availability
        })
    else:
        return redirect('home')