#!/usr/bin/python
import calendar
import time

if __name__ == '__main__':
    s = "你好 world!!"
    num = 3
    print(s)
    print(num)

    if num == 1:
        print(1)
    elif num == 2:
        print(2)
    elif num == 3:
        print(3)
    else:
        print(4)

    flag = False
    if flag:
        print("true")
    else:
        print("false")
    #
    # count = 1
    # while count < 10:
    #     print(count)
    #     count = count + 1
    #
    # for index in s:
    #     if index == "o":
    #         continue
    #     print(index)
    structtime = time.localtime(time.time())
    asctime = time.asctime(structtime)
    print(asctime)

    print(time.strftime("%Y-%m-%d %H:%M:%S.%z"))

    count = 1
    while True:
        time.sleep(2)
        print(count)
        count = count + 2
