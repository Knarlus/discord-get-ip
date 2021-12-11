import KnarlusLogConsole as KnLog


def get_token(file_path: str = "TOKEN.txt") -> str:
    """
    get_token returns the first line from the file at the given path.

    :param file_path: path to token file
    :return: token as string
    """
    try:
        with open(file=file_path, mode="r") as token_file:
            token = token_file.readline()
        return token
    except FileNotFoundError as error:
        KnLog.log_to_console(log_msg=f"The file '{file_path}' was not found. Please set up the token file!",
                             log_function_name="get_token", log_type="err")
        exit(1)


if __name__ == "__main__":
    print(get_token("tok"))
