#!/usr/bin/env python3
import unittest
from src.scanner import NetworkScanner
from src.utils import NetworkUtils

class TestNetworkScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = NetworkScanner()
        self.utils = NetworkUtils()

    def test_ip_range_validation(self):
        valid_ranges = ['192.168.1.0/24', '10.0.0.0/16']
        invalid_ranges = ['256.0.0.0/24', 'not_an_ip']
        
        for ip_range in valid_ranges:
            self.assertTrue(self.utils.validate_ip_range(ip_range))
        
        for ip_range in invalid_ranges:
            self.assertFalse(self.utils.validate_ip_range(ip_range))

    def test_port_open_check(self):
        # This test might fail depending on network configuration
        # Replace with appropriate test IPs/ports
        self.assertFalse(self.utils.is_port_open('8.8.8.8', 12345))

if __name__ == '__main__':
    unittest.main()
