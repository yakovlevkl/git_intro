import os

from dotenv import load_dotenv


def it():
    for i in (1, 2, 3, 4, 5):
        print(i)


if __name__ == "__main__":
    it()
    load_dotenv('var.env')
    key1 = os.environ.get('key1')
    print(f"{key1=}")