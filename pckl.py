import pickle

# Make the dictionary that you're gonna save
your_data = {1:2, 3:4, 5:6}

# Open a file for writing as a binary file

# The `with` block automatically closes the file at the end of the block
# I find it easier than manually closing the file
with open("out.pck", "wb") as out_file:
	# And write your data out for a file so you can get it back later
	pickle.dump(your_data, out_file)
