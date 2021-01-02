from flask import Flask,redirect, url_for, request
from flask import render_template
from SEMV2 import main_func
#from werkzeug import secure_filename
import numpy as np
app = Flask(__name__)

@app.route("/")
def success():
	return render_template('index.html')
	
@app.route("/index")
def tryagain():
	return redirect("/")

@app.route('/calculate',methods = ['POST'])
def login():
	if request.method == 'POST':
		felement = request.form['dropdown1']
		selement = request.form['dropdown2']
		basisF = request.form['basisF']
		#filename = request.form['filename']
		filename = request.files['file'].filename
		f = request.files['file']
     		#read file
		lines = f.readlines();
		num_lines = sum(1 for line in lines)
		if(num_lines != basisF):
			return render_template('failure.html',message = "The number of basis function entered does not match the number of lines in your file.Please try again")
     		#initialize variables
		r_vals = []
		int_count = 0  
		last_val =0
		nBasis = int(basisF)
		
		h_mat = np.full((nBasis,nBasis),0.0)
		for line in lines:
			line = line.decode()
			if(int_count == 0):
				tempLine = line.strip()
				tempLine = line.lstrip()
				pVal = tempLine.split()
				firstLine = float(pVal[0])*(1.8897261339213) #firstline is r_min
				r_vals.append(float(pVal[0])*1.8897261339213)
				h_mat[int_count,int_count] += float(pVal[1])

			else:
		#if((line.strip != " ")and(int_count < nBasis)): #does not store empty
				if(line.strip != " "):
					tempLine = line.strip()
					tempLine = line.lstrip()
					pVal = tempLine.split()
					lastLine = float(pVal[0])*(1.8897261339213) #lastLine is r_max
					#print(pVal[0])
					r_vals.append(float(pVal[0])*1.8897261339213)
					h_mat[int_count,int_count] += float(pVal[1])
					last_val = float(pVal[1])
			int_count+=1
		
		for i in range(0,int_count):
        		h_mat[i,i] = h_mat[i,i] - last_val;
		
		rmax = float(lastLine)
		rmin = float(firstLine)
		nBasis = int_count 
		delta = (rmax - rmin)/ (nBasis)
     		#print("delta is {}".format(delta))
		deltasq = delta**2
		
		answer_arr = main_func(nBasis,filename,felement,selement,h_mat,r_vals,deltasq)
		#return answer_arr[0]
		return render_template('success.html',answer = answer_arr)

     #f.save(f.filename)
     #
     #return answer_arr[0]
#  else:
#     user = request.args.get('nm')
#     return redirect(url_for('success',name = user))


		

	







if __name__ == "__main__":
    app.run(debug=True)
