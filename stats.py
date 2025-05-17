def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    words = text.split()
    words_count = len(words)
    return words_count

def get_num_chars(text):
    contents_lower = str.lower(text)
    char_count = {}
    for char in contents_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# In stats.py
def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(chars_dict):
    # Create a list of dictionaries from the chars_dict
    chars_list = []
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "num": count})
    
    # Sort the list using the sort_on function
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
