#!/usr/bin/env python3
import ipaddress
import socket

class NetworkUtils:
    @staticmethod
    def validate_ip_range(ip_range: str) -> bool:
        """
        Validate if the provided IP range is valid
        
        :param ip_range: IP range to validate
        :return: Boolean indicating validity
        """
        try:
            ipaddress.ip_network(ip_range, strict=False)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_port_open(ip: str, port: int, timeout: float = 1.0) -> bool:
        """
        Check if a specific port is open on an IP
        
        :param ip: Target IP address
        :param port: Port number to check
        :param timeout: Connection timeout
        :return: Boolean indicating port status
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False
