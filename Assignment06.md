Assignment (Lecture:9 and 10)

1. Clear concepts of Git using this video: https://youtu.be/SWYqp7iY_Tc

2. Modify the student_api project such that 
	- `/students/?branch=coe` returns only those students which are in `coe` branch. 
	- `/students/?cgpa=8` returns only those student who have 8 cgpa.
	- `/students/?branch=coe&cgpa=8` returns those students who are in `coe` branch and have 8 cgpa.

	Hint: Use `request.args` to get URL parameters dictionary.