"""
In this project, we aim to implement 7 tools of Statistical Process Control, also called 7 magnificent tools of quality. They are:
1. Histogram - to find normality in the process,
2. Scatter diagram - to find correlation and regression analysis,
3. Pareto chart - to find the major causes by 80-20 rule,
4. Cause and effect diagram - to analyze the goals, problems and departments,
5. Defect concentration diagram - to find parts/modules with most defects,
6. Check list - a list of complaints/things to be corrected, and
7. Control chart - to find the band of acceptability of product.
"""

"""import necessary modules for inbuilt functions"""
import numpy
import scipy.stats as stat
import matplotlib.pyplot as plt
import pandas as pd
#import requests

"""File operations"""
f = open("../sample/Sample.txt", 'r')

text = f.read()
print("\ntext\n")
print(text)
#print(type(text))
#print("len(text)")
#print(len(text))

lines = text.split()
print("\nlines\n")
print(lines)
m = len(lines)
#print(len(lines))

words = []
for line in lines:
	words.append(line.split(','))
print("\nwords\n")
print(words)
#print(len(words))

colTitles = words[0]
n = len(colTitles)
n = n - 1
print("\ncolTitles\n")
print(colTitles)
#print(len(colTitles))

rowTitles = []
for i in range(m):
	rowTitles.append(words[i].pop(0))
print("\nrowTitles\n")
print(rowTitles)
#print(len(rowTitles))

# 1*mn matrix of words
#print(m,n)
Y = []
for i in range(1,m):
	for j in range(n):
		Y.append(words[i][j])
m = m - 1
#print(m,n)
# print(Y)

for y in Y:
	try:
		y = float(Y.pop(0))	
	except:
		y = 0
	Y.append(y)
# print("Y")
# print(Y)
# print(len(Y))

# m*n matrix
X = []
for i in range(m):
	X.append(Y[i*n:(i+1)*n])
print("\nData Frame - X\n")
print(X)
# print(len(X))
m = len(X)
n = len(X[1])
# print("m = ", m)
# print("n = ", n)

"""Stats Operations"""
#filer
filer = 0
#sparse-ing - isn't it done? except = 0
#make these tuples

def desc(arr):
	s = 0
	ssd = 0
	scd = 0
	sfd = 0

	for a in arr:
		s += a

	#Mean, first central moment
	m1 = s / len(arr)
	print("Arithmetic mean = ", m1)

	for a in arr:
		ssd += ((a - m1) ** 2)
		scd += ((a - m1) ** 3)
		sfd += ((a - m1) ** 4)

	#Variance, Second central moment
	m2 = ssd / len(arr)
	print("Variance = ", m2)

	#Standard deviation
	#sd = scipy.sqrt(m2)
	#print("sd = ", sd)

	#Third central moment
	m3 = scd / len(arr)
	#print "Third Moment(Y) = ", m3
	
	#Skewness
	skew = m3 / (m2 ** (3/2))
	print("Skewness = ", skew)
	if skew > 0:
		print("Positively Skewed")
	elif skew < 0:
		print("Negatively Skewed data")
	else:
		print("Symmetric data")
		
	#Fourth central moment
	m4 = sfd / len(arr)
	#print "Fourth Moment(Y) = ", m4

	#Kurtosis
	kurt = m4 / (m2 ** 2)
	exkurt = kurt - 3
	print("Kurtosis = ", kurt)
	print("Excess Kurtosis = ", exkurt)
	if kurt > 3:
		print("Leptokurtic data")
	elif kurt < 3:
		print("Platykurtic data")
	else:
		print("Mesokurtic data")
		
	print("Geometric mean = ", stat.gmean(arr))
	print("Harmonic mean = ", stat.hmean(arr))
	print("Mode = ", stat.mode(arr))
	
	#return summary = {}
	#median
	#quartile
	#box plot
	#most likely estimator
	
	im = plt.figure()
	plt.hist(arr)
	plt.show()
	global filer
	im.savefig("../sample/desc%d.png" %filer, bbox_inches="tight")
	filer += 1
	return filer

"""Descriptive Statistics and histogram"""
# #Histogram of the entire data set
# desc(X)

#Histogram for some rows
for i in range(4):
	desc(X[i])


def scat(arr1, arr2):
	plt.subplot(2,1,1)
	plt.plot(arr1)
	plt.subplot(2,1,2)
	plt.plot(arr2)
	plt.show()
	#plt.plot(arr1,arr2)
	#plt.show()
	
	im = plt.figure()
	for i in range(len(arr1)):
		for j in range(len(arr2)):
			plt.scatter(arr1[i],arr2[j])
	plt.show()
	global filer
	im.savefig("../sample/scat%d.png" %filer, bbox_inches="tight")
	filer += 1
	return filer

"""Scatter plot"""
#scatter all vs all
#Too demanding as m*n increases
#plt.plot(X)
scat(X,X)

#scatter each row against itself and others
for i in range(2):
	for j in range(2):
		scat(X[i], X[j])

# #put inside scat
# #correlation matrix
df = pd.DataFrame(data=X,columns = colTitles)
im = plt.figure()
df.cumsum().plot()
df.plot.barh(stacked="True")
df.diff().hist(cumulative = True, alpha = 0.7, figsize=(4,4))
im.savefig("../sample/hist.png", bbox_inches="tight")
df.plot.box()
pd.plotting.scatter_matrix(df, alpha = 0.7, figsize=(4,4))
im.savefig("../sample/scat.png", bbox_inches="tight")
df.plot.pie(autopct='%.2f', subplots= True)
df.plot.area()
plt.show()

print("\nCorrelation Matrix\n")
print(df.corr())

def control(arr):
	xBar = stat.tmean(arr)
	print("xBar")
	print(xBar)
	#R = max(arr) - min(arr)
	#print(R)
	S = stat.tvar(arr) ** 0.5
	print("S")
	print(S)
	cl = numpy.empty(len(arr))
	cl.fill(xBar)
	ucl = numpy.empty(len(arr))
	ucl.fill(xBar + 1.5 * S)
	lcl = numpy.empty(len(arr))
	lcl.fill(xBar - 1.5 * S)
	im = plt.figure()
	plt.plot(arr,marker = "o")
	plt.plot(cl, color = 'g')
	plt.plot(ucl, color = 'r')
	plt.plot(lcl, color = 'r')
	plt.show()
	global filer
	im.savefig("../sample/ctrl%d.png" %filer, bbox_inches="tight")
	filer += 1
	return filer

#3S Control chart for some rows
for i in range(4):
	control(X[i])
	
"""
Done - frontend
algorithm CauseEffect
	input:	list of causes
	output:	fishbone diagram
				5M + E
			Man
			Machine
			Material
			Method
			Measurement
			Environment
TBD - backend flowchart

algorithm Pareto
	input: table of complaints(col0) and frequencies(col1) T
	output: Pareto chart

	C[] <- T.col[0]
	F[] <- T.col[1]
	sum = 0
	CF[0] = 0
	for i in range(len(F)):
		CF[i] = CF [i - 1] + F[i]
		sum += F[i]
	for i in range(len(F)):
		RCF[i] = CF[i] / sum
	T.col[2] <- RCF[]
	T.sort(col[2])
	plot(T.col[0], T.col[2])
	if RCF[i] < .80:
		major complaint
	else:
		minor complaint

#def Pareto(name):
	#par = open("/home/spikebuster/ycm/sample/pareto.csv", 'r')

#Pareto(Y)

algorithm DefectConcentration
	#from charts
	Chance cause
	Assignable cause

#POST with form-encoded data
#r = requests.post("http://localhost/spc.com/html/test.html", data=payload)
#print(r.text)
"""