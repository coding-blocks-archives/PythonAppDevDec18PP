Assignment (Lecture:6 and 7)

1. Write a generator function to iterate over first `n` fibonacci numbers.

2. Consider a list of the form:
	```
	[
		(x1, y1, z1),
	 	(x2, y2, z2),
	 	(x3, y3, z3),
	 	.
	 	.
	 	.
	 	(xn, yn, zn)
	 ]
	```
	Transform it to following form:
	```
	[
		(x1, x2, x3, ...., xn),
		(y1, y2, y3, ...., yn),
		(z1, z2, z3, ...., zn)
	]
	```

3. Write a program which takes a text file as input and does following operations sequentially over it:
	- Get list of words present in file
	- Convert all words to uppercase (using map)
	- Remove the words from list which contain 'A' (using filter)
	- Generate a string by concatenating all the words in the final list (using reduce)

4. Go through the available public apis listed here: https://github.com/toddmotto/public-apis. Select any 2 of your favorite APIs and write a python script to: 
	- collect data from those APIs
	- save the data in a file (json/txt file)

5. Write a simple python script which 
	- inputs the path to an image folder from the user
	- creates a new album on imgur and save the album hash provided in the response (https://apidocs.imgur.com/#8f89bd41-28a1-4624-9393-95e12cec509a)
	- uploads all images in the local folder to the album (https://apidocs.imgur.com/#b98029b6-5cc1-4a6f-b4bf-fe1db50869a2)
	- provide the album link to the user.