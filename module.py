from tabulate import tabulate

class Membership:
    membership_benefit = [{'Membership':'Platinum','Discount': '15%', 'Another Benefit': "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"},
                              {'Membership':'Gold','Discount': '10%', 'Another Benefit': "Benefit Silver + Voucher Ojek Online"},
                              {'Membership':'Silver','Discount': '8%', 'Another Benefit': "Voucher Makanan"}]
    
    membership_requirement = [{'Membership':'Platinum','Monthly Expense (Rp.)': 8000000, 'Monthly Income (Rp.)': 15000000},
                              {'Membership':'Gold','Monthly Expense (Rp.)': 6000000, 'Monthly Income (Rp.)': 10000000},
                              {'Membership':'Silver','Monthly Expense (Rp.)': 5000000, 'Monthly Income (Rp.)': 7000000}]
    
    def show_benefit(self):
        '''
        Show all membership benefit in tabulated table (grid)

        parameter:
        None

        Return:
        None
        '''
        print(tabulate(self.membership_benefit, headers='keys', tablefmt='grid'))
    
    def show_requirement(self):
        '''
        show all membership requirement in tabulated table (grid)

        Parameter:
        None

        Return:
        None
        '''
        print(tabulate(self.membership_requirement,headers='keys', tablefmt='grid', intfmt=","))
    
    def predict_membership(self,expense:int,income:int, prnt_result:bool = False):
        '''
        Predict possible membership for user based on the monthly expense and income
        using Euclidean distance

        parameter:
        - Expense : Int
        - Income : Int
        - prnt_result : bool = False | True for print result / False to not print result

        return:
        - predicted membership : Str
        '''
        if type(expense) == int and type(expense) == int:
            pass
        else:
            raise ValueError('Wrong input')
        
        min_dict = {}
        for item in self.membership_requirement:
            key_index = list(item.keys())
            rvalue = round(((expense - item[key_index[1]])**2 + (income - item[key_index[2]])**2)**0.5,2)
            min_dict[item['Membership']] = rvalue
        prediction = list(min(min_dict.items(), key= lambda x : x[1]))
        
        if prnt_result == True:
            print(f"Berdasarkan Monthly Income dan Expense anda, anda masuk pada kategori '{prediction[0]}'!")
        return prediction[0]
        
    
    def calculate_price(self, membership:str, price_list:list, prnt_result:bool = False):
        '''
        Calculate price after discount for the member

        parameter:
        - membership : str (typo result in null disc)
        - price_list : list (int)
        - prnt_result : bool = False | True for print result / False to not print result

        return:
        - Total price (Discounted) : int
        '''
        disc = 0
        for item in self.membership_benefit:
            if item['Membership'] == membership.capitalize():
                disc = int(item['Discount'].strip('%'))/100
                break
        if prnt_result == True:
            print(f"Total belanja anda : Rp. {int(sum(price_list)*(1-disc))}")
        return int(sum(price_list)*(1-disc))


