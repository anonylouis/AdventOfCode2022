#!/usr/bin/python3

f = open('input.txt')


L= []
for i in range(10) :
	L.append([0, 0])
#L[0] = head, L[1] = 1 etc.... L[9] is the tail

P = {(0, 0)}
for l in f :
	l = l[:-1].split()
	if l[0] == "L" :
		for c in range(int(l[1])) :
			L[0][0] -= 1
			for n in range(len(L) - 1) :
				if L[n + 1][1] < (L[n][1] - 1) :
					if L[n + 1][0] == (L[n][0] - 1) or L[n + 1][0] == (L[n][0] + 1) or L[n + 1][0] == L[n][0] :
						L[n + 1][0] = L[n][0]
					elif L[n + 1][0] < (L[n][0] - 1) :
						L[n + 1][0] += 1 
					else :
						L[n + 1][0] -= 1
					L[n + 1][1] +=1
				elif L[n + 1][0] < (L[n][0] - 1) :
					L[n + 1][0] += 1
					if L[n + 1][1] == (L[n][1] - 1) or L[n + 1][1] == (L[n][1] + 1) or L[n + 1][1] == L[n][1] :
						L[n + 1][1] = L[n][1]
					elif L[n + 1][1] < (L[n][1] - 1) :
						L[n + 1][1] += 1 
					else :
						L[n + 1][1] -= 1
				elif L[n + 1][1] > (L[n][1] + 1) :
					if L[n + 1][0] == (L[n][0] - 1) or L[n + 1][0] == (L[n][0] + 1) or L[n + 1][0] == L[n][0] :
						L[n + 1][0] = L[n][0]
					elif L[n + 1][0] < (L[n][0] - 1) :
						L[n + 1][0] += 1 
					else :
						L[n + 1][0] -= 1
					L[n + 1][1] -=1
				elif L[n + 1][0] > (L[n][0] + 1) :
					L[n + 1][0] -= 1
					if L[n + 1][1] == (L[n][1] - 1) or L[n + 1][1] == (L[n][1] + 1) or L[n + 1][1] == L[n][1] :
						L[n + 1][1] = L[n][1]
					elif L[n + 1][1] < (L[n][1] - 1) :
						L[n + 1][1] += 1 
					else :
						L[n + 1][1] -= 1
			P.add((L[-1][0], L[-1][1]))
	elif l[0] == "R" :
		for c in range(int(l[1])) :
			L[0][0] += 1
			for n in range(len(L) - 1) :
				if L[n + 1][1] < (L[n][1] - 1) :
					if L[n + 1][0] == (L[n][0] - 1) or L[n + 1][0] == (L[n][0] + 1) or L[n + 1][0] == L[n][0] :
						L[n + 1][0] = L[n][0]
					elif L[n + 1][0] < (L[n][0] - 1) :
						L[n + 1][0] += 1 
					else :
						L[n + 1][0] -= 1
					L[n + 1][1] +=1
				elif L[n + 1][0] < (L[n][0] - 1) :
					L[n + 1][0] += 1
					if L[n + 1][1] == (L[n][1] - 1) or L[n + 1][1] == (L[n][1] + 1) or L[n + 1][1] == L[n][1] :
						L[n + 1][1] = L[n][1]
					elif L[n + 1][1] < (L[n][1] - 1) :
						L[n + 1][1] += 1 
					else :
						L[n + 1][1] -= 1
				elif L[n + 1][1] > (L[n][1] + 1) :
					if L[n + 1][0] == (L[n][0] - 1) or L[n + 1][0] == (L[n][0] + 1) or L[n + 1][0] == L[n][0] :
						L[n + 1][0] = L[n][0]
					elif L[n + 1][0] < (L[n][0] - 1) :
						L[n + 1][0] += 1 
					else :
						L[n + 1][0] -= 1
					L[n + 1][1] -=1
				elif L[n + 1][0] > (L[n][0] + 1) :
					L[n + 1][0] -= 1
					if L[n + 1][1] == (L[n][1] - 1) or L[n + 1][1] == (L[n][1] + 1) or L[n + 1][1] == L[n][1] :
						L[n + 1][1] = L[n][1]
					elif L[n + 1][1] < (L[n][1] - 1) :
						L[n + 1][1] += 1 
					else :
						L[n + 1][1] -= 1
			P.add((L[-1][0], L[-1][1]))
	elif l[0] == "D" :
		for c in range(int(l[1])) :
			L[0][1] -= 1
			for n in range(len(L) - 1) :
				if L[n + 1][1] < (L[n][1] - 1) :
					if L[n + 1][0] == (L[n][0] - 1) or L[n + 1][0] == (L[n][0] + 1) or L[n + 1][0] == L[n][0] :
						L[n + 1][0] = L[n][0]
					elif L[n + 1][0] < (L[n][0] - 1) :
						L[n + 1][0] += 1 
					else :
						L[n + 1][0] -= 1
					L[n + 1][1] +=1
				elif L[n + 1][0] < (L[n][0] - 1) :
					L[n + 1][0] += 1
					if L[n + 1][1] == (L[n][1] - 1) or L[n + 1][1] == (L[n][1] + 1) or L[n + 1][1] == L[n][1] :
						L[n + 1][1] = L[n][1]
					elif L[n + 1][1] < (L[n][1] - 1) :
						L[n + 1][1] += 1 
					else :
						L[n + 1][1] -= 1
				elif L[n + 1][1] > (L[n][1] + 1) :
					if L[n + 1][0] == (L[n][0] - 1) or L[n + 1][0] == (L[n][0] + 1) or L[n + 1][0] == L[n][0] :
						L[n + 1][0] = L[n][0]
					elif L[n + 1][0] < (L[n][0] - 1) :
						L[n + 1][0] += 1 
					else :
						L[n + 1][0] -= 1
					L[n + 1][1] -=1
				elif L[n + 1][0] > (L[n][0] + 1) :
					L[n + 1][0] -= 1
					if L[n + 1][1] == (L[n][1] - 1) or L[n + 1][1] == (L[n][1] + 1) or L[n + 1][1] == L[n][1] :
						L[n + 1][1] = L[n][1]
					elif L[n + 1][1] < (L[n][1] - 1) :
						L[n + 1][1] += 1 
					else :
						L[n + 1][1] -= 1
			P.add((L[-1][0], L[-1][1]))
	elif l[0] == "U" :
		for c in range(int(l[1])) :
			L[0][1] += 1
			for n in range(len(L) - 1) :
				if L[n + 1][1] < (L[n][1] - 1) :
					if L[n + 1][0] == (L[n][0] - 1) or L[n + 1][0] == (L[n][0] + 1) or L[n + 1][0] == L[n][0] :
						L[n + 1][0] = L[n][0]
					elif L[n + 1][0] < (L[n][0] - 1) :
						L[n + 1][0] += 1 
					else :
						L[n + 1][0] -= 1
					L[n + 1][1] +=1
				elif L[n + 1][0] < (L[n][0] - 1) :
					L[n + 1][0] += 1
					if L[n + 1][1] == (L[n][1] - 1) or L[n + 1][1] == (L[n][1] + 1) or L[n + 1][1] == L[n][1] :
						L[n + 1][1] = L[n][1]
					elif L[n + 1][1] < (L[n][1] - 1) :
						L[n + 1][1] += 1 
					else :
						L[n + 1][1] -= 1
				elif L[n + 1][1] > (L[n][1] + 1) :
					if L[n + 1][0] == (L[n][0] - 1) or L[n + 1][0] == (L[n][0] + 1) or L[n + 1][0] == L[n][0] :
						L[n + 1][0] = L[n][0]
					elif L[n + 1][0] < (L[n][0] - 1) :
						L[n + 1][0] += 1 
					else :
						L[n + 1][0] -= 1
					L[n + 1][1] -=1
				elif L[n + 1][0] > (L[n][0] + 1) :
					L[n + 1][0] -= 1
					if L[n + 1][1] == (L[n][1] - 1) or L[n + 1][1] == (L[n][1] + 1) or L[n + 1][1] == L[n][1] :
						L[n + 1][1] = L[n][1]
					elif L[n + 1][1] < (L[n][1] - 1) :
						L[n + 1][1] += 1 
					else :
						L[n + 1][1] -= 1
			P.add((L[-1][0], L[-1][1]))

print(len(P))
