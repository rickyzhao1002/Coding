# This program will parse through a facebook user info taking the name and the gender

def main():
	"This function will open a containing file, parse the data, and write to an output file"

	# Open file to read
	print("Opening file...")
	try:
		openFile = open("info.txt", "r")	# open file for reading and writing
	except IOError:
		print("Error: Cannot find existing file")

	if(openFile):
		print("Sucess\n")
	else:
		print("Failed\n")

	# Open file to write
	writeFile = open("userInfo.txt", "w");

	data = "1"
	nameExtracted = False;

	# Run through file
	while data:
		data = openFile.readline();

		# Extract name
		if "name" in data:
			if(nameExtracted == False):
				inputData = data;
				inputData = inputData[12:-3]
				writeFile.write(inputData);
				writeFile.write("\n");
				nameExtracted = True;

		# Extract gender
		if "gender" in data:
			inputData2 = data;
			inputData2 = data[14:-3];
			writeFile.write(inputData2);
			writeFile.write("\n\n");
			nameExtracted = False;	# Reset for next user data

	# Close files
	openFile.close();
	writeFile.close();

# Main execution of code
if __name__ == "__main__":
	main();