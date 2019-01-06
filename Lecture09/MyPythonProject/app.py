from flask import Flask, render_template, request
from datetime import datetime
import csv

app = Flask(__name__)

@app.route('/hello')
def index():
	data = [[1,2,3],
			[4,5,6],
			[7,8,9]]
	return render_template('index.html', name="Nikhil",
		hobbies=['Football', 'Cricket', 'Kabaddi'], data=data)

@app.route('/task/<int:task_id>/')
def show_picture(task_id):
	task = {
		'id': task_id,
		'name': 'bjdskvbfjk',
		'time': datetime.now()
	}
	return render_template('task.html', task=task)


@app.route('/shubham/')
def shubham():
	print(request.args)
	return str(request.args)

@app.route('/portal/', methods=['GET', 'POST'])
def student_portal():
	if request.method == 'GET':
		return render_template('student_form.html')
	else:
		fields = ['roll_no', 'name', 'branch', 'gender', 'dob', 'photo']
		with open("student_data.csv", 'a') as f:
			csv_writer = csv.DictWriter(f, fieldnames=fields)
			csv_writer.writerow(dict(request.form))

		photo = request.files.get('photo')
		photo.save('static/images/{}'.format(photo.filename))
		return "Thanks for submitting"

if __name__ == "__main__":
	app.run(port=8000, use_reloader=True, debug=True)