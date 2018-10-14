'''
Team Member #1: Will Fraisl
Team Member #2: N/A
Zagmail Address for Team Member #1: wfraisl@zagmail.gonzaga.edu
Project 2: This project asks the user to enter a file name and substring
	and displays the number of substring in the file
Due: 9/7/18
'''

def open_file():
	while(True):
		file_name = raw_input("Enter an input file name: ")
		try:
			file_contents = open(file_name, "r").read()
			break
		except:
			print("Invalid file name.  Try again.")
	return file_contents

def searchSub(string,subStr,posStr_in):
	posSub = 0;
	posStr = posStr_in
	while(posSub < len(subStr)):
		if string[posStr] == subStr[posSub]:
			posSub = posSub + 1
			posStr = posStr + 1
		else:
			return -1
	return posStr_in

def count_substrings(string,subStr):
	count = 0
	posStr = 0
	lastSub = len(string) - len(subStr)

	while (posStr <= lastSub):
		pos = searchSub(string,subStr,posStr)
		if (pos >= 0):
			count += 1
			posStr += 1
		else:
			posStr += 1
	print count, "substrings found"
def main():
	file_contents = open_file()
	substring = raw_input("Enter a substring to search: ")
	count_substrings(file_contents,substring)

main()
