import numpy as np
import math
import decimal as Decimal
import scipy as sc
from scipy import linalg
from scipy import interpolate
from periodic import findReducedMass #Import findReducedMass function from periodic.py file
import os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def calcKE(nBasis, reduced_mass, deltasq,h_mat):
	pisq = pow(float(math.pi),2)
	p1 = float(-1/3)*(pisq/deltasq)
	p2 = float(2)/deltasq
	beta = float(-2/deltasq)

	c = float(-1)/(2*reduced_mass)
	for n in range (0,nBasis):
		for m in range (0,nBasis):
			if(n==m):
				nsq = pow(n+1,2)
				h_mat[n,n] = h_mat[n,n] + c*(p1+ p2/(2*nsq))
				
			else:#n!=m
				a = abs(n-m)
				asq = a**2
				b = n+m+2
				bsq = b**2
				h_mat[n,m] = h_mat[n,m] + c*beta*((-1)**a/asq - (-1)**b/bsq)
		
def sortEigVal(eigvals,nBasis):
	for j in range (0,nBasis-1):
		for i in range (j+1,nBasis):
			if(eigvals[i] < eigvals[j]):
				temp = eigvals[j]
				eigvals[j] = eigvals[i]
				eigvals[i] = temp

def rotationalMotion(r_vals,j, rmass,h_mat,nBasis):
	
	for n in range (0,nBasis):
		rsq = r_vals[n]**2
		
		h_mat[n][n] +=(j*(j+1)*1)/(2*rmass*rsq)




def main_func(nBasis,filename,firstEl,secondEl,h_mat2,r_vals,deltasq):
	int_count = 0
	firstLine = ""
	lastLine = ""
	tempLine = ""
	n =0
	pi = math.pi
	prev = 0.0
	answer_arr = []
	
	
	nBasis = int(nBasis)
	
	rm = findReducedMass(firstEl,secondEl); #rm is reduced mass
	
	
	h_mat = np.full((nBasis,nBasis),0.0)
	T_mat = np.full((nBasis,nBasis),0.0)
	
	
	fileName = filename
	r_vals = r_vals
	deltasq = deltasq
	
	J = []
	y = []
	
	
	calcKE(nBasis,rm, deltasq,h_mat2)
	
	for j in range(0,21):
		h_mat = h_mat2.copy()
		rotationalMotion(r_vals, j, rm,h_mat,nBasis)
		eigvals, eigvecs = linalg.eig(h_mat)
		eigvals = eigvals.real
		sortEigVal(eigvals,nBasis)
		#print(eigvals)
		
		
		T_mat[0][j] = eigvals[0]
		T_mat[1][j] = eigvals[1]
		T_mat[2][j] = eigvals[2]
		T_mat[3][j] = eigvals[3]	
	
	a = 0
	overtones = []
	for n in range(1,4):
		y = []
		J = []			
	#	#pbranch		
		for j in range (20,0,-1):
			val = (T_mat[n][j-1] - T_mat[0][j])*(4.359744e-18)/(6.626e-34*2.9979e10)#convert a.u to J and then divide by hc
			y.append(val)
			J.append(-1*j)
			
		
	#	#rbranch
		for j in range (1,21):
			val = (T_mat[n][j] - T_mat[0][j-1])*(4.359744e-18)/(6.626e-34*2.9979e10)
			y.append(val)
			J.append(j)	
			
	
		f = interpolate.interp1d(J, y,kind = 'cubic')
		xnew = 0;
		ynew = f(xnew);
		J = J[:len(J)//2] + [xnew] + J[len(J)//2:];
		y = y[:len(y)//2] + [ynew] + y[len(y)//2:];
		
		
		popt = np.polyfit(J,y,3)
		if(a == 0):
			#print("De is {}".format(popt[0]/-4))
			answer_arr.append(format(popt[0]/-4))
			#print("ae is {}".format(popt[1]/-1))
			answer_arr.append(format(popt[1]/-1))
			be = (popt[2]/2)+ (popt[1]/-1)
			#print("Be is {}".format(be))
			answer_arr.append(format(be))
		a+=1
		overtones.append(popt[3])
	
	overtones.pop()
	overtones = np.array(overtones)
	C = ([1,-2],[2,-6])
	ans = np.linalg.inv(C).dot(overtones)
	#print("ve is {}".format(ans[0]))
	answer_arr.append(format(ans[0]))
	#print("vexe is {}".format(ans[1]))
	answer_arr.append(format(ans[1]))
	
	return answer_arr
	
		
	
	

	
