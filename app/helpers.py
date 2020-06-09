import json
import os


def collect_files():
    reports_location = "./reports/"
    reports = dict()
    for file_name in os.listdir(reports_location):
        with open(reports_location + file_name, "r") as file:
            reports[file_name] = json.load(file)
    return reports
