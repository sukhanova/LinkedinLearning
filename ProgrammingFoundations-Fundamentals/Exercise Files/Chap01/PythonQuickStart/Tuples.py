# if you need to use a sequence that cannot be changed after creation - Python has a type of sequence called a tuple.
# A tuple has a specific order and the items in a tuple cannot be changed once created.


child1_birth = ("Oliver", "Fairview Riverside", "Minneapolis", "Minnesota", "USA", "01/01/2001")

child2_birth = ("Sam", "Allina Health", "Roseville",
                "Minnesota", "USA", "07/03/2003")

type(child1_birth)
type(child2_birth)


print(child1_birth)
print(child2_birth[2])

#if you run any lines below - error displays tuple' object does not support item assignment
child2_birth[0] = "Samantha"
random.shuffle(child1_birth)
