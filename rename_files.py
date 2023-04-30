# def print_hi(name):
#     print(f"Hi {name}")
import os


def rename_file(root, name):
    # print(root)
    # print(name)
    valid_name = get_valid_name(name)
    old_name = os.path.join(root, name)
    new_name = os.path.join(root, valid_name)
    os.rename(old_name, new_name)


def get_valid_name(name):
    name = name.split("-")
    name = f"{name[2][:2]}_{name[1]}_{name[0]}_{name[2][2:]}{name[3]}{name[4][:2]}_photo.JPG"
    return name


def rename_files(name_file):
    for root, dirs, files in os.walk(name_file):
        for name in files:
            rename_file(root, name)


DIRECTORY = r"C:\TEMP"

if __name__ == "__main__":
    rename_files(DIRECTORY)
