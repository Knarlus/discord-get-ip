from datetime import datetime
from termcolor import colored, cprint

log_types = {"inf": ("[ Info  ]", "green"), "war": ("[Warning]", "yellow"), "err": ("[ Error ]", "red"),
             "otherwise": ("[ None  ]", "grey")}


def log_to_console(log_msg: str, log_function_name: str, log_type: str, write_to_file: bool = False):
    current_time = datetime.now().strftime("%d.%m.%Y @ %H:%M:%S")
    log_type = log_type.lower()
    if log_type in log_types.keys():
        print_type, log_color = log_types[log_type]
    else:
        print_type, log_color = log_types["otherwise"]
        log_to_console(log_msg=f"function was called with illegal parameter for 'log_type': '{log_type}'",
                       log_function_name="log_to_console", log_type="war", write_to_file=write_to_file)
    cprint(colored(f"{print_type} {current_time} | {log_function_name} | {log_msg}", log_color))
    if write_to_file:
        log_to_file(log_msg=log_msg, log_function_name=log_function_name, log_type=log_type)


def log_to_file(log_msg: str, log_function_name: str, log_type: str, log_path: str = "log.txt"):
    current_time = datetime.now().strftime("%d.%m.%Y @ %H:%M:%S")
    log_type = log_type.lower()
    print_type, _ = log_types[log_type] if log_type in log_types.keys() else log_types["otherwise"]
    with open(file=log_path, mode="a") as log_file:
        log_file.write(f"{print_type} {current_time} | {log_function_name} | {log_msg}\n")


if __name__ == "__main__":
    log_to_console("Executed as main script", "KnarlusLogConsole.py", "err", True)
