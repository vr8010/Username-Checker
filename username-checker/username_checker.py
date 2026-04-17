#!/usr/bin/env python3
"""
Username Checker - Check username availability across multiple platforms
"""




import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def load_sites(filename='sites.json'):
    """Load platform URLs from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return {}


def check_username(platform, url_template, username, timeout=5):
    """
    Check if username exists on a platform
    Returns: (platform, url, status, is_taken)
    """
    url = url_template.format(username)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        
        # Check status code
        if response.status_code == 200:
            return (platform, url, "Taken", True)
        elif response.status_code == 404:
            return (platform, url, "Available", False)
        else:
            return (platform, url, f"Unknown ({response.status_code})", None)
            
    except requests.exceptions.Timeout:
        return (platform, url, "Timeout", None)
    except requests.exceptions.RequestException as e:
        return (platform, url, "Error", None)


def check_all_platforms(username, sites):
    """Check username across all platforms using multithreading"""
    results = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all tasks
        future_to_platform = {
            executor.submit(check_username, platform, url, username): platform
            for platform, url in sites.items()
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_platform):
            results.append(future.result())
    
    return results


def display_results(results):
    """Display results in a formatted manner"""
    print("\n" + "="*60)
    print("RESULTS:")
    print("="*60)
    
    # Sort results: Taken first, then Available, then others
    taken = [r for r in results if r[3] is True]
    available = [r for r in results if r[3] is False]
    unknown = [r for r in results if r[3] is None]
    
    for platform, url, status, _ in taken:
        print(f"{platform:<15}: {status:<12} -> {url}")
    
    for platform, url, status, _ in available:
        print(f"{platform:<15}: {status:<12}")
    
    for platform, url, status, _ in unknown:
        print(f"{platform:<15}: {status:<12}")
    
    print("="*60)


def main():
    """Main function"""
    print("="*60)
    print(" "*20 + "USERNAME CHECKER")
    print("="*60)
    
    # Load sites
    sites = load_sites()
    if not sites:
        print("No platforms to check. Exiting.")
        return
    
    # Get username from user
    username = input("\nEnter username to check: ").strip()
    
    if not username:
        print("Username cannot be empty!")
        return
    
    print(f"\nChecking availability for '{username}'...")
    print("Please wait...\n")
    
    # Check all platforms
    start_time = time.time()
    results = check_all_platforms(username, sites)
    elapsed_time = time.time() - start_time
    
    # Display results
    display_results(results)
    print(f"\nCompleted in {elapsed_time:.2f} seconds")
    print("\n⚠️  Disclaimer: This tool is for educational purposes only.")
    print("Use responsibly and ethically.\n")


if __name__ == "__main__":
    main()
