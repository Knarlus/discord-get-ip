from datetime import datetime
from termcolor import colored, cprint

def log_console(log_msg: str, log_function_name: str, log_type: str):
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%d.%m.%Y @ %H:%M:%S")
    if not isinstance(log_msg, str):
        log_msg = str(log_msg)
    log_type = log_type.lower()
    if log_type == "err":
        print_out = colored(str(f"[ ERROR ] {current_time} | {log_function_name} | {log_msg}"), "red")
    elif log_type == "war":
        print_out = colored(str(f"[WARNING] {current_time} | {log_function_name} | {log_msg}"),"yellow")
    elif log_type == "inf":
        print_out = colored(str(f"[ INFO  ] {current_time} | {log_function_name} | {log_msg}"), "green")
    else:
        log_error = "Function 'log_console()' was called with invalid log_type: " + str(log_type)
        log_console(log_msg=log_error, log_function_name=log_function_name, log_type="war")
        print_out = colored(str(f"[ NONE  ] {current_time} | {log_function_name} | {log_msg}"), "grey")
    cprint(print_out)

def log_file(print_out):
    "write to file"


log_console("Not available", "Discord-API", "err")