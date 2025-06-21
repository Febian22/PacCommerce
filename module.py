from tabulate import tabulate

class Membership:
    def show_benefit(self):
        self.membership_benefit = [{'Membership':'Platinum','Discount': '15%', 'Another Benefit': "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"},
                              {'Membership':'Gold','Discount': '10%', 'Another Benefit': "Benefit Silver + Voucher Ojek Online"},
                              {'Membership':'Silver','Discount': '8%', 'Another Benefit': "Voucher Makanan"}]
        print(tabulate(self.membership_benefit, headers='keys', tablefmt='grid'))
    
    def show_requirement(self):
        self.membership_requirement = [{'Membership':'Platinum','Monthly Expense (Rp.)': 8000000, 'Monthly Income (Rp.)': 15000000},
                              {'Membership':'Gold','Monthly Expense (Rp.)': 6000000, 'Monthly Income (Rp.)': 10000000},
                              {'Membership':'Silver','Monthly Expense (Rp.)': 5000000, 'Monthly Income (Rp.)': 7000000}]
        
        print(tabulate(self.membership_requirement,headers='keys', tablefmt='grid', intfmt=","))
    
    def predict_membership(self,expense:int,income:int):
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
        print(f"Berdasarkan Monthly Income dan Expense anda, anda masuk pada kategori '{prediction[0]}'!")
        
    
    def calculate_price(self, membership:str, price_list):
        disc = 0
        for item in self.membership_benefit:
            if item['Membership'] == membership.capitalize():
                disc = int(item['Discount'].strip('%'))/100
                break
        
        print(f"Total belanja anda : Rp. {int(sum(price_list)*(1-disc))}")


if __name__ == '__main__':
    user1 = Membership()
    user1.show_benefit()
    user1.show_requirement()
    user1.predict_membership(3_000_000,14_000_000)
    belanja = [1_000_000, 2_000_000, 2_000_000]
    user1.calculate_price('Platinum',belanja)

