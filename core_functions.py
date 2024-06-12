import socket
import requests
from datetime import datetime


def get_ping(address: str) -> bool:
    """
    Ping a network address to check its availability.

    Parameters:
    - address (str): The network address (IP or domain) to ping.

    Returns:
    - int: Returns 1 if the address is reachable, 0 otherwise.

    Raises:
    - subprocess.CalledProcessError: If the subprocess (ping command) encounters an error.

    Example:
    >>> get_ping("127.0.0.1")
    1
    """
    try:
        if address.startswith(('http://', 'https://')):
            address = address.split('://')[1]

        # Split the address into host and port (if available)
        parts = address.split(':')
        host = parts[0]
        port = int(parts[1]) if len(parts) == 2 else 80

        # Create a socket and try to connect
        with socket.create_connection((host, port), timeout=10):
            print(f'Ping {address} successfully.')
            return True

    except (socket.timeout, socket.error):
        print(f'Ping {address} unsuccessfully!')
        return False


def get_status(address: str) -> bool:
    """
    Retrieve the HTTP status code for a given web address.

    Parameters:
    - address (str): The URL or web address to check.

    Returns:
    - int: Returns 1 if the HTTP status code is in the range 200-205 (success),
           otherwise returns 0.

    Raises:
    - Exception: If there is an error during the HTTP request.

    Example:
    >>> get_status("https://www.example.com")
    1
    """
    try:
        # Send an HTTP GET request to the specified address
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'}
        if address.startswith('http://') or address.startswith('https://'):
            response = requests.get(address, headers=headers, timeout=100, proxies={'http': '', 'https': ''})
        else:
            response = requests.get(f"http://{address}", headers=headers, timeout=100, proxies={'http': '', 'https': ''})

        # Get the HTTP status code from the response
        status = response.status_code

        # Check if the status code indicates success (in the range 200-205)
        if status in range(200, 206):
            print(f'Status {address} successfully.')
            return True  # Success
        else:
            print(f'Status {address} unsuccessfully!')
            return False  # Not in the success range

    except requests.RequestException as e:
        print(f'Status {address} unsuccessfully!')
        print(f"Error: {e}")
        # Handle exceptions and return 0
        return False


def get_load_time(address: str) -> bool:
    """
    Measure the response time of a web address.

    Parameters:
    - address (str): The URL or web address to measure the response time for.

    Returns:
    - int: Returns 1 if the response time is less than or equal to 20 seconds,
           otherwise returns 0.

    Raises:
    - Exception: If there is an error during the HTTP request.

    Example:
    >>> get_load_time("https://www.example.com")
    1
    """
    load_time = 0
    try:
        # Record the start time of the HTTP request
        start_time = datetime.now().second

        # Send an HTTP GET request to the specified address
        requests.get(f"http://{address}", timeout=20)

        # Record the end time of the HTTP request
        end_time = datetime.now().second

        # Calculate the response time in seconds
        if start_time < end_time:
            load_time = end_time - start_time
        elif start_time > end_time:
            load_time = start_time - end_time

        # Check if the response time is within an acceptable range (<= 30 seconds)
        if load_time <= 30:
            print(f'Load {address} successfully.')
            return True  # Response time is within acceptable range
        else:
            print(f'Load {address} unsuccessfully!')
            return False  # Response time exceeds the acceptable range

    except requests.exceptions.RequestException:
        # Handle exceptions and return an error message
        print(f'Load {address} unsuccessfully!')
        return False
