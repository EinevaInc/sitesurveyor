from django.shortcuts import render

def index(request):
    """
    View function for the home page of the site.
    """
    context = {
        'message': 'Welcome to Site Surveyor!',
        'features': [
            {'title': 'High Accuracy', 'description': 'Leverage cutting-edge algorithms for precise measurements.'},
            {'title': 'User-Friendly Interface', 'description': 'Intuitive design for surveyors of all skill levels.'},
            {'title': 'Collaborative Tools', 'description': 'Work seamlessly with your team on surveying projects.'},
        ],
    }
    return render(request, 'home/index.html', context)