from enum import Enum


class WM():
    AVG_CURRENT_TIME_REPORT = 60 / 3600
    AVG_CURRENT_CONSUMPTION_REPORT = 83.7
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.0073
    AVG_CURRENT_CONSUMPTION_WORK = 1.14


class TB():
    AVG_CURRENT_TIME_REPORT = 180 / 3600
    AVG_CURRENT_CONSUMPTION_REPORT = 20.9  # mA wake up, log into the network and report, measured!
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.332  # mA sleep consumption (not available), measured!
    AVG_CURRENT_CONSUMPTION_WORK = 8.52  # mA including GSM, measured!


class TC():
    AVG_CURRENT_TIME_REPORT = 22 / 3600
    AVG_CURRENT_CONSUMPTION_REPORT = 81.5  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.177  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 7.33  # мА


class T5():
    AVG_CURRENT_TIME_REPORT = 60 / 3600
    AVG_CURRENT_CONSUMPTION_REPORT = 51.8  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.185  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 142  # mA with GSM


class TR():
    # LoRa
    AVG_CURRENT_TIME_REPORT = 60 / 3600
    AVG_CURRENT_CONSUMPTION_REPORT = 65.5  # mA
    AVG_CURRENT_CONSUMPTION_SLEEP = 0.223  # mA
    AVG_CURRENT_CONSUMPTION_WORK = 1.89  # mA


class TD():
    # Test Device
    report_time = 0 # Default
    report_capacity = 0 # Default
