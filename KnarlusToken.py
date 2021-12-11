def get_token(relative_file_path: str = "TOKEN.txt") -> str:
    with open(file=relative_file_path, mode="r") as token_file:
        token = token_file.readline()
    return token
