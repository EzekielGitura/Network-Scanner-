#!/usr/bin/env python3
from src.scanner import NetworkScanner
from src.cli import CLIHandler
import sys

def main():
    try:
        # Parse CLI arguments
        args = CLIHandler.parse_arguments()
        
        # Initialize scanner
        scanner = NetworkScanner()
        
        # Perform scan
        results = scanner.arp_scan(args.target)
        
        # Print or save results
        if not results:
            print("[!] No devices found.")
            sys.exit(1)
        
        print("\n[+] Discovered Devices:")
        print("-" * 50)
        print("{:<20} {:<20} {:<20}".format("IP", "MAC", "Hostname"))
        print("-" * 50)
        
        for device in results:
            print("{:<20} {:<20} {:<20}".format(
                device['ip'], 
                device['mac'], 
                device['hostname']
            ))
        
        # Optional: Save to file if output specified
        if args.output:
            with open(args.output, 'w') as f:
                for device in results:
                    f.write(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {device['hostname']}\n")
            print(f"\n[+] Results saved to {args.output}")
    
    except Exception as e:
        print(f"[!] An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
