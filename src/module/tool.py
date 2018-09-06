import random
import string
from datetime import datetime

BLANK = ""
SPACE = " "


class Common:

    @staticmethod
    def random_string(length: int, word_number: int):
        words = ""
        for index in range(word_number):
            temp = BLANK.join(random.sample(string.ascii_letters, k=length))
            words += temp + SPACE
        return words

    @staticmethod
    def get_time_stamp():
        return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


if __name__ == "__main__":
    print(Common.random_string(5,5))