from collections import OrderedDict
from GUI.result import ResultGUI

class encoding:
    def __init__(self, key, str):
        self.oddFlag = False
        self.zCheck = ""
        self.blankCheck = ""
        self.array = [['*' for col in range(5)] for row in range(5)]
        # key = input("key 값 입력 : ")  # key
        self.setBoard(key)  # 보드 세팅
        # str = input("암호문 입력 : ")  # encoded str
        str = str.lower()
        # 공백 제거
        plain_str = ""
        for s in str:
            if s == " ":
                self.blankCheck += '10'
                continue
            if s == 'z':
                plain_str += 'q'
                self.zCheck += '1'
            else:
                plain_str += s
                self.zCheck += '0'
        encryption, playFair = self.strEncryption(key, plain_str)
        decryption = self.strDecryption(key, encryption, self.zCheck)


        self.rt(encryption, playFair)

    # 암호판 세팅
    def setBoard(self, key):
        # 중복 제거
        deduplicated_key = ''.join(OrderedDict.fromkeys(key))
        board_str = deduplicated_key+"abcdefghijklmnopqrstuvwxyz"
        board_str = ''.join(OrderedDict.fromkeys(board_str))
        print(board_str)

        # 배열에 대입
        a = 0
        for i in range(len(self.array)):
            for j in range(len(self.array)):
                self.array[i][j] = board_str[a]
                a += 1
                print(self.array[i][j], end=" ")
            print()

    # 암호화
    def strEncryption(self, key, str):
        playFair = list()
        encPlayFair = list()
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        encStr = ""

        # 2개씩 쪼개기
        i = 0
        while i < len(str):
            tmpArr = ['' for i in range(2)]
            tmpArr[0] = str[i]
            try:
                if str[i] == str[i+1]:  # 글이 반복되면 x추가
                    tmpArr[1] = 'x'
                    i -= 1
                else:
                    tmpArr[1] = str[i+1]
            except IndexError:
                tmpArr[1] = 'x'
                self.oddFlag = True
            playFair.append(tmpArr)
            i += 2
        for i in range(len(playFair)):
            print(playFair[i][0]+""+playFair[i][1], end=" ")
        print()


        for i in range(len(playFair)):
            tmpArr = ['' for i in range(2)]
            for j in range(len(self.array)):    # 쌍자암호의 각각 위치 체크
                for k in range(len(self.array)):
                    if self.array[j][k] == playFair[i][0]:
                        x1 = j
                        y1 = k
                    if self.array[j][k] == playFair[i][1]:
                        x2 = j
                        y2 = k
            if x1 == x2:    # 행이 같은 경우
                tmpArr[0] = self.array[x1][(y1+1)%5]
                tmpArr[1] = self.array[x2][(y2+1)%5]
            elif y1 == y2:  # 열이 같은 경우
                tmpArr[0] = self.array[(x1+1)%5][y1]
                tmpArr[1] = self.array[(x2+1)%5][y2]
            else:   # 행, 열 모두 다른 경우
                tmpArr[0] = self.array[x2][y1]
                tmpArr[1] = self.array[x1][y2]
            encPlayFair.append(tmpArr)

        for i in range(len(encPlayFair)):
            encStr += encPlayFair[i][0]+""+encPlayFair[i][1]+" "
        print(encStr)

        return encStr, playFair

    # 복호화
    def strDecryption(self, key, str, zCheck):
        playFair = list()
        decPlayFair = list()
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0
        decStr = ""
        lengthOddFlag = 1

        for i in range(len(str), 2):
            tmpArr = ['' for i in range(2)]
            tmpArr[0] = str[i]
            tmpArr[1] = str[i+1]
            playFair.append(tmpArr)

        for i in range(len(playFair)):
            tmpArr = ['' for i in range(2)]
            for j in range(len(self.array)):
                for k in range(len(self.array[j])):
                    if(self.array[j][k] == playFair[i][0]):
                        x1 = j
                        y1 = k
                    elif(self.array[j][k] == playFair[i][1]):
                        x2 = j
                        y2 = k

            if x1 == x2:
                tmpArr[0] = self.array[x1][(y1+4)%5]
                tmpArr[1] = self.array[x2][(y2+4)%5]
            elif y1 == y2:
                tmpArr[0] = self.array[(x1+4)%5][y1]
                tmpArr[1] = self.array[(x2+4)%5][y2]
            else:
                tmpArr[0] = self.array[x2][y1]
                tmpArr[1] = self.array[x1][y2]

            decPlayFair.append(tmpArr)

        for i in range(len(decPlayFair)):
            if i != len(decPlayFair)-1 and decPlayFair[i][1]=='x' and decPlayFair[i][0]==decPlayFair[i+1][0]:
                decStr += decPlayFair[i][0]
            else:
                decStr += decPlayFair[i][0]+""+decPlayFair[i][1]

        # z위치 찾아서 q로 돌려놓음
        for i in range(len(zCheck)):
            if zCheck[i] == '1':
                decStr = decStr.replace(i, 'q')

        print(decStr)
        # 띄어쓰기

    def rt(self, enc, playFair):
        ResultGUI(enc, playFair)


if __name__ == '__main__':
    encoding = encoding()
