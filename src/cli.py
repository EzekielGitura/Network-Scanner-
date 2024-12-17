#!/usr/bin/env python3
import argparse
from typing import Dict

class CLIHandler:
    @staticmethod
    def parse_arguments() -> Dict:
        parser = argparse.ArgumentParser(
            description="Advanced Network Discovery and Scanning Tool",
            epilog="Ensure you have permission before scanning networks!"
        )
        parser.add_argument(
            "-t", "--target", 
            required=True, 
            help="Target IP / IP Range (e.g., 192.168.1.0/24)"
        )
        parser.add_argument(
            "-o", "--output", 
            help="Output file for scan results"
        )
        parser.add_argument(
            "-v", "--verbose", 
            action="store_true", 
            help="Enable verbose output"
        )
        parser.add_argument(
            "--ports", 
            nargs='+', 
            type=int, 
            help="Specific ports to scan (optional)"
        )
        
        return vars(parser.parse_args())
