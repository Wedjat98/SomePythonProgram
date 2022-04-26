from module_demoB import save2file

fee = input('pls input a number:\n')
members = input('pls input names :').split()
headcount = len(members)
avgFee = int(fee)/headcount
print(f'the avg fee is {avgFee}')
save2file(members, avgFee)
