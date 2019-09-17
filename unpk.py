import pickle

# Open a file for reading as a binary file

# The `with` block automatically closes the file at the end of the block
# I find it easier than manually closing the file
with open("out.pck", "rb") as in_file:
	# Load the dictonary back from the pickle file
	your_data = pickle.load(in_file)

# Now you can use the dictionary like you made it this run!
print(your_data)
print(your_data[1])
