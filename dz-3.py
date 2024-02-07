# TODO

import sys, collections, re
from datetime import datetime


def read_error(func) :
    def inner(*args, **kwargs) :
        
        try:
            return func(*args, **kwargs)
        
        except FileNotFoundError as e:
            print(f"File not found. Please enter path to log-file. Error: {e}")
            
        except ValueError as e:
            return "The log entry is damaged."
            
    return inner

@read_error
def parse_log_line(line: str) -> dict :
    pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (DEBUG|ERROR|INFO) .+")
    if pattern.match(line):
        info = line.split()
        date, time, log, *msg = info
        entry = {'date': date, 'time': time, 'level': log, 'message': ' '.join(msg)}
    else:
        raise ValueError


@read_error
def load_logs(file_path: str) -> list :
    
    result = []
    with open(file_path, 'r', encoding='UTF-8') as file:
        
        while True:
            line = file.readline()
            if not line:
                break
            
            result.append(parse_log_line(line))
            
    return result

def filter_logs_by_level(logs: list, level: str) -> list :
    
    filtered_logs = []
    
    for log in logs:
        if log['level'] == level:
            filtered_logs.append(log)
            
    return filtered_logs


def count_logs_by_level(logs: list) -> dict :
    
    counter_dict = {}
    
    for log in logs:
        level = log['level']
        if not(level in counter_dict):
            counter_dict[level] = 1
        else:
            counter_dict[level] += 1
            
    return counter_dict


def display_log_counts(counts: dict) :
    result = ""
    string = "Рівень логування"
    print(f"{string.ljust(18)}| Кількість")
    print('-' * 29)
    for key, value in counts.items():
        result += f"{key.ljust(18)}| {value}\n"
    return result

msg = "2024-01-22 11:30:15 "

logs = load_logs("dz-3.log")

for log in logs:
    print(log)
