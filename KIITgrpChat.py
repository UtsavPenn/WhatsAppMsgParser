import os
import re
import operator
import matplotlib.pyplot as plt
	
filename = 'KIITgrpChat.txt'
#filename = 'KIITgrpChat.txt'
#print "**************** 2014 Q4 Leader Board (September 30-December 31st)******************"

word_list=re.split('\s+',file(filename).read().lower())

utsav = word_list.count('utsav:')
rachit = word_list.count('rachit:')
harsh = word_list.count('harsh:')
rudra = word_list.count('florida:')
#def process(l):
	
#with open(filename, 'r') as f:
#    lines = f.readlines()

#for line in lines:
#	process(line)	


friends = {'Utsav':utsav, 'Rachit':rachit, 'Harsh':harsh,'Rudra':rudra} 

print"*************Leaderboard*******"
print "Utsav: %d"%utsav
print "Rachit: %d"%rachit
print "Harsh: %d"%harsh
print "Rudra: %d"%rudra 
plt.bar(range(len(friends)), friends.values(), align='center')
plt.xticks(range(len(friends)), friends.keys())

plt.show()