import subprocess
from typing import Any, Union, Tuple, Sequence


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


def menu(text: str, items: Sequence[Tuple[Any, str]],
         height: int = 0, width: int = 0,
         list_height: int = 0, ) -> int:
    flat_items = []
    for i, item in enumerate(items):
        flat_items.extend([str(i), item[1]])
    args = [
        "whiptail", "--notags", "--menu", str(text), str(height), str(width),
        str(list_height)
    ] + flat_items
    result = subprocess.run(args, stderr=subprocess.PIPE)
    output_str = result.stderr.decode("UTF8")
    try:
        idnum = int(output_str)
    except:
        raise Exception(output_str)
    return idnum


if __name__ == "__main__":
    msgbox("This is msgbox test")

    print("yesno: ", end="")
    if yesno("This is yesno test"):
        print("'ok' selected")
    else:
        print("'no' selected")

    print(inputbox("This is inputbox test.\nThis will echo your text."))

    print(passwordbox("This is inputbox test.\nThis will echo your text."))

    print(menu(
        "This is menu test.",
        [
            ("spam", "SPAM! SPAM!"),
            ("hoge", "hoge ho ge"),
            ("world", "hello world"),
        ]
    ))
