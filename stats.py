def count_words(text):
    text_list = text.split()
    return len(text_list)

def count_characters(text):
    dict_characters = {}
    for character in text:
        lower_char = character.lower()
        if lower_char not in dict_characters:
            dict_characters[lower_char] = 1
        else:
            dict_characters[lower_char] += 1
    return dict_characters

def sort_on(dict):
    return dict["count"]

def sorted_dictonaries(dict_of_characters):
    list1 = []
    for key, value in dict_of_characters.items():
        if key.isalpha():
            nested_dict = {"char" : key, "count" : value}
            list1.append(nested_dict)

    list1.sort(reverse=True, key=sort_on)
    return list1
