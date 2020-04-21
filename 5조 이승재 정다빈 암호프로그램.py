alphatonum = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
numtoalpha = {"0":"A" ,"1":"B", "2":"C", "3":"D", "4":"E", "5":"F", "6":"G", "7":"H", "8":"I", "9":"J", "10":"K", "11":"L", "12":"M", "13":"N", "14":"O", "15":"P", "16":"Q", "17":"R", "18":"S", "19":"T", "20":"U", "21":"V", "22":"W", "23":"X", "24":"Y", "25":"Z"}
print("암호화 프로그램!!")

while True:
    print("암호화를 희망하신다면 1을")
    print("암호해독을 희망하신다 2를")
    print("종료를 희망하신다면 3을 입력해주세요.")
    key = input()                                   # key 변수로 mode를 구성, 1은 암호화, 2는 
    if key != '1' and key != '2' and key != '3':    # input의 최적화를 위한 코드
        print("다시 입력해 주시길 바랍니다.")
        continue
    key = int(key)
    
    if key == 3:
        print("프로그램을 종료합니다.")
        break
    
    elif key == 1:
        while True:
            print("암호화 모듈입니다.")
            print("첫 번째 암호키를 입력해주세요:")
            a = input()
            wrong = 0
            if a == "":
                wrong = 1
            for temp in a:
                if temp != "0" and temp != "1" and temp != "2" and temp != "3" and temp != "4" and temp != "5" and temp != "6" and temp != "7" and temp != "8" and temp != "9": # input의 최적화를 위한 코드
                    wrong = 1
                    break
            if wrong == 1:
                print("잘못 입력하셨습니다.")
                continue
            a = int(a)
            #(a,26)=1을 만족할 수 있는 수가 들어갈 수 있음. φ(26) = 12가지. s.t. 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.
            #하지만 보안프로그램이기 때문에 사용자에게 들어갈 수 있는 수를 알려주지 않음.
            print("두 번째 암호키를 입력해주세요:")
            b = input()
            wrong = 0
            if b == "":
                wrong = 1
            for temp in b:
                if temp != "0" and temp != "1" and temp != "2" and temp != "3" and temp != "4" and temp != "5" and temp != "6" and temp != "7" and temp != "8" and temp != "9": # input의 최적화를 위한 코드
                    wrong = 1
                    break
            if wrong == 1:
                print("잘못 입력하셨습니다.")
                continue
            b = int(b)
            #b에는 0부터 25까지 26가지가 들어갈 수 있음. 이 역시 사용자에게 제공하지 않음.

            while True:
                print("암호화 하고 싶은 문자를 영문으로 적어주세요:")
                arr = input()
                arr = arr.upper()
                if arr == "":
                    print("문자를 입력해주시길 바랍니다.")
                    continue
                break
            ans = "암호화된 코드는 : "
            if (a == 1 or a == 3 or a == 5 or a == 7 or a == 9 or a == 11 or a == 15 or a == 17 or a == 19 or a == 21 or a == 23 or a == 25) and (b <= 25 and b >= 0):
                print("허가된 사용자 입니다.")
                for temp in arr:
                    if ord(temp) >= 65 and ord(temp) <= 90:
                        temp = alphatonum[temp]
                        num = str((temp * a + b) % 26)
                        ans = ans + numtoalpha[num]
                    else :
                        ans = ans + temp
                ans = ans + " 입니다."
                print(ans)
            else:
                print("허가되지 않은 사용자로 보입니다.")
            break
    
    elif key == 2:
        while True:
            print("암호 해독 모듈입니다.")
            print("첫 번째 암호키를 입력해주세요:")

            a = input()
            wrong = 0
            if a == "":
                wrong = 1
            for temp in a:
                if temp != "0" and temp != "1" and temp != "2" and temp != "3" and temp != "4" and temp != "5" and temp != "6" and temp != "7" and temp != "8" and temp != "9": # input의 최적화를 위한 코드
                    wrong = 1
                    break
            if wrong == 1:
                print("잘못 입력하셨습니다.")            
                continue
            a = int(a)
            #(a,26)=1을 만족할 수 있는 수가 들어갈 수 있음. φ(26) = 12가지. s.t. 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.
            #하지만 보안프로그램이기 때문에 사용자에게 들어갈 수 있는 수를 알려주지 않음.
            print("두 번째 암호키를 입력해주세요:")
            b = input()
            wrong = 0
            if b == "":
                wrong = 1
            for temp in b:
                if temp != "0" and temp != "1" and temp != "2" and temp != "3" and temp != "4" and temp != "5" and temp != "6" and temp != "7" and temp != "8" and temp != "9": # input의 최적화를 위한 코드
                    wrong = 1
                    break
            if wrong == 1:
                print("잘못 입력하셨습니다.")
                continue
            b = int(b)
            #b에는 0부터 25까지 26가지가 들어갈 수 있음. 이 역시 사용자에게 제공하지 않음.

            while True:
                print("암호를 해독하고 싶은 문자를 영문으로 적어주세요:")
                arr = input()
                arr = arr.upper()
                if arr == "":
                    print("문자를 입력해주시길 바랍니다.")
                    continue
                break
            ans = "원래 코드는 : "
            if (a == 1 or a == 3 or a == 5 or a == 7 or a == 9 or a == 11 or a == 15 or a == 17 or a == 19 or a == 21 or a == 23 or a == 25) and (b <= 25 and b >= 0):
                print("허가된 사용자 입니다.")
                for temp in arr:
                    if ord(temp) >= 65 and ord(temp) <= 90:
                        temp = alphatonum[temp]
                        num = str(((pow(a,11)) * (temp - b)) % 26)
                        ans = ans + numtoalpha[num]
                    else :
                        ans = ans + temp
                ans = ans + " 입니다."
                print(ans)
            else:
                print("허가되지 않은 사용자로 보입니다.")
            break
    else:
        print("잘못입력하셨습니다.")
        continue
