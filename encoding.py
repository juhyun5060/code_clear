from collections import OrderedDict

class encoding:
    def __init__(self):
        self.setBoard("attitude")

    # 암호판 세팅
    def setBoard(self, key):
        # 중복 제거
        deduplicated_key = ''.join(OrderedDict.fromkeys(key))
        board_str = deduplicated_key+"abcdefghijklmnopqrstuvwxyz"
        board_str = ''.join(OrderedDict.fromkeys(board_str))
        print(board_str)

        # 배열에 대입
        array = [['*' for col in range(5)] for row in range(5)]
        a = 0
        for i in range(len(array)):
            for j in range(len(array)):
                array[i][j] = board_str[a]
                a += 1
                print(array[i][j], end=" ")
            print()




if __name__ == '__main__':
    encoding = encoding()
