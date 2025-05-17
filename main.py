import sys
if len(sys.argv)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]


#import functions from stats
import stats

book_text = stats.get_book_text(path)
words_count = stats.get_num_words(book_text)
char_dict = stats.get_num_chars(book_text)

chars_sorted_list = stats.chars_dict_to_sorted_list(char_dict)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {words_count} total words")
print("--------- Character Count -------")

for char_dict in chars_sorted_list:
    char = char_dict["char"]
    count = char_dict["num"]
    if char.isalpha():
        print(f"{char}: {count}")

print("============= END ===============")
