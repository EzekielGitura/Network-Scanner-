# Network Scanner

## Overview
A comprehensive network discovery and scanning tool built with Python, leveraging Scapy for network interactions.

## Features
- ARP Network Discovery
- Hostname Resolution
- Basic Port Scanning
- Logging Capabilities
- Flexible Command-Line Interface

## Prerequisites
- Python 3.8+
- Scapy
- Root/Administrator Privileges

## Installation
```bash
git clone https://github.com/EzekielGitura/network-scanner.git
cd network-scanner
pip install -r requirements.txt
```

## Usage
```bash
# Basic ARP Scan
python main.py -t 192.168.1.0/24

# Scan with output to file
python main.py -t 192.168.1.0/24 -o results.txt

# Verbose mode
python main.py -t 192.168.1.0/24 -v

# Scan specific ports
python main.py -t 192.168.1.1 --ports 22 80 443
```

## Security Warning
🚨 **IMPORTANT**: Always obtain explicit permission before scanning networks or systems you do not own. Unauthorized network scanning may be considered a cybersecurity offense.

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License
MIT License

## Disclaimer
This tool is for educational and authorized testing purposes only. Misuse may be illegal and unethical.
