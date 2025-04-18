from stats import get_word_count, get_char_count, sorted_dicts

FRANK = "books/frankenstein.txt"

def get_book_text(book):
    """
    This function takes a book object and returns the contents of the file as a string.
    """
    with open(book) as f:
        file_contents = f.read()
    return file_contents




def main():
    text = get_book_text(FRANK)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {FRANK}...")
    print("----------- Word Count ----------")
    get_word_count(text)
    print("--------- Character Count -------")
    big_dict = get_char_count(text)
    list_of_dicts = sorted_dicts(big_dict)
    for dict in list_of_dicts:
        for char in dict:
            count = dict[char]
            print(f"{char}: {count}")
    print("============= END ===============")


main()

