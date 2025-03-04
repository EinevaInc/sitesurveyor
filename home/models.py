from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class FeatureRequest(models.Model):
    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('import_export', 'Import/Export Data'),
        ('coordinate_systems', 'Coordinate Systems & Transformations'),
        ('calculations_basic', 'Basic Calculations (Distance, Angle, Area)'),
        ('calculations_advanced', 'Advanced Calculations (Traverse, Earthwork, etc.)'),
        ('cad_integration', 'CAD Integration'),
        ('point_cloud', 'Point Cloud Processing'),
        ('engineering_surveying', 'Engineering Surveying Tools'),
        ('mining_surveying', 'Mining Surveying Tools'),
        ('topographic_surveying', 'Topographic Surveying Tools'),
        ('remote_sensing', 'Remote Sensing Integration'),
        ('other', 'Other'), # Always include an "Other" option
    ]

    URGENCY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    feature_title = models.CharField(max_length=255)
    feature_description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='general')
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, default='medium')
    submission_date = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    agree_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.feature_title

    class Meta:
        verbose_name = "Feature Request"
        verbose_name_plural = "Feature Requests"
        ordering = ['-submission_date']  # Order by submission date (newest first)