# Reference Page: https://logmi.jp/tech/articles/329470
from concurrent.futures import ProcessPoolExecutor
from random import random
from time import sleep


def func(key):
    print(key)
    sleep(random())
    print(key)


def do_parallel():
    with ProcessPoolExecutor() as executor:
        for key in [1, 2, 3]:
            executor.submit(func, key)


if __name__ == '__main__':
    do_parallel()
