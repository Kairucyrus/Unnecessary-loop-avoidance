our_list = [[[1,4,5]], [[8, 0,7]]]

def flatten_list(info):
	flattened = []
	for list_one in info:
		for list_two in list_one:
			for x in list_two:
				flattened.append(x)
	return flattened

out = print(f"Nested for loop: {flatten_list(our_list)}")
print("\n")


from itertools import chain
def flat_short(info):
    return list(chain.from_iterable(chain.from_iterable(info)))
print(f"Simplified flattening: {flat_short(our_list)}")
