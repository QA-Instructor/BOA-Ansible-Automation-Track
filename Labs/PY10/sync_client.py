#! venv/bin/python3
import requests
from time import sleep

def process_data(obj):
    outstr = ""
    for k in obj.keys():
        outstr += f"{k.upper()}: {str(obj.get(k))}\n"
    sleep(1)
    return outstr

def main():
    books = requests.get('http://localhost:5000/api/books').json()
    authors = requests.get('http://localhost:5000/api/authors').json()
    for book in books:
        print(process_data(book))
    for author in authors:
        print(process_data(author))

if __name__ == '__main__':
    main()

