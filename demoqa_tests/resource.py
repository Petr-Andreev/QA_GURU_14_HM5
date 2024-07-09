from pathlib import Path
import tests

file_name = 'foto.png'

def path(file_name):
    return str(
        Path(tests.__file__).parent.joinpath(f"resources/{file_name}").absolute()
    )
