def read(file_name):
    with open(file_name, "r+") as file:
        text = file.readline().replace("\n", "")
        pattern = file.readline().replace("\n", "")

    return text, pattern
