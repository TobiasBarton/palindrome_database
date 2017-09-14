from datetime import datetime
import string

from flask import Flask, request, jsonify

from palindrome import Palindrome
import functions as func


# Constant variables
# PALINDROME_LIST will be a list of dictionaries 
# key and values pairs as defined by palindrome.py class Palindrome
# Entries could also be stored in JSON file or noSQL db
PALINDROME_LIST = []

app = Flask(__name__)

@app.route("/palindromes", methods=["POST", "GET"])
def palindrome():
    if request.method == "POST":
        string_in = request.args.get('string')
        cleaned_str = func.clean_string(string_in)

        if cleaned_str == cleaned_str[::-1]:
            # if the string reversed is the same store and print result
            pal = Palindrome(cleaned_str)
            PALINDROME_LIST.append(pal.serialize())
            return 'true\n'

        elif cleaned_str != cleaned_str[::-1]:
            # if the string reversed is not the same just print result
            return 'false\n'

    elif request.method == "GET":
        # if call is GET return the last 10 entries within 10 mins
        return jsonify(func.last_palindromes(PALINDROME_LIST, limit=10, duration=600))


if __name__ == "__main__":
    app.run(debug=True)

