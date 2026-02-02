import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    _, file_in, path = command.split()
    if _ != "mv":
        return
    if path.find("/") == -1:
        os.rename(file_in, path)
        return
    if path[-1] == "/":
        os.makedirs(path, exist_ok=True)
        os.rename(f"{file_in}", f"{path}/{file_in}")
        return
    file_out = path.split("/")[-1]
    directory = "/".join(path.split("/")[:-1])
    os.makedirs(directory, exist_ok=True)
    os.rename(f"{file_in}", os.path.join(directory, file_out))
