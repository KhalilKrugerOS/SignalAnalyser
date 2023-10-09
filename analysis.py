import subprocess
import re
import time
import platform


class signal_analysis:

    def read_data_from_cmd(self):
        p = subprocess.Popen("netsh wlan show network mode=bssid interface=\"wi-fi\"",
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = p.stdout.read().decode('unicode_escape')
        if platform.system() == 'Linux':
            m = re.findall(
                '(wlan[0-9]+).*?Signal level=(-[0-9]+) dBm', out, re.DOTALL)
        elif platform.system() == 'Windows':
            m = re.findall(
                'SSID.*?:.*? ([A-z0-9 ]*[-_]?[A-z0-9]*).*?Signal.*?:.*?([0-9]*)%', out, re.DOTALL)
        else:
            raise Exception('reached else of if statement')
        p.communicate()
        return m

    def wifi_signal_power_analyser(self):
       # the read_data function result in a list containing 1 tuple of 2 els
        power_max = 0
        power_min = -99
        while True:
            networks = self.read_data_from_cmd()
            if len(networks) == 0:
                raise Exception("verify your connection and try again")
            for network in networks:
                signal_name = network[0]
                signal_percent_mesured = int(network[1])
                signal_power_dbm = power_max - \
                    (1 - signal_percent_mesured/100)*(power_max - power_min)
                print(
                    f"Signal name = {signal_name} : power = {signal_power_dbm}dbm\n")
            print("update ... ")
            time.sleep(5)
