from pathlib import Path

file_name = 'foto.png'


def path(file_name):
    return str(Path(__file__).parent.joinpath(f"resources/{file_name}"))
