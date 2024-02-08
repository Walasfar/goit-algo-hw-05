import sys
import re

def read_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except FileNotFoundError as e:
            print("Log file not found.")
        # Пошкоджена запис
        except ValueError as e:
            return {'level': 'DAMAGED','msg': e}
        
        except KeyError as e:
            return e
            
    return inner

@read_error
def parse_log_line(line: str) -> dict:
    pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (INFO|ERROR|DEBUG|WARNING) .+")
    # Якщо запис логу правильна
    if pattern.match(line):
        splited_line = line.split()
        date, time, level, *msg = splited_line
        entry = {'date': date, 'time': time, 'level': level, 'msg': ' '.join(msg)}
        return entry
    # Інакше створиться запис з повідомленням про пошкоджену запис
    else:
        raise ValueError("The log entry is damaged.")


@read_error
def load_logs(file_path: str) -> list:
    entry_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        
        while True:
            line = file.readline()
            if not line:
                break
            
            entry_list.append(parse_log_line(line))
    return entry_list

@read_error
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []
    
    for entry in logs:
        if entry['level'] == level:
            filtered_logs.append(entry)
        
    return filtered_logs


log_file = load_logs('dz-3.log')

filtered_logs = filter_logs_by_level(log_file, 'DAMAGED')

for log in filtered_logs:
    print(log)
