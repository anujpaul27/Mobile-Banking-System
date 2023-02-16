class mobile_banking_management:
    
    def __init__ (self,castomer_name, balance, won_number,password, nid,bathday):
        self.castomer_name = castomer_name
        self.balance = balance
        self.won_number = won_number
        self.password = password
        self.nid = nid
        self.bathday = bathday


    def SendMoney (self,number,amount,pin):
        if pin == self.password:
            if amount > self.balance:
                return print('Failed!.. Your Balance is low')
            elif amount < 50:
                return print('Failed!.. Please Send Minimum 50 Taka ')
            elif amount > 2500:
                return print('Failed!.. Please Send Maximum 25000 Taka')
            else:
                self.balance = self.balance-amount
                return print(f'Successful Send Money:{amount} taka From:{self.won_number} to {number}. Balance TK:{self.balance}')
        else:
            return print('Failed Send Money!. Don`t Match Pin Code. Try Again')

    def MobileRecharg (self,num,amo,pin):
            if pin == self.password:
                if amo > self.balance:
                    return print('Failed!.. Your Balance is low')
                elif amo < 20:
                    return print('Failed!. Please Send Minimum 50 Taka ')
                elif amo > 500:
                    return print('Failed!.. Please Send Maximum 25000 Taka')
                else:
                    self.balance = self.balance-amo
                    return print(f'Successful Mobile Recharg:{amo} taka From:{self.won_number} to: {num}. Balance TK:{self.balance}')
            else:
                return print('Failed Mobile Recharg!. Don`t Match Pin Code. Try Again')

    def CashOut (self,castomer_number,enter_amount,pin):
            if pin == self.password:
                if enter_amount > self.balance:
                    return print('Failed!.. Your Balance is low')
                elif enter_amount < 50:
                    return print('Failed!. Please Send Minimum 50 Taka ')
                elif enter_amount > 25000:
                    return print('Failed!.. Please Send Maximum 25000 Taka')
                else:
                    self.balance = self.balance-enter_amount
                    return print(f'Successful Cash Out:{enter_amount} taka From:{self.won_number} to {castomer_number}. Balance TK:{self.balance}')
            else:
                return print('Failed Cash Out!. Don`t Match Pin Code. Try Again')


while True:
    print()
    import time 
    print('Welcome to brack bank')
    time.sleep(2)
    print('if you create bkash mobile banking accunt: Press 1')
    f = int (input('Enter: '))
    if f==1:
        name = str(input('Your Name: '))
        check = True
        while check == True:
            number= str (input('Enter Your Number: '))
            if len(number)==11:
                check =False
            else:
                print('Invalid, Again Enter Your Number: ')
        Check = True
        while Check== True:
            nid = str (input('Enter NID: '))
            if len(nid) == 5:
                Check =False 
            else :
                print('Invalid, Again Enter Your NID: ')

        check2 = True
        while check2== True:
            bathday = str (input('Enter Date of Bath: '))
            if len(bathday) == 10 and bathday[2] == ':' and bathday[5]==":":
                check2=False
            else:
                print('wrong, Try Again: ')
        
        pas = int (input('Enter 5 Number Of Code: '))
        check3 = True
        while check3 == True:
            pas1 = int (input('Confirm Pin Code: '))
            if pas == pas1:
                check3= False
            else:
                print('Wrong: Try Again: ')
        print()
        print('Welcome to bkash account ')
        print('It is best mobile banking & Secure aaccount in bangladesh')
        print()
        my_bkash = mobile_banking_management(name, 500, number, pas, nid,bathday)
        print('1. Send Money')
        print('2. Mobile Recharge')
        print('3. Cash Out')
        UseOfNum= int (input('Enter: '))
        if UseOfNum == 1:
            number = str (input('Enter Bkash Number: '))
            amount = int (input('Enter Amount: '))
            Pin = int (input('Enter Your Pin: '))
            my_bkash.SendMoney(number, amount, Pin)

        if UseOfNum == 2:
            number = str (input('Enter mobile Number: '))
            amount = int (input('Enter Amount: '))
            Pin = int (input('Enter Your Pin: '))
            my_bkash.MobileRecharg(number, amount, Pin)

        if UseOfNum == 3:
            number = str (input('Enter Bkash Number: '))
            amount = int (input('Enter Amount: '))
            Pin = int (input('Enter Your Pin: '))
            my_bkash.CashOut(number, amount, Pin) 
    else:
        print('Close this program')           