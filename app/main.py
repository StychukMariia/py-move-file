import os


def move_file(command: str) -> None:
    _, file_in, path = command.split()
    if _ != "mv":
        return
    if path.find("/") == -1:
        os.rename(file_in, path)
        return
    file_out = path.split("/")[-1]
    if path[-1] == "/":
        return
    directory = "/".join(path.split("/")[:-1])
    os.makedirs(directory, exist_ok=True)
    os.rename(f"{file_in}", f"{directory}/{file_out}")
