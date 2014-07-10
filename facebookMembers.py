# This program will take an input file from a copy pasted facebook group members list
# and parse out their names


#Global variables
members = [2000];	# list to contain names

def main():
	"This contains the main code for the program"
	
	openFile();
	


def openFile():
	"This opens the file containing data including full names and stores name in a list"

	# Open a file
	print("Opening file...")
	try:
		openFile = open("data.txt", encoding= "utf8")	# open file for reading and writing "r+"
	except IOError:
		print("Error: Cannot find existing file")

	if(openFile):
		print("Sucess\n")
	else:
		print("Failed\n")

	# Write to file
	writeFile = open("members.txt", "w");

	counter = 0;
	index = 0;

	while openFile.readline():
		data = openFile.readline();
		if(data == "Add Friend\n"):		#used to locate the full name on following line
			member = openFile.readline();
			writeFile.write(member);
			index += 1;
			counter += 1;
	openFile.close();
	writeFile.close();
	print("Total number of names:",counter);
	


# Main execution of code
if __name__ == "__main__":
	main();





