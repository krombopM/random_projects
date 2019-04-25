## French word list

#imports
import random


#Main Program

list = open('list.txt','r')

word_list = []

for line in list.readlines():
	
	word_list.append(line)

#Test for length of wordlist
assert(len(word_list)) == 100


points = 0

while True:
	q = random.choice(word_list)
	q = q.split(' ')
	print(q[-1])
	print('What does the word ', q[1], ' mean?')


	#ans = input()
	ans = str(q[-1])
	ans = str(ans)

	if ans == str(q[-1]):
		print('Correct!')
		points += 1
	else:
		print('No, the answer was: ', str(q[-1]))
		points -= 1

	print('Points: ', points)

