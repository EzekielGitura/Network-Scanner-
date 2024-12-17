"""
Network Scanner Package Initialization

This file ensures the src directory is recognized as a Python package
and can perform any necessary package-level setup.
"""

# Import key classes to make them easily accessible
from .scanner import NetworkScanner
from .cli import CLIHandler
from .utils import NetworkUtils

# Package-level configuration or setup can be done here
__version__ = "0.1.0"
__all__ = [
    'NetworkScanner', 
    'CLIHandler', 
    'NetworkUtils'
]

# Optional: Package-level setup
def setup_package():
    """
    Optional package initialization function
    Can be used for global configurations, logging setup, etc.
    """
    import logging
    
    # Configure global logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
