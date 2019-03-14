import subprocess
from typing import Union


def msgbox(text: str, height: int = 0, width: int = 0) -> None:
    subprocess.run(
        ["whiptail", "--msgbox", text, str(height), str(width)])
    return


def yesno(text: str, height: int = 0, width: int = 0) -> bool:
    result = subprocess.run(
        ["whiptail", "--yesno", text, str(height), str(width)])
    return not result.returncode


if __name__ == "__main__":
    msgbox("This is msgbox test")

    print("yesno: ", end="")
    if yesno("This is yesno test"):
        print("'ok' selected")
    else:
        print("'no' selected")
