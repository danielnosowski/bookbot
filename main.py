def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def wordcounter(booktxt):
    words = booktxt.split()
    length = len(words)

def main():
    path_to_file = "./books/frankenstein.txt"
    booktxt = get_book_text(path_to_file)
    print(booktxt)

main()