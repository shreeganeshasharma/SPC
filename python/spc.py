"""
Statistical Process Control Tool
Author: Shree Ganesha Sharma M S

Abstract and Objective

Quality can be defined as "fitness for use". If a product or service is available in the market, we look for some characteristic properties, and desire numerous dimensions, which make it superior over other products, and improve its sales. They can be features, aesthetic, performance, cost, serviceability etc.

Therefore, it is paramount that we understand quality, achieve it, and control it. This is the aim of Statistical Quality Control (SQC). We can achieve and control quality through Design of experiments, Process control, and Product control.

Process Control is a continuous process during the manufacturing, which involves sampling the items and measuring their properties and hence the quality.
In this project, we aim to implement 7 tools of Statistical Process Control, also called 7 magnificent tools of quality. They are:
1. Histogram - to find normality in the process,
2. Scatter diagram - to find correlation and regression analysis,
3. Pareto chart - to find the major causes by 80-20 rule,
4. Cause and effect diagram - to analyze the goals, problems and departments,
5. Defect concentration diagram - to find parts/modules with most defects,
6. Check list - a list of complaints/things to be corrected, and
7. Control chart - to find the band of acceptability of product.
"""

#import necessary modules for inbuilt functions
import math
#import random
import scipy.stats as stat
import pandas as pd
#import csv
import matplotlib.pyplot as plt
import requests

"""
	make responsive
	def integrate(filename):
		f = open("/home/spikebuster/ycm/sample/Sample.csv", 'r')
		f = open("/home/spikebuster/ycm/sample/Sample.html", 'r')
		f = open("/home/spikebuster/ycm/sample/Sample.xlsx", 'r')
		f = open("/home/spikebuster/ycm/sample/Sample.pdf", 'r')
"""

f = open("/home/spikebuster/ycm/sample/Sample.txt", 'r')
#f = open("/home/spikebuster/ycm/sample/eg.csv", 'r')

url = "https://w3schools.com/python/demopage.htm"
payload = {'firstName': 'Ganesh'}

# GET
r = requests.get(url)
#print(r.text)
# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
r = requests.post(url, data=payload)

text = f.read()
print "text"
print text, len(text)

lines = text.split()
m = len(lines)

words = []
for line in lines:
	words.append(line.split(','))

print "lines"
print lines, len(lines)

print "words"
print words, len(words)

colTitles = words[0]
n = len(colTitles)
n = n - 1
print "colTitles"
print colTitles, len(colTitles)

rowTitles = []
for i in range(m):
	rowTitles.append(words[i].pop(0))
print "rowTitles"
print rowTitles, len(rowTitles)

Y = []
for i in range(1,m):
	for j in range(n):
		Y.append(words[i][j])
m = m - 1
#print m, n
#print Y

for y in Y:
	try:
		y = float(Y.pop(0))	
	except:
		y = 0
	Y.append(y)

print "Y"
print Y, len(Y)

X = []
for i in range(m):
	X.append(Y[i*n:(i+1)*n])
print "X"
print X, len(X)

print "m = ", m
print "n = ", n

#filer
filer = 0

#sparse-ing
#make these tuples
def histog(arr):
	s = 0
	ssd = 0
	scd = 0
	sfd = 0

	for a in arr:
		s += a

	#Mean, first central moment
	m1 = s / len(arr)
	print "mean = ", m1


	for a in arr:
		ssd += ((a - m1) ** 2)
		scd += ((a - m1) ** 3)
		sfd += ((a - m1) ** 4)

	#Variance, Second central moment
	m2 = ssd / len(arr)
	print "var = ", m2

	#Standard deviation
	sd = math.sqrt(m2)
	print "sd = ", sd

	#Third central moment
	m3 = scd / len(arr)
	#print "Third Moment(Y) = ", m3

	#Fourth central moment
	m4 = sfd / len(arr)
	#print "Fourth Moment(Y) = ", m4

	#Skewness
	skew = m3 / (m2 ** (3/2))
	print "Skewness = ", skew
	if skew > 0:
		print "Positively Skewed"
	elif skew < 0:
		print "Negatively Skewed data"
	else:
		print "Symmetric data"

	#Kurtosis
	kurt = m4 / (m2 ** 2)
	exkurt = kurt - 3
	print "Kurtosis = ", kurt
	print "Excess Kurtosis = ", exkurt
	if kurt > 3:
		print "Leptokurtic data"
	elif kurt < 3:
		print "Platykurtic data"
	else:
		print "Mesokurtic data"

	im = plt.figure()
	plt.hist(arr)
	plt.show()
	im.savefig("sample/%d.pdf" %filer, bbox_inches="tight")
	global filer
	filer += 1

	#print "Geometric mean"
	#print stat.gmean(arr)

	#print "Harmonic mean"
	#print stat.hmean(arr)

	print "Mode"
	print stat.mode(arr)


	#return summary = {}
	#median
	#quartile
	#box plot
	#most likely estimator
	return filer

#Histogram of the entire data set
#histog(Y)

#Histogram for all rows
#for i in range(3):
	#histog(X[i])

#Histogram for each column
#for j in range(n):
#	for i in range(m):
#		plt.hist()
#	plt.show()

"""
Scat
	output: scatter diagram, correlation, regression

	#for i = 1:n in X plot(row[i])
	#for j = 1:m in X plot(col[j])
	#Scatter diagram
	plot(X)
	#for row[i], row[j] in X corr(row[i], row[j])
	#for col[j], col[j] in X corr(col[i], col[j])
	corr(X)
	corr(Y)
	linearRegression(X)
	linearRegression(Y)

"""
def scat(arr1, arr2):
	plt.subplot(2,1,1)
	plt.plot(arr1)
	plt.subplot(2,1,2)
	plt.plot(arr2)	
	plt.show()

	im = plt.figure()

	for i in range(len(arr1)):
		for j in range(len(arr2)):
			plt.scatter(arr1[i],arr2[j])
	plt.show()
	im.savefig("sample/%d.pdf" %filer, bbox_inches="tight")


	global filer
	filer += 1

	return

#scatter all vs all
#Too demanding as m*n increases
#scat(Y,Y)

#scatter each row against itself
#for i in range(len(X)):
#for i in range(3):
	#scat(X[i], X[i])

#correlation matrix
#df = pd.DataFrame(data=X)
#print "Correlation Matrix"
#print df.corr()

#def Pareto(name):
	#par = open("/home/spikebuster/ycm/sample/pareto.csv", 'r')

#Pareto(Y)
"""

#TBD on frontend
algorithm CheckList
	input:	list of complaints
			list of to be done items
			drop down

#TBD on frontend
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

algorithm ControlChart
	input : m * n matrix X
			1 x m * n vector Y
	output: Control charts
	#Pending
	Variable - X bar, S, and R
	Attribute - p and np, c and u for defective/not defective vs no of defects

	Upper Control Limit
	Lower Control Limit
	6 Sigma Limits
	Probabilistic limits
	Specification limits

algorithm DefectConcentration
	#from charts
	Chance cause
	Assignable cause
"""
