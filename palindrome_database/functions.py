from datetime import datetime
import string



def clean_string(string_in):
    """
    Function to 'clean' string by getting rid of punctuation and white space.
    Does not remove special characters.
    :param: string_in - String to clean
    :return: The clenaed string
    """
    translator = str.maketrans('', '', string.punctuation)
    clean_str = string_in.translate(translator)
    clean_str = clean_str.replace(" ", "")
    return clean_str

def last_palindromes(palindromes, limit=10, duration=600):
    """
    A function to find the last entries of the palindromes list that have occured within a time
    period (duration)
    :param: palindromes - a list of dicts with keys time_added, palindrome_str, and id
    :param: limit - the number of last entries to retrieve
    :param: duration - the time period within the entries had to be entered 
    :return: a list of length=limit of palindromes strings which have occured within duration
    """
    count = 0
    current_time = datetime.now()
    last_palindromes_list = []
    for item in palindromes[::-1]:
        if count < limit:
            time_delta = current_time - item['time_added']
            if time_delta.seconds < duration:
                last_palindromes_list.append(item['palindrome_str'])
            count += 1
        else:
            break
    return last_palindromes_list
