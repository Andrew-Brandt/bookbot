from stats import get_word_count, get_char_count

FRANK = "./books/frankenstein.txt"

def get_book_text(book):
    """
    This function takes a book object and returns the contents of the file as a string.
    """
    with open(book) as f:
        file_contents = f.read()
    return file_contents



def main():
    text = get_book_text(FRANK)
    get_word_count(text)
    get_char_count(text)


main()

