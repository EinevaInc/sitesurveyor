# SiteSurveyor

SiteSurveyor is an open-source Land Surveying software designed to revolutionize the surveying industry. Available on web, mobile, and desktop platforms, SiteSurveyor supports both online and offline modes, enabling surveyors to perform their tasks efficiently and save their data to the cloud. The software is applicable in various surveying categories, including Engineering Survey, Mining Survey, Topographic Survey, Remote Sensing, and Cadastral Survey.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Cross-Platform**: Available on web, mobile, and desktop platforms.
- **Offline Mode**: Perform surveys without an internet connection and sync data once online.
- **Cloud Storage**: Save and manage survey data securely in the cloud.
- **User Management**: Secure authentication and role-based access control.
- **Dynamic Forms**: Create and manage survey forms dynamically.
- **Data Visualization**: Real-time data visualization and reporting.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies
SiteSurveyor leverages the following technologies:
- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Version Control**: Git

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- Node.js (for frontend dependencies)

### Steps
1. **Clone the repository**:
    ```sh
    git clone https://github.com/EinevaInc/sitesurveyor.git
    cd sitesurveyor
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install backend dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Install frontend dependencies**:
    ```sh
    npm install
    ```

5. **Set up the database**:
    ```sh
    psql -U postgres -c "CREATE DATABASE sitesurveyor;"
    psql -U postgres -c "CREATE USER sitesurveyor_user WITH PASSWORD 'yourpassword';"
    psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE sitesurveyor TO sitesurveyor_user;"
    ```

6. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:8000`.
2. Register for an account or log in with your credentials.
3. Create, manage, and visualize surveys as needed.

## Project Structure
```
sitesurveyor/
├── home/                # Contains modules or components related to the "home" functionality
├── sitesurveyor/        # Main Django application directory
│   ├── __init__.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI configuration
├── .env                 # Environment configuration file
├── .gitignore           # Specifies files and directories to be ignored by Git
├── LICENSE              # License file
├── manage.py            # Django management script
├── package.json         # Node.js dependencies and scripts
├── README.md            # Project description and instructions
└── requirements.txt     # Python dependencies
```

## Contributing
We welcome contributions to SiteSurveyor! To contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
