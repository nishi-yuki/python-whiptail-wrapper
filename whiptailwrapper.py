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


def inputbox(text: str, height: int = 0, width: int = 0,
             init_text: str = "", password: bool = False) -> Union[str, None]:
    mode = "--passwordbox" if password else "--inputbox"
    result = subprocess.run(
        ["whiptail", mode, text, str(height), str(width), init_text],
        stderr=subprocess.PIPE)
    if result.returncode == 0:
        return result.stderr.decode("UTF8")
    else:
        return None


def passwordbox(text: str, height: int = 0, width: int = 0,
                init_text: str = "", password: bool = False) -> Union[str, None]:
    return inputbox(text, height, width, init_text, password=True)


if __name__ == "__main__":
    msgbox("This is msgbox test")

    print("yesno: ", end="")
    if yesno("This is yesno test"):
        print("'ok' selected")
    else:
        print("'no' selected")

    print(inputbox("This is inputbox test.\nThis will echo your text."))

    print(passwordbox("This is inputbox test.\nThis will echo your text."))
