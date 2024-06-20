def main():
    book_path = "books/frankenstein.txt"
    text = read_file_contents(book_path)
    words = count_words(text)
    char_dict_count = count_characters(text)
    sort_dict = convert_dict_to_list_of_dicts(char_dict_count)
    report_card(words, sort_dict, book_path)

def read_file_contents(path):
    with open(path) as f:
        return f.read()
    
def count_words(split_into_words):
    words = split_into_words.split()
    return words

def count_characters(dict_count):
    lowered_string = dict_count.lower()
    dictionary = {}

    for char in lowered_string:
        if char not in dictionary:
            dictionary[char] = 1
        elif char in dictionary:
            dictionary[char] += 1
    return dictionary

def convert_dict_to_list_of_dicts(dict):
    list = []

    for k, v in dict.items():
        list.append({"character": k, "count": v})
    
    list.sort(reverse=True, key=sort_on)
    return list

def sort_on(list):
    return list["count"]

def report_card(amount_words, sorted_dict, path):
    print(f"--- Begin report of {path} ---")
    print(f"--- {len(amount_words)} words found in the document ---")
    print()

    for item in sorted_dict:
        if not item["character"].isalpha():
            continue
        print(f"The {item['character']} character was found {item['count']} times")

    print()
    print("--- End of Report ---")

main()