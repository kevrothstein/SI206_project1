import os
import filecmp
import datetime


def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	file1 = open(file, "r")
	head = file1.readline().strip().split(',')
	data_list = []


	for data in file1.readlines():
		dictionary = {}
		number = 0
		data_list2 = data.strip().split(',')
		for keys in head:
			dictionary[keys] = data_list2[number]
			number += 1
		data_list.append(dictionary)
	return data_list
#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sort_list = sorted(data, key = lambda x: x[col])
	return sort_list[0]["First"] + ' ' + sort_list[0]["Last"]

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	grade_sizes = {'Senior':0, 'Junior':0, 'Freshman':0, 'Sophomore':0}
	for kevin in data:
		if kevin['Class'] == 'Senior':
			grade_sizes['Senior'] += 1
		elif kevin['Class'] == 'Junior':
			grade_sizes['Junior'] += 1
		elif kevin['Class'] == 'Freshman':
			grade_sizes['Freshman'] += 1
		elif kevin['Class'] == 'Sophomore':
			grade_sizes['Sophomore'] += 1
	sort_class = sorted(grade_sizes, key= lambda kevin: grade_sizes[kevin], reverse= True)
	total = []
	for kevin in sort_class:
		total.append((kevin, grade_sizes[kevin]))
	return total			



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	day_dict = {}
	for kevin in a:
		date= kevin['DOB'].split('/')
		day = date[1]
		if day not in day_dict:
			day_dict[day] = 1
		else:
			day_dict[day] += 1
	days_sort = sorted(day_dict, key = lambda kevin:day_dict[kevin], reverse= True)			
	return int(days_sort[0])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	age_list= []
	for kevin in a[1:]:
		birth_month, birth_day, birth_year = kevin['DOB'].split('/')
		year_now = int(datetime.date.today().year)
		month_now = int(datetime.date.today().month) 
		current_day = int(datetime.date.today().day)
		if ((current_day > int(birth_day)) and (month_now) > int(birth_month)):
			age_list.append(year_now - int(birth_year))
		else:
			age_list.append(year_now - int(birth_year) + 1)
	return round((sum(age_list)/ len(age_list)), 0)			


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	my_csv = open(fileName, 'w')
	list_sorted = sorted(a, key = lambda x: x[col])

	for element in list_sorted:
		lst = []
		for y in element.values():
			lst.append(y)
		rows = ",".join(lst[:3])
		my_csv.write(rows + "\n")

	my_csv.close()
	return None


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

