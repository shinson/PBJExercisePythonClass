import random

pb = random.randrange(0, 10+1)
jelly = random.randrange(0, 10+1)
bread = random.randrange(0, 10+1)

if bread == 1:
	Nobread = "one slice"
elif bread >1:
	Nobread = "{0} slices".format(bread)
else:
	Nobread = " 0 slices."

if pb >=1 and jelly >=1 and bread >=2:
	PBJsandwich = "Yes"
else:
	PBJsandwich = "No"

NoOfBread = bread/2

if NoOfBread < pb and NoOfBread < jelly:
	NoOfSandwiches = NoOfBread
elif pb < jelly and pb < NoOfBread:
	NoOfSandwiches = pb
elif pb > jelly and jelly < NoOfBread:
	NoOfSandwiches = jelly
elif NoOfBread == 0 or pb == 0 or jelly == 0:
	NoOfSandwiches = 0
else:
	NoOfSandwiches = 0
	
if NoOfSandwiches == 1 :
	part1 = "1 PB&J sandwich. Hip Hip Hooray."
elif NoOfSandwiches >1 :
	part1 = "{0} PB&J sandwiches! Lunch will be awesome.".format(NoOfSandwiches)
else:
	part1 = "0 PB&J sandwiches :-(. Let's see the alternatives!"

openFace = bread%2
leftoverJ = jelly - NoOfSandwiches
leftoverPB = pb - NoOfSandwiches

if openFace == 1 and leftoverJ>=1 and leftoverPB>=1:
	NoOpenFace = 1
elif bread == 0 or jelly == 0 or pb == 0:
	NoOpenFace = 0
else:
	NoOpenFace = 0

if NoOpenFace == 1 :
	part2 = "1 PB&J open face sandwich. Not the best, but just deal with it."
else:
	part2 = "0 PB&J  open face sandwiches. There must be other sandwiches"

leftoverJ2 = jelly - NoOfSandwiches - NoOpenFace
leftoverPB2 = pb - NoOfSandwiches - NoOpenFace
leftoverB2 = bread - (NoOfSandwiches*2) - NoOpenFace
leftoverNoOfBread = (bread/2) - (NoOfSandwiches) - NoOpenFace


if leftoverJ2 < leftoverNoOfBread and leftoverB2>=2 and leftoverJ2 >=1:
	noJellySandwich = leftoverJ2
elif leftoverJ2 > leftoverNoOfBread and leftoverB2>=2:
	noJellySandwich = leftoverNoOfBread
elif leftoverJ2==0 or leftoverNoOfBread<=2:
	noJellySandwich = 0
else:
	noJellySandwich = 0

if noJellySandwich == 1 :
	part3 = "1 jelly sandwich Good...I guess."
elif noJellySandwich >1 :
	part3 = "{0} Jelly sandwiches! I hope you like jelly.".format(noJellySandwich)
else:
	part3 = "0 jelly sandwiches. Peanut butter is better anyways."

if leftoverPB2 < leftoverNoOfBread and leftoverB2>=2 and leftoverPB>=1:
	noPbSandwich = leftoverJ2
elif leftoverPB2 > leftoverNoOfBread and leftoverB2>=2:
	noPbSandwich = leftoverNoOfBread
elif leftoverPB2==0 or leftoverNoOfBread<=2:
	noPbSandwich = 0
else:
	noPbSandwich = 0

if noPbSandwich == 1 :
	part4 = "1 peanut butter sandwich for you. Good...I guess."
elif noPbSandwich >1 :
	part4 = "{0} peanut butter sandwiches! I hope you like peanut butter.".format(noPbSandwich)
else:
	part4 = "0 peanut butter sandwiches. Aww shucks."

totalSandwich = NoOfSandwiches + NoOpenFace + noJellySandwich + noPbSandwich

if totalSandwich == 1:
	part5 = "Only 1 sandwich today. I hope it fills you up!"
elif totalSandwich >1:
	part5 = "{0} sandwiches today for lunch! I hope you're hungry.".format(totalSandwich)
else:
	part5 = "No sandwiches for you today. It's time for take out!"


print """
You have {0} peanut butter, {1} jelly, and {2} of bread. 
Therefore you can make {3}
You can make {4}
And make {5}
Finally, you can make {6}
{7}""".format(pb, jelly, Nobread, part1, part2, part3, part4, part5)
