import time
import concurrent.futures
import logging
import configparser
from datetime import datetime

from core_functions import get_ping, get_load_time, get_status
from database.db import *

logging.basicConfig(filename='MyLog.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
config = configparser.ConfigParser()


def main_loop(start_date: str, end_date: str, start_time: str, end_time: str, interval_minutes: int,
              second_interval_minutes: int, target_addresses: str = None, selected_functions: list = None):
    """
    Execute a main loop to continuously check the status of target IP addresses within a specified time range.

    Parameters:
    - start_date (str): The start date in the format '%Y-%m-%d'.
    - end_date (str): The end date in the format '%Y-%m-%d'.
    - start_time (str): The start time in the format '%H:%M:%S'.
    - end_time (str): The end time in the format '%H:%M:%S'.
    - target_addresses (list, optional): A list of target IP addresses to check. Default is ['127.0.0.1'].

    Returns:
    None

    Logs:
    - If any of the target IP addresses is down (unreachable), an error message is logged for each affected IP.
    - The main loop continues until the current date and time exceed the specified end date and time.

    Example:
    >>> main_loop('2022-02-02', '2022-02-02', '17:00:00', '18:00:00', 5, 10, '127.0.0.1')
    """

    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    start_time = datetime.strptime(start_time, "%H:%M:%S").time()
    # h_start, m_start, s_start = start_time.hour, start_time.minute, start_time.second

    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    end_time = datetime.strptime(end_time, "%H:%M:%S").time()
    # h_end, m_end, s_end = end_time.hour, end_time.minute, end_time.second

    try:
        results = []
        while True:
            # Check the status of target IP addresses
            current_time = datetime.now()
            print('\n')
            result = check_selected_function(target_addresses, second_interval_minutes, selected_functions)
            results.append(result)
            print('******')
            print('\n')
            time.sleep(interval_minutes * 6)

            # Break the loop if the current date and time exceed the specified end date and time
            if current_time.date() > end_date:
                print('Date ended.')
                break
            if current_time.time() > end_time:
                print('Time ended.')
                count_result = len(results)
                count_unsuccessfully = results.count(False)
                up_or_down = check_percent(all_=count_result, any_=count_unsuccessfully)
                if not up_or_down:
                    add_log(project_id=5, server_address=target_addresses, message=f'Server {target_addresses} is down!')
                    break
                else:
                    add_log(project_id=5, server_address=target_addresses,
                            message=f'Server {target_addresses} is ok!')
                    break

            if len(results) >= 5:
                count_result = len(results)
                count_unsuccessfully = results.count(False)
                up_or_down = check_percent(all_=count_result, any_=count_unsuccessfully)
                if not up_or_down:
                    break

    except Exception as e:
        # Log an exception message if an error occurs during the main loop
        # logging.exception("An error occurred: %s", str(e))
        add_log(project_id=5, server_address=target_addresses, message=f"An error occurred: {e}")


def check_selected_function(address: str, second_interval_minutes, selected_functions):
    """
    Check the status of addresses concurrently using multi-threading.

    Parameters:
    - addresses: A IP addresses to be checked.

    Returns:
    None

    Logs:
    - If any of the addresses is down (unreachable), an error message is logged for each affected IP.
    - If all addresses are reachable, an info message is logged indicating that all servers are okay.
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

        # Retrieve ping, status, load time, and attribute information for each IP concurrently
        if "Get Ping" in selected_functions:
            ping_results = executor.submit(get_ping, address)
            ping_results = [ping_results.result()]
        else:
            ping_results = [None]

        if "Get Status" in selected_functions:
            status_results = executor.submit(get_status, address)
            status_results = [status_results.result()]
        else:
            status_results = [None]

        if "Get Load Time" in selected_functions:
            load_results = executor.submit(get_load_time, address)
            load_results = [load_results.result()]
        else:
            load_results = [None]

        if "All" in selected_functions:
            ping_results = list(executor.map(get_ping, [address]))
            status_results = list(executor.map(get_status, [address]))
            load_results = list(executor.map(get_load_time, [address]))

        # Identify IP addresses where ping, status, and load time are all 0
        final_result = [i for i, (ping, status, load) in
                        enumerate(zip(ping_results, status_results, load_results)) if
                        ping == status == load == False]

        if final_result:
            # Log an error message for each IP address that is down
            ips_is_down = []
            for ip in final_result:
                # logging.error(f'Server with IP {ip} is down.')
                add_log(project_id=5, server_address=address, message=f'Server with IP {ip} is down.')
                ips_is_down.append(ip)

            second_check_ping(ips_is_down, second_interval_minutes)

        return True


def second_check_ping(ips_is_down, second_interval_minutes):
        server_down = True
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            while server_down:
                time.sleep(second_interval_minutes * 60)
                ping_results = list(executor.map(get_ping, ips_is_down))
                if 0 not in ping_results:
                    server_down = False
                if ping_results.count(0) == len(ping_results):
                    continue
                else:
                    server_index = ping_results.index(1)
                    live_server = ips_is_down.pop(server_index)
                    # logging.info(f'Servers {live_server} is okay.')
                    add_log(project_id=5, server_address=live_server, message=f'Servers {live_server} is okay.')
            # Log an info message indicating that all servers are okay
            # logging.info(f'All servers are okay.')
            add_log(project_id=5, server_address=', '.join(ips_is_down), message='All servers are okay.')


def check_percent(all_, any_):
    """

    Args:
        all_: Count all requests
        any_: Count unsuccessfully request

    Returns: Returns False if more than 80% failed

    """
    percent = (any_ * 100) // all_

    print(f'{percent}% Unsuccessfully')

    if percent > 80:
        return False
    else:
        return True
