from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import Session, relationship, backref
from sqlalchemy.ext.automap import automap_base
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "super secret key"
Bootstrap(app)

Base = automap_base()
engine = create_engine('mysql://root@localhost/regDB')

# reflect the tables
Base.prepare(engine, reflect=True)

students = Base.classes.students

studentsCourse = Base.classes.studentCourse

session = Session(engine)




 #routers to pages

#studnet registration deletion and list
@app.route('/student')
def student():
	student = session.query(students).all()
	return render_template("student.html",item=student)
	#return ""

@app.route('/student/new', methods=['GET', 'POST'])
def newStudnet():
	if request.method == 'POST':
		newstudent  = students(stid = request.form['stid'], Fname=request.form['fname'],\
		Mname=request.form['mname'], Lname=request.form['lname'], Gender=request.form['gender'],\
		dcode=request.form['dcode'] )

		#session.rollback()
		session.add(newstudent)
		session.commit()
		return redirect(url_for('student'))
	else:
		return render_template('newstudent.html')






@app.route('/student/<int:stid>/delete', methods=['GET', 'POST'] )
def delStudnet(stid):
	editedItem = session.query(students).filter_by(stid=stid).one()
	if request.method == 'POST':
		session.delete(editedItem)
		session.commit()
	return render_template(
            'delestudent.html', stid=stid,  item=editedItem)
 	#return "delete new student"

@app.route('/student/<int:stid>/edit', methods=['GET', 'POST'])
def editStudnet(stid):
	editedItem = session.query(students).filter_by(stid=stid).one()
	if request.method == 'POST':
		if request.form['Fname']:
			editedItem.Fname = request.form['Fname']
		if request.form['gender']:
			editedItem.Gender = request.form['gender']
		if request.form['dcode']:
			editedItem.dcode = request.form['dcode']

		session.add(editedItem)
		session.commit()
		return redirect(url_for('student', stid=stid))
	else:

		return render_template(
            'editstudent.html', stid=stid,  item=editedItem)


 	#return "add new student"



@app.route('/stdcourse')
def stdcourse():
	student = session.query(studentsCourse).all()
	return render_template("studentCourse.html",item=student)
 	#return 'student courses list'

# courses add up and removal
@app.route('/course')
def course():

 	return 'courses list'


@app.route('/course/new')
def newCourse():
 	return 'add new course'

@app.route('/course/delete')
def delCourse():
 	return 'delete course'





# department crud procces

@app.route('/department')
def department():
	return 'list of department'

@app.route('/department/new')
def newdepartment():
	return 'new dapartment added'

@app.route('/department/delete')
def deldepartment():
	return 'department deleted'


# lectural course 

@app.route('/lectural')
def lectural():
	return 'list of lectural'

@app.route('/lectural/new')
def newlectural():
	return 'new lectural added'

@app.route('/lectural/delete')
def dellectural():
	return 'lectural deleted'


# studentcourses add up and removal



@app.route('/stdcourse/new')
def newstdCourse():
 	return 'add new  student course'

@app.route('/stdcourse/delete')
def delstdCourse():
 	return 'delete student course'


#lectural course 
@app.route('/leccourse')
def leccourse():
 	return 'lecture courses list'


@app.route('/leccourse/new')
def newlecCourse():
 	return 'add new  lectural course'

@app.route('/leccourse/delete')
def dellecCourse():
 	return 'delete lectural course'







if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)