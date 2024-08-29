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

    return render(request, 'trainee/trainees_list.html', context)
def track_create(request):
    return render(request, 'trainee/trainee_create.html')
def track_update(request,id):
    return render(request, 'trainee/trainee_update.html')
def track_details(request,id):
    return render(request, 'trainee/trainee_details.html')
def track_delete(request,id):
    return render(request, 'trainee/trainee_delete.html')
