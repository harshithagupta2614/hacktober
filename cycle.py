# Python program to impleament cycle sort

def cycleSort(array):
writes = 0
	
# Loop through the array to find cycles to rotate.
for cycleStart in range(0, len(array) - 1):
	item = array[cycleStart]
	
	# Find where to put the item.
	pos = cycleStart
	for i in range(cycleStart + 1, len(array)):
	if array[i] < item:
		pos += 1
	

	if pos == cycleStart:
	continue

	while item == array[pos]:
	pos += 1
	array[pos], item = item, array[pos]
	writes += 1
	

	while pos != cycleStart:
		

	pos = cycleStart
	for i in range(cycleStart + 1, len(array)):
		if array[i] < item:
		pos += 1
		

	while item == array[pos]:
		pos += 1
	array[pos], item = item, array[pos]
	writes += 1
	
return writes
	


