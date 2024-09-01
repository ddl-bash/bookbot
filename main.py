def main():
    PATH = "books/frankenstein.txt"
    text = get_book_text(PATH)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    print(f"--- Begin report of {PATH} ---")
    print(f"{num_words} words found in the document\n")    
    
    sorted_dict = sort_char_count(chars_dict)
    for item in sorted_dict:
        print(f"The '{item['char']}' character was found {item['count']} times")
    
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    char_count ={}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] +=  1
    return char_count

def sort_char_count(dict):
    new_list = []
    for k, v in dict.items():
        if str.isalpha(k):
            new_list.append({"char": k, "count": v})
    return sorted(new_list, reverse=True, key=sort_count)

def sort_count(dict):
    return dict["count"]

main()