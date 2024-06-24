class Notepad:
    def __init__(self):
        self.memo_list = []

    def memo(self): # 메모(텍스트)를 리스트로 출력하는 기능
        memo = input("메모입력")
        self.memo_list.append(memo)

    def memo_print(self): # 모든 메모를 콘솔로 출력하는 기능
        for memo in self.memo_list:
            print(memo)

    def memo_save(self, filename): # 메모를 파일에 저장하는 기능
        with open(filename, 'w') as file:
            for memo in self.memo_list:
                file.write(memo + '\n')
                self.memo_save("memo.txt")

    def memo_load(self,filename): # 파일로부터 메모를 붙러오는 기능
        with open(filename, 'r') as file:
            print(file.read())