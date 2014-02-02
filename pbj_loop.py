import random

# Determines the value of each variable
pb = random.randrange(1, 11)
jelly = random.randrange(1, 11)
bread = random.randrange(1, 21)
sandwiches = 0

# Prints out the number of ingridients we have for reference
print "I have {0} slices of bread, {1} servings of peanut butter, and {2} servings of jelly.".format(bread, pb, jelly)

#Creates a loop to determine how many sandwiches we can make, and also displays left over ingridients
while bread>=2 and pb >=1 and jelly >=1:
	bread = bread - 2
	pb = pb -1
	jelly = jelly - 1
	sandwiches = sandwiches + 1
	print "I am making sandwich # {0}.".format(sandwiches)
	print "I have enough bread to make {0} sandwiches, enough peanut butter for {1} sandwiches, and enough jelly for {2} sandwiches.".format(bread/2, pb, jelly)

#Determines which ingridient was the reason why we could not make any more sandwiches and prints that information out
if bread == 0 and pb == 0 and jelly == 0:
	print "All done; We ran out of all of our ingredients"
elif bread <= 1 and pb >=1 and jelly >=1:
	print "All Done; We ran out of bread!"
elif pb <1 and bread >=2 and jelly >=1:
	print "All Done; We ran out of peanut butter!"
else:
	print "All Done; We ran out of jelly!"

#Prints out the number of sandwiches we were able to make
print "We had enough to make {0} sandwiches.".format(sandwiches)
