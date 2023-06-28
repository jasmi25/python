print("Welcome to ATM")
card=input("insert u r card: ")
if card == "yes" or card=="YES" :
	language= input("Enter u r language: ")
	if language== "english" or language == "ENGLISH":
		pin = int(input("Enter u r 4 dight pin: "))
		if pin>999 and pin<10000:
			print('1 - Withdraw/WITHDRAW')
			print("2 - Balance enquiry/BALANCE ENQUIRY")
			print("3 - Deposite/DEPOSITE")
			print("4 - bill pay/BILL PAY")
			t_type=int(input("Choose transactions: "))
			if t_type== 1 :
				ac_type=input("enter account type ")
				if ac_type=="saving" or ac_type=="current" or ac_type=="join account":
					wdraw_am= int(input("Enter withdraw amount: "))
					if wdraw_am>=500 and wdraw_am<=20000 and wdraw_am%500==0:
						a=wdraw_am//2000
						A=wdraw_am%2000
						b=A//500
						B=A%500
						print("notes of 2000",a,"notes of 500",b)
						rc=input("enter rc yes or not: ")
						if rc=="yes":
							print("amount rc")
							k_n=input("enter key name: ")
							if k_n=="enter" or k_n=="ENTER":
								print("thank you")
							else:
								print("invalid key name")
						else:
							print("not rc amount")
					else:
						print("invalid")
				else:
					print("account not avilable")
			elif t_type == 2 :
				ac_type=input("enter account type: ")
				if ac_type=="saving" or ac_type=="current" or ac_type=="join account":
					bal_enquiry=input("enter balance enquiry yes or not: ")
					if bal_enquiry=="yes":
						print("total amount")
						print("enquiry done")
						k_n=input("enter key name: ")
						if k_n=="enter" or k_n=="ENTER":
							print("thank you")
						else:
							print("invalid key")
					else:
						print("invalid")
				else:
					print("invalid account")
			elif t_type == 3 :
				account_num=int(input("enter account num: "))
				if account_num<=1000000000000 and account_num>=999999999999:
					depo_amount=int(input("enter deposit amount"))
					if depo_amount>=100 and depo_amount<=490000:
						print("deposite successful: ",depo_amount)
						k_n=input("enter key name: ")
						if k_n=="enter" or k_n=="ENTER":
							print("thank you")
						else:
							print("invalid key name")
					else:
						print("deposite unsuccessful")
				else:
					print("invalid account")
			elif t_type==4:
				account_num=int(input("enter account num: "))
				if account_num<=1000000000000 and account_num>=999999999999:
					bill_p=int(input("enter ur bill how much you want to pay: "))
					if bill_p>=100 and bill_p<=20000:
						print("ur bill pay successful",bill_p)
						k_n=input("enter key name: ")
						if k_n=="enter" or k_n=="Enter":
							print(" thank you: ")
						else:
							print("invalid key")
					else:
						print("ur bill pay unsuccessful: ")
				else:
					print(" account invalid ")
			else:
				print("worng choice")
		else:
			print("worng pin number")
	else:
		print("invalide language")
else:
	print("pls insert card properly")
