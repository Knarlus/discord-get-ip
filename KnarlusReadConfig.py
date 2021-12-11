from typing import List
from KnarlusLogConsole import log_to_console


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
        log_to_console(log_msg=f"The file '{file_path}' was not found. Please set up the token file!",
                       log_function_name="get_token", log_type="err")
        log_to_console(log_msg=str(error),
                       log_function_name="get_token", log_type="err")
        exit(1)


def get_guild_ids(file_path: str = "GUILD_IDS.txt") -> List[int]:
    """
    get_guild_ids returns a list of all guild ids found in the given guild id file (standard if GUILD_IDS.txt)

    :param file_path: path to guild id file
    :return: list of int representing all known guild ids
    """
    guild_ids: List[int] = []
    try:
        with open(file=file_path, mode="r") as guild_id_file:
            for line in guild_id_file:
                if line:
                    try:
                        guild_ids.append(int(line))
                    except ValueError as error:
                        log_to_console(log_msg=f"The line '{line[:-1]}' could not be converted to int. Please check \
guild id file {file_path}!", log_function_name="get_guild_ids", log_type="war")
                        log_to_console(log_msg=str(error), log_function_name="get_guild_ids", log_type="war")
    except FileNotFoundError as error:
        log_to_console(log_msg=f"The file '{file_path}' was not found. Please set up the guild id file!",
                       log_function_name="get_guild_ids", log_type="err")
        log_to_console(log_msg=str(error),
                       log_function_name="get_guild_ids", log_type="err")
        exit(1)
    if not guild_ids:
        log_to_console(log_msg=f"The file '{file_path}' does not contain any guild ids. No guild will have slash \
support", log_function_name="get_guild_ids", log_type="war")
    return guild_ids


if __name__ == "__main__":
    print(get_token())
    print(get_guild_ids())
