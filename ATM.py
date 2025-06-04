from Bank import Bank
from BankServer import BankServer

def main():   
    while(1):
        print("口座番号を入力してください: xxxx-xxxx") # カードリーダーで口座番号をget
        bankno = input()
        bank.setBankno(bankno)

        print("パスワードを入力してください: 4桁")
        password = input()
        if bank.auth_bank(password):
            break
        else:
            pass
        
        mode_selct()

def mode_selct():
    print("1:入金 2:出金 3:残高照会") 
    mode = input()
    if mode == "1" or mode == "入金":
        bank.inBalance()
    elif mode == "2" or mode == "出金":
        bank.outBalance()
    elif mode == "3" or mode == "残高照会":
        bank.getBalance()
    else :
        print("想定外の数値が入力された")


if __name__=="__main__":
    server = BankServer()
    bank = Bank(server)
    main()