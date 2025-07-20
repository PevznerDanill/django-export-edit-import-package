# Django Export Edit Import

A Django app for exporting, editing, and importing data with Excel files. This package provides a comprehensive solution for handling data import/export workflows in Django applications.

## Features

- Export Django model data to Excel files
- Import data from Excel files with validation
- Edit data through Excel interface
- Business logic validation
- Celery integration for background processing
- Error handling and reporting
- Customizable field mappings

## Installation

### From Private PyPI

```bash
pip install --index-url https://pypi.your.internal/simple/ django-export-edit-import==1.0.0
```

### From Source

```bash
pip install django-export-edit-import
```

## Quick Start

1. Add `django_export_edit_import` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'django_export_edit_import',
    ...
]
```

2. Run migrations:

```bash
python manage.py migrate django_export_edit_import
```

3. Include the app's URLs in your project's `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('export-import/', include('django_export_edit_import.urls')),
    ...
]
```

## Configuration

### Settings

Add these settings to your Django settings file:

```python
# Celery configuration (if using background processing)
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Export/Import settings
EXPORT_EDIT_IMPORT = {
    'UPLOAD_PATH': 'uploads/import_files/',
    'EXPORT_PATH': 'exports/',
    'MAX_FILE_SIZE': 10 * 1024 * 1024,  # 10MB
    'ALLOWED_EXTENSIONS': ['.xlsx', '.xls'],
}
```

## Usage

### Basic Export

```python
from django_export_edit_import.create_export_excel_file import ExcelExporter
from myapp.models import MyModel

exporter = ExcelExporter(MyModel)
file_path = exporter.export_to_excel(
    queryset=MyModel.objects.all(),
    file_name="my_export.xlsx"
)
```

### Basic Import

```python
from django_export_edit_import.import_processors import ExcelImportProcessor
from myapp.models import MyModel

processor = ExcelImportProcessor(MyModel)
result = processor.process_file("path/to/import_file.xlsx")
```

## Dependencies

- Django >= 3.2
- openpyxl >= 3.0.9
- celery >= 5.0.0
- pandas >= 1.3.0

## License

MIT License

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## Support

For support, email support@yourcompany.com or create an issue on GitHub.
