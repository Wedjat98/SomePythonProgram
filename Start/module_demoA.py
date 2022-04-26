import module_demoB as save

fee = input('pls input a number:\n')
members = input('pls input names :').split()
headcount = len(members)
avgFee = int(fee)/headcount
print(f'the avg fee is {avgFee}')

save.save2file(members, avgFee)