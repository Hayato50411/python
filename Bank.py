from BankServer import BankServer
class Bank:
    def __init__(self, server: BankServer):
        self.server = server
        self.bankno = ""
        self.bank_data = {} # {name: "xxx",password: "yyy",balance: z}

    def auth_bank(self, password: str):
        if self.bankno in self.server.bank_dict:
            if self.server.bank_dict[self.bankno]["password"] == password:
                self.bank_data = self.server.getdata(self.bankno)
                name = self.bank_data["name"]
                print(f"認証成功\nいらっしゃいませ {name}様")
                return 1
            else :
                print("パスワードが違います")    
                return 0
        else :
            print("存在しない口座番号")
            return 0  

    def inBalance(self):
        print("いくら入金しますか？")
        num = int(input())
        self.bank_data["balance"] += num

    def outBalance(self):
        print("いくら出金しますか？")
        num = int(input())
        if self.bank_data["balance"] > num:
            self.bank_data["balance"] -= num
        else :
            print("残高が足りません")

    def getBalance(self):
        return self.bank_data["balance"]
    
    def setBankno(self, bankno):
        self.bankno = bankno
    
        