import KnarlusLogKonsole as KnLog


def get_token(relative_file_path: str = "TOKEN.txt") -> str:
    try:
        with open(file=relative_file_path, mode="r") as token_file:
            token = token_file.readline()
        return token
    except FileNotFoundError as error:
        KnLog.log_console(log_msg=f"The file '{relative_file_path}' was not found. Please set up the token file!",
                          log_function_name="get_token", log_type="err")
        exit(1)


if __name__ == "__main__":
    print(get_token())
