print("\n")
print("DEALERSHIP 'THE GALICIAN'")
print("\n")
RBM_Series_1 = input("Enter the number of 'RBM Series 1' units sold: ")
RBM_Series_2 = input("Enter the number of 'RBM Series 2' units sold: ")
RBM_Series_3 = input("Enter the number of 'RBM Series 3' units sold: ")
print("\n")
commission_result1 = (float(RBM_Series_1) * 20000) * 0.3
commission_result2 = (float(RBM_Series_2) * 35000) * 0.5
commission_result3 = (float(RBM_Series_3) * 60000) * 0.7
total_commission = commission_result1 + commission_result2 + commission_result3
print("\n")
print("Commission for 'RBM Series 1' unit sales: €" + str(commission_result1))
print("Commission for 'RBM Series 2' unit sales: €" + str(commission_result2))
print("Commission for 'RBM Series 3' unit sales: €" + str(commission_result3))
print("\nTotal Commissions for sales: €" + str(total_commission) + "\n")
