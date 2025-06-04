# from collections import defaultdict
class BankServer:
    def __init__(self):
        self.bank_dict = {
            "0000-0000":{"name": "Taro","password": "0000", "balance": 0},
            "1111-1111":{"name": "Hanako","password": "1111", "balance": 50000},
            "2222-2222":{"name": "John","password": "2222", "balance": 100000}
        }

    def getdata(self, bankno: str):
        return self.bank_dict[bankno]