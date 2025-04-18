from stats import get_word_count, get_char_count, sorted_dicts
import sys


def get_path():
    try:
       return sys.argv[1]
    except Exception as e:
       
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)




def get_book_text(book):
    """
    This function takes a book object and returns the contents of the file as a string.
    """
    with open(book) as f:
        file_contents = f.read()
    return file_contents




def main():
    path = get_path()
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
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

