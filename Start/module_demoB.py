def save2file(members, avgFee):
    with open('record.txt', 'a', encoding='utf8') as f:
        recordList = [f'{member}:{avgFee}' for member in members]
        f.write('|'.join(recordList) + '\n')
