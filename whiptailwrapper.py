import subprocess
from typing import Union


def msgbox(text: str, height: int = 0, width: int = 0) -> None:
    subprocess.run(
        ["whiptail", "--msgbox", text, str(height), str(width)])
    return


if __name__ == "__main__":
    msgbox("This is msgbox test")
