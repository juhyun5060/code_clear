from collections import OrderedDict
from GUI.result import ResultGUI

class encoding:
    def __init__(self, key, str):
        self.oddFlag = False
        self.array = [['*' for col in range(5)] for row in range(5)]
        key = key.lower()
        self.setBoard(key)  # 보드 세팅
        str = str.lower()
        # 공백 제거
        plain_str = ""
        for s in str:
            if s == " ":
                continue
            # 암호판 세팅할 때 z가 잘리므로 z를 q로 변경
            if s == 'z':
                plain_str += 'q'
            else:
                plain_str += s
        encryption, playFair = self.strEncryption(key, plain_str)

        self.rt(encryption, playFair)
        # ResultGUI(encryption, playFair)

    # 암호판 세팅
    def setBoard(self, key):
        # 중복 제거(순서를 기억하는 딕셔너리에 키 값으로 넣어줌)
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
        # 매핑한 정보
        playFair = list()
        # 암호화 된
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
                        x1 = j  # 1
                        y1 = k  # 1
                    if self.array[j][k] == playFair[i][1]:
                        x2 = j  # 1
                        y2 = k  # 3
            if x1 == x2:    # 행이 같은 경우
                tmpArr[0] = self.array[x1][(y1+1)%5]    # 오른쪽으로 이동하므로 y+1 & 다섯줄이므로 %5
                tmpArr[1] = self.array[x2][(y2+1)%5]
            elif y1 == y2:  # 열이 같은 경우
                tmpArr[0] = self.array[(x1+1)%5][y1]    # 아래쪽으로 이동하므로 x+1 & 다섯줄이므로 %5
                tmpArr[1] = self.array[(x2+1)%5][y2]
            else:   # 행, 열 모두 다른 경우
                tmpArr[0] = self.array[x2][y1]
                tmpArr[1] = self.array[x1][y2]
            encPlayFair.append(tmpArr)

        for i in range(len(encPlayFair)):
            encStr += encPlayFair[i][0]+""+encPlayFair[i][1]+" "
        print(encStr)

        return encStr, playFair

    def rt(self, enc, playFair):
        ResultGUI(enc, playFair)


if __name__ == '__main__':
    encoding = encoding()
