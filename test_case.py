from module import Membership

#Test Case 1
cahya = Membership()
cahya.show_benefit()

#Test Case 2
shandy = Membership()
shandy.show_requirement()

#Test Case 3
cahya.predict_membership(7_000_000,9_000_000, prnt_result= True)

#Test Case 4
list_belanja = [200_000, 300_000, 120_000]
ana = Membership()
ana.calculate_price('Gold',list_belanja, prnt_result= True)




