def findReducedMass(firstEl,secondEl):

	periodic_dict = {
		'H-1':1.007,
		'H-2':2.014,
		'H-3':3.016,	
		'HE-4':4.002,
		'LI-6':6.015,
		'LI-7':7.016,	
		'BE-9':9.012,	
		'B-10':10.012,
		'B-11':11.009,	
		'C-12':12.000,
		'C-13':13.003,
		'C-14':14.003,	
		'N-14':14.007,
		'N-15':15.000,	
		'O-16':15.995,
		'O-17':16.999,	
		'O-18':17.999,
		'F-19':18.998,	
		'NE-20':19.992,
		'NE-21':20.993,
		'NE-22':21.991,	
		'NA-23':22.989,	
		'MG-24':23.985,
		'MG-25':24.985,	
		'AL-27':26.982,	
		'SI-28':27.976,	
		'P-31':30.974,	
		'S-32':32.065,
		'CL-35':34.968,
		'CL-37':36.965,
		'AR-36':35.968,
		'AR-38':37.963,
		'AR-40':39.962,
		'K-39':38.962,
		'K-40':39.963,
		'K-41':40.962,
		'CA-40':39.963,
		'CA-42':41.948,
		'CA-43':42.959
	};
	
	#print("Enter first element.Put a dash and followed by isotope")
	#print("Example: \"CL-37\" = chlorine 37 isotope which gives a mass of 36.965")
	#el = input('')
	el = firstEl
	y= periodic_dict[el.upper()]
	mass1 = float(y * 0.001)/(6.022e23)#g/mol to kg
	mass1 = mass1/(9.109e-31)#kg to m_e
	#mass1 = y
	#print("Enter second element.Put a dash and followed by isotope")
	#el = input('')
	el = secondEl
	y= periodic_dict[el.upper()]
	mass2 = float(y * 0.001)/(6.022e23) #g_mol to kg
	mass2 = mass1/(9.109e-31)#g/mol to m_e
	#mass2 = y
	numerator = mass1*mass2
	denominator = mass1 + mass2
	reducedMass = numerator/float(denominator)
	
	return reducedMass





