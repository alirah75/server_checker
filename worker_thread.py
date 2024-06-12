from PyQt5.QtCore import QThread, pyqtSignal
import time
import logging
import concurrent.futures
from datetime import datetime

from core_functions import *

logging.basicConfig(filename='MyLog.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class WorkerThread(QThread):
    log_signal = pyqtSignal(str)

    def __init__(self, start_date, end_date, start_time, end_time, interval_minutes, second_interval_minutes,
                 target_address, selected_functions, parent=None):
        super().__init__(parent)
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = str(datetime.strptime(end_date, '%Y-%m-%d').date())
        self.end_time = str(datetime.strptime(end_time, '%H:%M').time())
        self.interval_minutes = interval_minutes
        self.second_interval_minutes = second_interval_minutes
        self.target_address = target_address
        self.selected_functions = selected_functions
        self._is_running = True
        self.percent = 0

    def run(self):

        try:
            results = []
            current_time = datetime.now()
            self.log_signal.emit(f'Start time for Address: {current_time} {self.target_address}\n')
            while self._is_running:
                result = self.check_selected_function(self.target_address, self.second_interval_minutes,
                                                      self.selected_functions)
                results.append(result)
                # time.sleep(self.interval_minutes * 60)
                time.sleep(self.interval_minutes)
                current_time = datetime.now()
                current_date_str = current_time.strftime('%Y-%m-%d')
                if current_date_str > self.end_date:
                    self.log_signal.emit(f'Date ended for Address: {self.target_address}\n')
                    self.stop()

                current_time_str = current_time.strftime('%H:%M')
                if current_time_str > self.end_time:
                    self.log_signal.emit(f'Time ended for Address: {self.target_address}\n')
                    count_result = len(results)
                    count_unsuccessfully = results.count(False)
                    up_or_down = self.check_percent(all_=count_result, any_=count_unsuccessfully)
                    if not up_or_down:
                        # add_log(project_id=5, server_address=self.target_address,
                        #         message=f'Server {self.target_address} is down!')
                        self.stop()
                    else:
                        # add_log(project_id=5, server_address=self.target_address,
                        #         message=f'Server {self.target_address} is ok!')
                        self.stop()

                if len(results) >= 5:
                    count_result = len(results)
                    count_unsuccessfully = results.count(False)
                    up_or_down = self.check_percent(all_=count_result, any_=count_unsuccessfully)
                    if not up_or_down:
                        self.stop()
            self.stop()
        except Exception as e:
            # add_log(project_id=5, server_address=self.target_address, message=f"An error occurred: {e}")
            self.stop()

    def check_selected_function(self, address, second_interval_minutes, selected_functions):
        if "GetPing" in selected_functions:
            ping_results = [get_ping(address)]
        else:
            ping_results = [None]

        if "GetStatus" in selected_functions:
            status_results = [get_status(address)]
        else:
            status_results = [None]

        if "GetLoadTime" in selected_functions:
            load_results = [get_load_time(address)]
        else:
            load_results = [None]

        if "All" in selected_functions:
            ping_results = [get_ping(address)]
            status_results = [get_status(address)]
            load_results = [get_load_time(address)]

        final_result = [i for i, (ping, status, load) in enumerate(zip(ping_results, status_results, load_results))
                        if ping == status == load == False]

        if final_result:
            ips_is_down = []
            for ip in final_result:
                # add_log(project_id=5, server_address=address, message=f'Server with IP {ip} is down.')
                ips_is_down.append(ip)

            self.second_check_ping(ips_is_down, second_interval_minutes)

        return True

    def second_check_ping(self, ips_is_down, second_interval_minutes):
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
                    # add_log(project_id=5, server_address=live_server, message=f'Servers {live_server} is okay.')
            # add_log(project_id=5, server_address=', '.join(ips_is_down), message='All servers are okay.')

    def check_percent(self, all_, any_):
        self.percent = (any_ * 100) // all_
        if self.percent >= 80:
            self.log_signal.emit(f'{self.percent}% Unsuccessfully')

        return self.percent <= 80

    def stop(self):
        self._is_running = False
