import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            print(new_name)

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""

    # TODO: step-by-step, consider the problem cases and solve them
    #  Make all [0] capitals
    filename = filename.split("_")
    new_word = []
    for i, word in enumerate(filename):
        new_word.append(filename[i][0].capitalize())
        new_word.append(filename[i][1:])
    for i in range(len(filename)-1):
        filename = ["".join(new_word)]

    print(filename[0])

    #  Add's Spaces after capital letter
    filename = list(filename[0])
    for index, charter in enumerate(filename):
        if charter.isupper():
            if filename[index-1] != "_" and index > 0:
                print(filename[index-1])
                if filename[index-1] == "(":
                    filename.insert(index, "_")
                else:
                    filename.insert(index, "_")

    print("".join(filename))
    return new_name


main()