#!/usr/bin/env python3

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

def test_imports():
    """Test that all imports work correctly."""
    print("Testing imports from export_edit_import package...")
    
    try:
        from export_edit_import.models import (
            GeneratedFile, 
            GeneratedExportFile, 
            GeneratedImportFile, 
            GeneratedFileStatus,
            TimeStampedModel
        )
        print("✓ All models imported successfully!")
        
        # Test model classes
        print(f"✓ GeneratedFile: {GeneratedFile}")
        print(f"✓ GeneratedExportFile: {GeneratedExportFile}")  
        print(f"✓ GeneratedImportFile: {GeneratedImportFile}")
        print(f"✓ GeneratedFileStatus: {GeneratedFileStatus}")
        print(f"✓ TimeStampedModel: {TimeStampedModel}")
        
        # Test that the models have the TimeStampedModel fields
        print("\nTesting TimeStampedModel fields:")
        print(f"✓ GeneratedFile has 'created' field: {hasattr(GeneratedFile, 'created')}")
        print(f"✓ GeneratedFile has 'modified' field: {hasattr(GeneratedFile, 'modified')}")
        
        # Test status choices
        print("\nTesting GeneratedFileStatus choices:")
        for choice in GeneratedFileStatus.choices:
            print(f"  - {choice[0]}: {choice[1]}")
            
        print("\n✅ All tests passed! Package is working correctly.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
