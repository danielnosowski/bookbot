def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def wordcounter(booktxt):
    words = booktxt.split()
    length = len(words)
    return length

def main():
    path_to_file = "./books/frankenstein.txt"
    booktxt = get_book_text(path_to_file)
    word_count = wordcounter(booktxt)
    print(f"{word_count} words found in the document")

main()