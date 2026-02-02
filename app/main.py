import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "mv":
        file_in, file_out = command_list[1], command_list[2]
        if not os.path.exists(file_out):
            with (open(file_in, "r") as file_remove,
                  open(file_out, "w") as file_move):
                file_move.write(file_remove.read())
            os.remove(file_in)
