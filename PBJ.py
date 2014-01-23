import random

#Define how many indigents we have
pb =  random.randrange(0, 10+1)
jelly =  random.randrange(0, 10+1)
bread =  random.randrange(0, 10+1)

if pb == 1:
	servings_of_pb = "one serving of"
elif pb >1:
	servings_of_pb = "{0} servings of".format(pb)
else:
	servings_of_pb = " zero servings of"

if jelly == 1:
	servings_of_jelly = "one serving of"
elif pb >1:
	servings_of_jelly = "{0} servings of".format(jelly)
else:
	servings_of_jelly= "zero servings of"

if bread == 1:
	No_of_bread = "one slice"
elif bread >1:
	No_of_bread = "{0} slices".format(bread)
else:
	No_of_bread = "zero slices"

No_bread_pairs = bread/2 # Number of Pairs of Bread for a full sandwich

#Figuring out the minimum ingredient we have to determine the number of PBJ sandwiches
if No_bread_pairs <= pb and No_bread_pairs < jelly:
	No_of_sandwiches = No_bread_pairs
elif pb <= jelly and pb < No_bread_pairs:
	No_of_sandwiches = pb
elif jelly < pb and jelly <= No_bread_pairs:
	No_of_sandwiches = jelly
elif No_bread_pairs == 0 or pb == 0 or jelly == 0:
	No_of_sandwiches = 0
else:
	No_of_sandwiches = 0
	
if No_of_sandwiches == 1 :
	part1 = "one PB&J sandwich. Hip Hip Hooray."
elif No_of_sandwiches >1 :
	part1 = "{0} PB&J sandwiches! Lunch will be awesome.".format(No_of_sandwiches)
else:
	part1 = "zero PB&J sandwiches :-(. Let's see the alternatives!"

#Define what we have left over to determine the number of open face sandwiches
open_face = bread%2
leftoverJ = jelly - No_of_sandwiches
leftoverPB = pb - No_of_sandwiches

if open_face == 1 and leftoverJ>=1 and leftoverPB>=1:
	No_of_open_face = 1
elif bread == 0 or jelly == 0 or pb == 0:
	No_of_open_face = 0
else:
	No_of_open_face = 0

if No_of_open_face == 1 :
	part2 = "one PB&J open face sandwich. Not the best, but just deal with it."
else:
	part2 = "zero PB&J  open face sandwiches. There must be other sandwiches"

#Define what we have left over after open face sandwiches to determine the number of single ingredient sandwiches
leftoverJ2 = jelly - No_of_sandwiches - No_of_open_face
leftoverPB2 = pb - No_of_sandwiches - No_of_open_face
leftoverB2 = bread - (No_of_sandwiches*2) - No_of_open_face
leftover_no_of_bread= leftoverB2/2

#Makes a jelly sandwich with the minimum ingredient 
if leftoverJ2 <= leftover_no_of_bread and leftoverB2>=2 and leftoverJ2!=0:
	no_of_jelly_sandwich = leftoverJ2
elif leftoverJ2 > leftover_no_of_bread and leftoverB2>=2 and leftoverJ2!=0:
	no_of_jelly_sandwich = leftover_no_of_bread
elif leftoverJ2==0 or leftoverB2<=2:
	no_of_jelly_sandwich = 0
else:
	no_of_jelly_sandwich = 0

if no_of_jelly_sandwich == 1 :
	part3 = "one jelly sandwich Good...I guess."
elif no_of_jelly_sandwich >1 :
	part3 = "{0} Jelly sandwiches! I hope you like jelly.".format(no_of_jelly_sandwich)
else:
	part3 = "zero jelly sandwiches. Peanut butter is better anyways."
#Makes a peanut butter sandwich with the minimum ingredient 
if leftoverPB2 <= leftover_no_of_bread and leftoverB2>=2 and leftoverPB2!=0:
	no_of_pb_sandwich = leftoverPB2
elif leftoverPB2 > leftover_no_of_bread and leftoverB2>=2 and leftoverPB2!=0:
	no_of_pb_sandwich = leftover_no_of_bread
elif leftoverPB2==0 or leftoverB2<=2:
	no_of_pb_sandwich = 0
else:
	no_of_pb_sandwich = 0

if no_of_pb_sandwich == 1 :
	part4 = "one peanut butter sandwich for you. Good...I guess."
elif no_of_pb_sandwich >1 :
	part4 = "{0} peanut butter sandwiches! I hope you like peanut butter.".format(no_of_pb_sandwich)
else:
	part4 = "zero peanut butter sandwiches. Aww shucks."

#Calculates how many sandwiches total we made today!
total_sandwich = No_of_sandwiches + No_of_open_face + no_of_jelly_sandwich + no_of_pb_sandwich

if total_sandwich == 1:
	part5 = "Only one sandwich today. I hope it fills you up!"
elif total_sandwich >1:
	part5 = "{0} sandwiches today for lunch! I hope you're hungry.".format(total_sandwich)
else:
	part5 = "No sandwiches for you today. It's time for take out!"

#Output of the entire program
print """
You have {0} peanut butter, {1} jelly, and {2} of bread. 
Therefore you can make {3}
You can make {4}
And make {5}
You can make {6}
{7}""".format(servings_of_pb, servings_of_jelly, No_of_bread, part1, part2, part3, part4, part5)
