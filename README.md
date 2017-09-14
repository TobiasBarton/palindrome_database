# Palindrome database
A Palindromes database with two REST endpoints, created using Python and Flask.

A restful API created using Python and Flask for palindromes.
A Palindrome is a word or phrase with reads the same backwards as forwards.
In this case the palindrome string is independent of spaces and punctuations. 
An example is "Dammit I'm Mad"

Presents two endpoints:
   - POST /palindromes
   An endpoint that accepts a string parameter, that will return true if the string is paldinrome (and false otherwise)
   - GET /palindromes
   An endpoint that returns a list of the last 10 palindromes the system has recieved in the last 10 minutes.

To use, clone code and ensure you are using Python 3 and have the Flask Python Package installed.
Then run app.py.

## Getting Started

### Prerequisities

Flask

### Installing 

Download source code
```
git clone https://github.com/TobiasBarton/palindrome_database.git
```
then run
```
python3 setup.py install
```

## Running the tests

```
python3 tests.py
```

Access the POST endpoint to see if a string is palindrome:
```
curl -X POST "http://localhost:5000/palindromes?string=word"
```
Replace word with the string to be test

To return a list of the last 10 palindromes within 10 minutes run:
```
curl "http://localhost:5000/palindromes"
```

