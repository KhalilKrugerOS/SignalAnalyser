import subprocess
import re
import time
import platform
import matplotlib.pyplot as plt
import numpy as np

def read_data_from_cmd():
    p = subprocess.Popen("netsh wlan show interfaces", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = p.stdout.read().decode('unicode_escape')
    if platform.system() == 'Linux':
            m = re.findall('(wlan[0-9]+).*?Signal level=(-[0-9]+) dBm', out, re.DOTALL)
    elif platform.system() == 'Windows':
            m = re.findall('Nom.*?:.*?([A-z0-9]*-[A-z0-9 ]*).*?Signal.*?:.*?([0-9]*)%', out, re.DOTALL)
    else:
           raise Exception('reached else of if statement')
    p.communicate()
    return  m[0]


def wifi_signal_power_analyser():
       ## the read_data function result in a list containing 1 tuple of 2 els
        power_max = 0
        power_min = -99        
        while True:
            result = read_data_from_cmd()
            try:
                signal_name = result[0]
                signal_percent_mesured = int(result[1])
            except:
                  raise Exception("verify your connection and try again")
            signal_power_dbm = power_max - (1 - signal_percent_mesured/100)*(power_max - power_min)
            print(f"Signal name = {signal_name} : power = {signal_power_dbm}dbm {signal_percent_mesured}%")
            time.sleep(2)

wifi_signal_power_analyser()
