# Reference Page: https://atmarkit.itmedia.co.jp/ait/articles/2110/19/news025.html
import time
from queue import Queue
from threading import Thread


def do_in_thread(q):
    while True:
        item = q.get(block=True)
        if not item:  # 取り出した要素が偽と見なされる値（空文字列など）であれば
            break  # 無限ループを終了
        print(item)
    print('out while loop')


# 以下の書き方も考えられる
"""
def do_in_thread(q):
    item = q.get(block=True)
    while item:
        print(item)
        item = q.get(block=True)
    print('out while loop')
"""


if __name__ == '__main__':
    q = Queue()
    th = Thread(target=do_in_thread, args=[q])
    th.start()

    for item in ['foo', 'bar', 'baz', '', 'hoge']:
        time.sleep(2)
        print(f'item: {item}')
        q.put(item)
