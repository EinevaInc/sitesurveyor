# 🌍 SiteSurveyor - Open-Source Land Surveying Software

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Django Version](https://img.shields.io/badge/django-4.2-brightgreen.svg)](https://www.djangoproject.com/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/EinevaInc/sitesurveyor/pulls)

**The Future of Opensource Land Surveying**

<img src="https://images.unsplash.com/photo-1604881988758-f76ad2f7aac1" alt="SiteSurveyor in Action" style="border-radius: 10px; margin: 20px 0" width="800">

## 🚀 Why SiteSurveyor?

Traditional land surveying software is expensive, proprietary, and limits innovation. SiteSurveyor breaks these barriers by offering:

✅ **Professional-grade tools** for all surveying disciplines  
✅ **Complete data ownership** with no vendor lock-in  
✅ **Community-driven development** shaped by real surveyors  
✅ **Modern web-based interface** with mobile readiness  
✅ **Zero-cost solution** under MIT License

```bash
# Featured Capabilities
1. Advanced Coordinate Transformations
2. CAD-Grade Drafting Tools
3. LiDAR Point Cloud Processing
4. Automated Volume Calculations
5. Real-Time Collaboration
```



### 🔄 Modern Workflow Integration
- **Cloud Sync**: Secure Cloud Storage integration
- **Field-Ready**: Offline-first architecture
- **API Access**: RESTful endpoints for enterprise integration
- **Collaboration**: Real-time multi-user editing

## 🏗️ Why Open Source?

| Aspect          | Proprietary Software | SiteSurveyor       |
|-----------------|----------------------|--------------------|
| Cost            | $5k+/year           | Free Forever       |
| Customization   | Limited              | Full Access        |
| Data Security   | Vendor Risk          | Your Control       |
| Updates         | Vendor Timeline      | Community Driven   |
| Interoperability| Closed Formats       | Open Standards     |

**Enterprise Benefits:**
- Reduce software costs by 90%
- Eliminate licensing headaches
- Future-proof your workflow
- Participate in feature development

## 🛠️ Installation

### Requirements
- Python 3.10+
- PostgreSQL 14+ with PostGIS
- Node.js 18+ (for upcoming web components)

### Quick Start
```bash
# Clone repository
git clone https://github.com/EinevaInc/sitesurveyor.git
cd sitesurveyor

# Set up environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure database (PostGIS required)
createdb sitesurveyor
psql sitesurveyor -c "CREATE EXTENSION postgis;"

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Access the web interface at `http://localhost:8000`

## 📈 Roadmap 2025

- **Q1**: Mobile Field Data Collection App

## 🤝 How to Contribute

We welcome:
- Surveying professionals for requesting features
- GIS developers for feature enhancement and development
- Technical writers for documentation
- Translators for localization

**First-time contributors** check our [Good First Issues](https://github.com/EinevaInc/sitesurveyor/contribute)

## 📚 Learning Resources

1. [Getting Started Guide](docs/getting-started.md)
2. [API Reference](docs/api.md)
3. [Video Tutorials](https://youtube.com/sitesurveyor)
4. [Community Forum](https://forum.sitesurveyor.app)

## 📜 License

SiteSurveyor is MIT Licensed - see [LICENSE](LICENSE) for details.
