from django.shortcuts import render


# Create your views here.

def tracks_list(request):
    tracks = [
        {'id': 1, 'name': 'BackEnd'},
        {'id': 2, 'name': 'FrontEnd'},
    ]

    # Create a context dictionary to pass data to the template
    context = {
        'tracks': tracks
    }

    return render(request, 'track/tracks_list.html', context)
def track_create(request):
    return render(request, 'track/track_create.html')
def track_update(request):
    return render(request, 'track/track_update.html')
def track_details(request):
    return render(request, 'track/track_details.html')
def track_delete(request):
    return render(request, 'track/track_delete.html')
