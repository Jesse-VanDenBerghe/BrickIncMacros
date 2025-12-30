INDENTATION = "| "


def log(indent, message):
    indentations = ""

    for i in range(indent):
        indentations = indentations + INDENTATION

    print(indentations + message)


def logh1(message: str):
    print("+=== " + message.capitalize() + " ===")


def logh2(message: str):
    print("|--- " + message.lower() + " ----")
