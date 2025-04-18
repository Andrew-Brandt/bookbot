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



def sorted_dicts(dict):
    """
    this function takes a dictionary and returns a sorted list of dictionaries sorted by the value of the dictionary
    """
    list_of_dicts = []
    for char in dict:
        key = char
        num = dict[char]
        list_of_dicts.append({key: num})
        list_of_dicts.sort(reverse=True, key=lambda x: list(x.values())[0])      
    return(list_of_dicts)
        

