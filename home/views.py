from django.shortcuts import render, redirect
from .forms import FeatureRequestForm  # Import the form!
# from django.core.mail import send_mail # Removed: Email sending is on hold
# from django.conf import settings # Removed

def index(request):
    """
    View function for the home page of the site.
    """
    features = [
        {
            'title': 'Import & Export Various Data Formats',
            'description': 'Seamlessly import and export data in industry-standard formats like CSV, TXT, DXF, DWG, LandXML, Shapefiles, and raw data from total stations and GNSS receivers.',
            'icon': 'file-earmark-arrow-down'  # Example Bootstrap icon
        },
        {
            'title': 'Coordinate Systems & Transformations',
            'description': 'Work with geographic, projected, and local grid coordinate systems. Perform accurate transformations between different systems, including geoid model support.',
            'icon': 'geo-alt'
        },
        {
            'title': 'Comprehensive Calculations',
            'description': 'Perform a wide range of calculations, including distance, angle, area, traverse adjustments (Compass, Transit, Crandall, Least Squares), and COGO calculations.',
            'icon': 'calculator'
        },
        {
            'title': 'Advanced Calculations',
            'description': 'Handle complex calculations like earthwork (cut/fill), vertical and horizontal curves, slope, and grade. Generate 3D surface models (TINs, DEMs).',
            'icon': 'calculator-fill'
        },
        {
            'title': 'CAD Integration',
            'description': 'Import and export DXF/DWG files with improved fidelity. Utilize basic CAD editing tools directly within the software.',
            'icon': 'pencil-square'
        },
        {
            'title': 'Point Cloud Processing',
            'description': 'Import, visualize, and process point cloud data from LiDAR or photogrammetry. Filter, classify, and generate surfaces from point clouds.',
            'icon': 'cloud-arrow-down'
        },
        {
            'title': 'Engineering Surveying Tools',
            'description': 'Access specialized tools for road design, profile and cross-section generation, and stakeout tasks.',
            'icon': 'wrench-adjustable-circle'  # Example: Engineering-related icon
        },
        {
            'title': 'Mining Surveying Tools',
            'description': 'Perform volume calculations, stockpile monitoring, and access pit design tools for mining operations.',
            'icon': 'hammer' # Example: Mining related icon
        },
         {
            'title': 'Topographic Surveying Tools',
            'description': 'Generate contours, edit TINs, and manage breaklines for detailed topographic mapping.',
            'icon': 'map'
        },
        {
            'title': 'Remote Sensing Integration',
            'description': 'Work with orthophotos and DEM data. Extract features from remote sensing imagery.',
            'icon': 'globe-americas'
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