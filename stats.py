def get_word_count(file_contents):
    split = file_contents.split()
    count = len(split)
    print(f"Found {count} total words")


def get_char_count(file_contents):
    lower = file_contents.lower()
    split_word = lower.split()
    dict = {}
    for word in split_word:
        for char in word:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    return dict 

