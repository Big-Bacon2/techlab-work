# author: Big-Bacon2
 grade = float(input("Type a percent:"))
if grade >= 90:
	print "You earned an A on your recent test!"
elif grade <= 89 and grade >= 80:
	print "You earned an B on your recent test!"
elif grade <= 79 and grade >= 70:
	print "You earned an C on your recent test!"
elif grade <= 69 and grade >= 51:
	print "You earned an D on your recent test!"
elif grade <= 50 and grade > 1:
	print "You earned an F on your recent test!"
elif grade <=1:
	print "You earned a grade unknown to school teachers!"