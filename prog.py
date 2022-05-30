import csv

name = 'Mini' # CHANGE THIS
data_to_retr='annee' # CHANGE THIS

file = open(name+'.csv', encoding='utf-8')
csvreader = csv.reader(file)
header=next(csvreader)

for i in range(len(header)):
	if header[i] == data_to_retr:
		target=i

whitelist = []
index=0
for line in csvreader:
	if line[target] in whitelist:
		out.write(str(line)+'\n')
		print('Writting line ...')
		print(index)
		index=index+1
	else:
		out = open(name+'_'+line[target]+".csv", 'w', encoding='utf-8')
		whitelist.append(line[target])
		out.write(str(header)+'\n')

print('Travail terminé !!!')
file.close() # CAST
out.close() # CAST
		

file.close()
