#!/usr/bin/env python3
import scapy.all as scapy
import socket
import logging
from typing import List, Dict

class NetworkScanner:
    def __init__(self, log_path='logs/scanner.log'):
        # Set up logging
        logging.basicConfig(
            filename=log_path, 
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def arp_scan(self, ip_range: str) -> List[Dict[str, str]]:
        """
        Perform ARP scan on given IP range
        
        :param ip_range: IP range to scan (e.g., '192.168.1.0/24')
        :return: List of discovered devices
        """
        try:
            # Create ARP request packet
            arp_request = scapy.ARP(pdst=ip_range)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = broadcast/arp_request
            
            # Send packet and receive responses
            responses = scapy.srp(packet, timeout=2, retry=2, verbose=False)[0]
            
            discovered_devices = []
            for sent, received in responses:
                device_info = {
                    "ip": received.psrc,
                    "mac": received.hwsrc,
                    "hostname": self._resolve_hostname(received.psrc)
                }
                discovered_devices.append(device_info)
                
                # Log discovered devices
                self.logger.info(f"Device discovered: {device_info}")
            
            return discovered_devices
        
        except Exception as e:
            self.logger.error(f"ARP scan error: {e}")
            return []

    def _resolve_hostname(self, ip: str) -> str:
        """
        Resolve IP to hostname
        
        :param ip: IP address to resolve
        :return: Hostname or original IP
        """
        try:
            return socket.gethostbyaddr(ip)[0]
        except (socket.herror, socket.gaierror):
            return ip

    def port_scan(self, ip: str, ports: List[int] = None):
        """
        Perform basic port scanning
        
        :param ip: Target IP address
        :param ports: List of ports to scan (optional)
        :return: Dictionary of open ports
        """
        if not ports:
            ports = [21, 22, 23, 80, 443, 3306, 3389]
        
        open_ports = {}
        
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            
            if result == 0:
                open_ports[port] = self._get_service_name(port)
            
            sock.close()
        
        return open_ports

    def _get_service_name(self, port: int) -> str:
        """
        Retrieve standard service name for a port
        
        :param port: Port number
        :return: Service name
        """
        try:
            return socket.getservbyport(port)
        except:
            return "Unknown"
