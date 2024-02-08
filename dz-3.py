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
            return "Damaged entries."
            
    return inner

@read_error
def parse_log_line(line: str) -> dict:
    # Правильна запис логу
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

def count_logs_by_level(logs: list) -> dict:
    log_by_level = {}

    for log in logs:
        
        if log['level'] in log_by_level:
            log_by_level[log['level']] += 1
        else:
            log_by_level[log['level']] = 1
            
    return log_by_level

def display_log_counts(counts: dict):
    
    level_title = "Рівень логування |"
    count_title = 'Кількість'
    result = ""
    # Чорна магія з виводом таблички =)
    print(f"{level_title} {count_title}")
    print("-" * (len(level_title) - 2), "|", "-" * len(count_title))
    # Вивід рівнів логу
    for level, count in counts.items():
        result += f"{level.ljust((len(level_title) - 1))}| {count}\n"
        
    return result

@read_error
def print_details_log(log_file, level):
    result = f"Деталі логів для рівня '{level.upper()}':\n"
    for log in log_file:
        result += f"{log['date']} {log['time']} - {log['msg']}\n"
        
    return result


if __name__ == '__main__':
    
    arguments = len(sys.argv)
    
    if arguments >= 2:
        
        log_file = load_logs(str(sys.argv[1]))
        result = display_log_counts(count_logs_by_level(log_file))
        
        match arguments:
            
            case 2:
                print(result)
                
            case 3:
                print(result)
                entry_detal = filter_logs_by_level(log_file, sys.argv[2].upper())
                print(print_details_log(entry_detal, sys.argv[2]))
    else:
        print("|You must provide argument-path.| Path to log-file. |")

