from django.shortcuts import render, redirect
from .forms import FeatureRequestForm
# from django.core.mail import send_mail # Removed: Email sending is on hold
# from django.conf import settings # Removed

def index(request):
      # ... (your existing index view code) ...
    features = [
        {
            'title': 'Import & Export Various Data Formats',
            'description': 'Seamlessly import and export data in industry-standard formats like CSV, TXT, DXF, DWG, LandXML, Shapefiles, and raw data from total stations and GNSS receivers.',
            'icon': 'fas fa-file-import'
        },
        {
            'title': 'Coordinate Systems & Transformations',
            'description': 'Work with geographic, projected, and local grid coordinate systems. Perform accurate transformations between different systems, including geoid model support.',
            'icon': 'fas fa-globe-americas'
        },
        {
            'title': 'Comprehensive Calculations',
            'description': 'Perform a wide range of calculations, including distance, angle, area, traverse adjustments (Compass, Transit, Crandall, Least Squares), and COGO calculations.',
            'icon': 'fas fa-calculator'
        },
        {
            'title': 'Advanced Calculations',
            'description': 'Handle complex calculations like earthwork (cut/fill), vertical and horizontal curves, slope, and grade. Generate 3D surface models (TINs, DEMs).',
            'icon': 'fas fa-chart-line'
        },
        {
            'title': 'CAD Integration',
            'description': 'Import and export DXF/DWG files with improved fidelity. Utilize basic CAD editing tools directly within the software.',
            'icon': 'fas fa-drafting-compass'
        },
        {
            'title': 'Point Cloud Processing',
            'description': 'Import, visualize, and process point cloud data from LiDAR or photogrammetry. Filter, classify, and generate surfaces from point clouds.',
            'icon': 'fas fa-cloud'
        },
        {
            'title': 'Engineering Surveying Tools',
            'description': 'Access specialized tools for road design, profile and cross-section generation, and stakeout tasks.',
            'icon': 'fas fa-drafting-compass'
        },
        {
            'title': 'Mining Surveying Tools',
            'description': 'Perform volume calculations, stockpile monitoring, and access pit design tools for mining operations.',
            'icon': 'fas fa-hammer'
        },
         {
            'title': 'Topographic Surveying Tools',
            'description': 'Generate contours, edit TINs, and manage breaklines for detailed topographic mapping.',
            'icon': 'fas fa-map'
        },
        {
            'title': 'Remote Sensing Integration',
            'description': 'Work with orthophotos and DEM data. Extract features from remote sensing imagery.',
            'icon': 'fas fa-satellite-dish'
        },

    ]

    context = {
        'message': 'Revolutionizing Land Surveying',
        'features': features,
    }
    return render(request, 'home/index.html', context)

def feature_request_view(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the FeatureRequest to the database
            return redirect('home:index')  # Redirect to the home page
    else:
        form = FeatureRequestForm()

    return render(request, 'home/feature_request.html', {'form': form})