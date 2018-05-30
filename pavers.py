import math
import sys

# int maxIndex = 0

def constructCandidates(num, number):
	# int n
	# long test, test1
	n = int(num)
	size = 256
	F, F1, F2, F3 = [size], [size], [size], [size]
	G, G1, G2, G3 = [size], [size], [size], [size]
	for i in range(0, size + 1):
		F.append(0)
		F1.append(0)
		F2.append(0)
		F3.append(0)
		G.append(0)
		G1.append(0)
		G2.append(0)
		G3.append(0)

	F[0] = 1
	F[1] = 2
	F[2] = 11
	F1[0] = 0
	F1[1] = 2
	F1[2] = 16
	F2[0] = 0
	F2[1] = 1
	F2[2] = 8
	F3[0] = 0
	F3[1] = 0
	F3[2] = 4
	G[0] = 0 
	G[1] = 0
	G[2] = 2
	G1[0] = G1[1] = 0
	G1[2] = 1
	G2[0] = G2[1] = 0
	G2[2] = 1
	G3[0] = G3[1] = 0
	G3[2] = 1

	for i in range (2, n + 1):
		F[i+1] = 2*F[i] + 7*F[i-1] + 4*G[i]
		# print(i)
		# print(F[n])
		F1[i+1] = 2*F1[i] + 2*F[i] + 7*F1[i-1] + 8*F[i-1] + 4*G1[i]+2*G[i]
		F2[i+1] = 2*F2[i] + F[i] + 7*F2[i-1] + 4*F[i-1] + 4*G2[i]+2*G[i]
		F3[i+1] = 2*F3[i] + 7*F3[i-1] + 4*F[i-1] + 4*G3[i]+2*G[i]
		# test = 2.0*((double)(n+1))*F[n+1]
		# test1 = F1[n+1] + 2.0*F2[n+1] + 3.0*F3[n+1]
		# if math.abs(test - test1) > .0000001*test:
		# 	print 'mismatch', n+1, test, test1
		G[i+1] = 2*F[i-1] + G[i]
		G1[i+1] = 2*F1[i-1] + F[i-1] + G1[i]
		G2[i+1] = 2*F2[i-1] + F[i-1] + G2[i] + G[i]
		G3[i+1] = 2*F3[i-1] + F[i-1] + G3[i]
	print(number, F[n], F1[n], F2[n], F3[n])
		

def main():
 	# num = open(sys.argv[1]).readline()
 	# for i in range (1, int(num) + 1):
 	# 	print(i)
 		filename = sys.argv[-1]
 		with open(filename, 'r') as f:
 			lines = f.readlines()
 			for j in range(1, len(lines)):
 				line = lines[j]
 				number = line.split(" ", 1)[0]
 				# print("number: "+number)
 				num = line.split(" ", 1)[1]
 				constructCandidates(num, number)
 	
if __name__ == "__main__":
    main()