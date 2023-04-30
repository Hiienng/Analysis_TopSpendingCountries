https://www.programiz.com/python-programming/online-compiler/
https://www.learnx.org/dashboard/python/1/14
# 1. Variables and Types
  	myint = 7 
	myfloat = float(7)
	myfloat = 7.0
	mystring = 'hello'

	a = "hello"
	b = "world"
	c = 2
	d = 3
	c = a + " " + b
	print(a + " " + b*d, c, )

PRINT AS STRING

	if mystring == "hello":
   	print("String: %s" % mystring)
	
	if isinstance(myfloat, float) and myfloat == 10.0:
    	print("Float: %f" % myfloat)	
	
	mylist = [1,2,3]
	print("A list: %s" % mylist)

## PRINT AS F STRING 
	txt = "I have {an:.2f} Ruppes!"
	print(txt.format(an = 4))

	name = 'Tushar'
	age = 23
	print(f"Hello, My name is {name} and I'm {age} years old.")
	
	#
	txt = "I have {an:.2f} Ruppes!"
	print(txt.format(an = 4))

	# %s - String (or any object with a string representation, like numbers)
	# %d - Integers
	# %f - Floating point numbers
	# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

	# %x/%X - Integers in hex representation (lowercase/uppercase)

# 2. Lists

	mylist = []
	mylist.append(1) # => append adding the data into last position of list

	mylist1 = [1,2,3]
	mylist2 = [4,5,6]
	total = mylist1 + mylist2
	print(total)

To reverse a list

		list.reverse()
		my_list = list(reversed(my_list))
		my_list = my_list[::-1]

Shuffle a list: 
1. Approach 1

		import random
		random.shuffle(mylist)
	
2. Approach 2

		from random import shuffle
		x = [[i] for i in range(10)]
		shuffle(x)
		print(x)

		##PRINT 1 LETTER AT A POISTION
		list.pop(pos)
# 3. Basic Operators
## Arithmetic Operators

	a = 1 + 2 * 3 / 4.0
	b = remainder = 11 % 3
	c = 2 ** 3
	# True division /
	# Floor division //
	# Remainder(modulus) %
	# Exponentiaition **

# 4. String Formatting
	# initialize a multi-line string
	line_str = "I'm learning Python.\nI refer to TechBeamers.com tutorials."
	# check the index of a substring in another string
	str.find()
	str.rfind()
	str.index()
	str.rindex()
	re.search()
	isdigit() #>> check if the string only incl digits
	startswith() # >> check if a string starts with another string
	print(",".join("foo", "bar")) # >>  join a string with a comma delimiter
	print("foo, bar".slit(",")) # >> slit by comma
	print(x.capitalize())
## Basic String Operations
	astring = "Hello world!"
	print(len(astring))	  # >> len of a string
	print(astring.index("o")) # >> .index position of o
	print(astring.count("l")) # >> .count number of l
	print(astring[3:7])       # >> print the string from this position to other position
	print(astring[3:7:2])     # >> print the string from this position to other position at 2 steps
	print(astring[::-1])      # >> backward
	print(astring.upper())
	print(astring.lower())
	print(astring.startswith("Hello")) #>> true
	print(astring.endswith("asdfasdfasdf")) #>>False
	

# 5. Conditions
	# 
	if name in ["John", "Rick"]:
    		print("Your name is either John or Rick.")

	if name == "John" or name == "Rick":
    		print("Your name is either John or Rick.")
	
	#
	statement = False
	another_statement = True
	if statement is True:
    		Pass
	elif another_statement is True: # else if
    		Pass
    	else:
    		Pass
    
## Complex condition
	a = 200
	b = 33
	if b > a:
 	 print("b is greater than a")
	elif a == b:
	  print("a and b are equal")
	else:
	  print("a is greater than b")

## Null consequence = pass
	if (mutex == True) :
   	 pass
	else :
  	  print("False")

	#Condition in print
	x = [1,2,3]
	y = [1,2,3]
	print(x == y) 			# Prints out True
	print(x is y) 			# Prints out False
	print(not False) 		# Prints out True
	print((not False) == (False)) 	# Prints out False
	

# 6. Loops
## "FOR" LOOPS
	primes = [2, 3, 5, 7]
	for prime in primes:
    		print(prime)
	# >> a matrix 3 5 7
	for x in range(3, 8, 2):
    		print(x)
	
## "WHILE" LOOPS
	#Simple sample
	count = 0
	while count < 5:
    		print(count)
    		count += 1  # This is the same as count = count + 1 & Sequence is a matrix of 0 1 2 3 4
		
## "BREAK" STATEMENTS
	count = 0
	while True:
 	  print(count)
  	  count += 1
  	  if count >= 5:
    	  	break # Prints out 0,1,2,3,4

## "CONTINUE" STATEMENTS 
	#To skip the letter/number in range
	for x in range(10):
  	  if x % 2 == 0:   # Check if x is even
   	  	continue
	  print(x) 	   # Prints out only odd numbers - 1,3,5,7,9	

## LOOPS WITH ELSE
	count=0
	while(count<5):
   		print(count)
  	  	count +=1
	else:
    	print("count value reached %d" %(count))

	for i in range(1, 10):
  		if(i%5==0):
    		break
  		print(i)
	else:
 	print("this is not printed because for loop is terminated because of break but not due to fail in condition")

## NESTED LOOP
	names = ["John", "Jane"]
	foods = ["pizza", "sushi", "burgers"]
	for name in names:
   		for food in foods:
       		print(name + " likes " + food)
	
# 7. FUNCTIONS
	#
	def my_function():
	    print("Hello From My Function!")

	def my_function_with_args(username, greeting):
	    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

	def sum_two_numbers(a, b):
	    return a + b

	def my_func(name, age):
	    print(name + " is " + str(age) + " years old")	
	
	def my_function_with_args(username, greeting):
	    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))	
	my_function_with_args("John Doe", "a great year!")
	
	def sum_two_numbers(a, b):
	    return a + b
	x = sum_two_numbers(1,2)
	
## 1. FACTORIAL NUMBER
	import math
	math.factorial(1000)
## 2. ITERATIVE APPROACH
	def factorial(n):
	    fact = 1
	    for num in range(2, n + 1):
	        fact *= num
	    return fact
## 3. RECURSIVE APPROACH
	def factorial(n):
	    if n < 2:
	        return 1
	    else:
	        return n * factorial(n-1)	
## *ARGS STATEMENT 
	#To add
	def add(*numbers):
	    total = 0
	    for num in numbers:
	        total += num
	    return total
	print(add(2, 3, 5, 7, 9))

	def my_sum(my_integers):
	    result = 0
	    for x in my_integers:
	        result += x
	    return result
	list_of_integers = [1, 2, 3]
	print(my_sum(list_of_integers))

	def my_sum(*args):
	    result = 0
	    # Iterating over the Python args tuple
	    for x in args:
	        result += x
	    return result
	print(my_sum(1, 2, 3))

	def my_sum(*integers):
	    result = 0
	    for x in integers:
	        result += x
	    return result
	print(my_sum(1, 2, 3))

## **KWARGS STATEMENT
	def total_fruits(**fruits):
	    total = 0
	    for amount in fruits.values():
	        total += amount
	    return total
	print(total_fruits(banana=5, mango=7, apple=8))

	def concatenate(**kwargs):
	    result = ""
	    # Iterating over the Python kwargs dictionary
	    for arg in kwargs.values():
		result += arg
	    return result

	print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

	def concatenate(**words):
	    result = ""
	    for arg in words.values():
		result += arg
	    return result

	print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

	def concatenate(**kwargs):
	    result = ""
	    # Iterating over the keys of the Python kwargs dictionary
	    for arg in kwargs:
		result += arg
	    return result

	print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

## Lambda
	x = lambda a : a + 10
	print(x(5))

	x = lambda a, b : a * b
	print(x(5, 6))

	x = lambda a, b, c : a + b + c
	print(x(5, 6, 2))

	def myfunc(n):
	  return lambda a : a * n

	def myfunc(n):
	  return lambda a : a * n
	mydoubler = myfunc(2)
	print(mydoubler(11))

	def myfunc(n):
	  return lambda a : a * n
	mytripler = myfunc(3)
	print(mytripler(11))

	def myfunc(n):
	  return lambda a : a * n
	mydoubler = myfunc(2)
	mytripler = myfunc(3)

	print(mydoubler(11))
	print(mytripler(11))

# 08. CLASS, OBJECT FUNCTION, INSTANCE
Một lớp có 2 đối tượng: 
1. thuộc tính attribute 
2. phương thức method 
3. Property

## 8.1. CREATE CLASS
	class Car:
		pass
## 8.2. CREATE OBJECT OF THE CLASS
	class Car:
	    Sound = "beep" #this call instance (Thuộc tính/attribute)
	    Color = "green"
	Ford = Car() # assign the class(template) to an object with the variable "Ford" 
	Toyota = Car()
	    
## 8.2. ACCESSING A CLASS
## 8.3. ACCESSING AN OBJECT FUNCTION
## 8.4. ADD MANAGED ATTRIBUTES TO CLASS
Ford.color = "white" # change the attribute of ford into white, this will not change the color of Toyota

### __init__ Phương thức init giúp truyền dữ liệu vào thuộc tính color mà không ảnh hưởng đối tượng khác (toyota)

####Example 1
	class Car:
		def __init__(self, color):
			self.color = color
	Ford = Car('white')
	Toyota = Car('pink')
####Example 2
	Class Car2:
		sound = "beep..."
		def __init__(self,color,year)
			self.color123 = color
			selft.year345 = year
	Ford = Car2("Pink",2022)
	Print(ford.color123)
	Print(ford.year345) 
	Print(ford.sound) 
####Example 3
	Class Car3:
		sound = "beep..."
		def __init__(self,color)
			self.color123 = "orange"
	Print(Car3.sound) # result beep...
	#Print(ford.color) fail due to no result for ford
	ford = Card3('yellow')
	Print(ford.color) #result is "orange"

####Example 4
	# define the Vehicle class
	class Vehicle:
	    name = ""
	    kind = "car"
	    color = ""
	    value = 100.00
	    def description(self):
		desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
		return desc_str
	# your code goes here
	car1 = Vehicle()
	car1.name = 'Fer'
	car1.kind = 'convertible'
	car1.color = 'red'
	car1.value = 60000
	car2 = Vehicle()
	car2.name = 'Junp'
	car2.kind = 'van'
	car2.color = 'blue'
	car2.value = 10000

	# test code
	print(car1.description())
	print(car2.description())
####Example 5
	Class dog:
		def makesound(self): #Phương thức makesound trong lớp dog 
			print("bark")
	d = dog() #khai báo
	d.makesound #truy cập phương thức makesound
	
####Example 6: demo @property decorator >> Được sử dụng như một hàm tính riêng lẽ từ thông số đã input trước
	class Bill:    
	    def __init__(self, value, taxrate):
		self.value = value
		self.taxrate = taxrate
	    @property
	    def total(self):
		return self.value + self.value*self.taxrate

	    @total.setter
	    def total(self, total):
		self.value = total/(1+self.taxrate)

	bill1 = Bill(100, 0.5)
	bill1.total = 500
	print('value, total', bill1.value, bill1.total)
				


### 8.4.1 The Pythonic Approach
### 8.4.2 Providing Read-Only Attributes
### 8.4.3 Creating Read-Write Attributes
### 8.4.4 Providing Write-Only Attributes

# 09. Dictionaries
# 10. MODULES AND PACKAGES
# 11. LIST COMPREHENSION
# 12. REGULAR EXPRESSION
Q&A Section

1. 
2. Search at the **beginning**

        import re
        pattern = r"\d+"
        string = "123"
        if re.search(pattern, string) == 0:
            print("Found")
3. Search for **anywhere**


4. Split by a regex pattern?

        import re

        string = "one, two, three, four"
        pattern = ", "
        result = re.split(pattern, string)
        print(result)

12. Split by multiple delimiters? 

		import re
		string = "Some text; 123, Some text, 123"
		pattern = r"[,;]"
		print(re.split(pattern, string))

5. Replace by a regex pattern

        import re

        string = "one, two, three, four"
        pattern = ", "
        replacement = "-"
        result = re.sub(pattern, replacement, string)
        print(result)

́*6. Fetch all occurrences of a regex pattern
What is the wrong way fetch all occurrences of a regex pattern in a string?

	import re
        pattern = "ab"
        regex = re.compile(pattern)

*7. Count times replaces a regex pattern?

        import re
        pattern = r"\d+"
        string = "Some text. 123. Some text. 321"
        replacement = "Some text"
        result, replaced_count = re.subn(pattern, replacement, string)
        print(replaced_count)

*8. Match
What is the wrong way to get the part of the string where there was a match?

        import re
        pattern = r"\d+"
        string = "Some text. 123"
        match_object = re.match(pattern, string)
        print(match_object.group())    
11. Case-insensitive matching?

        import re

        text = "Python is a popular programming language"
        pattern = "python"

        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            print("Match found!")
9. Group
How do you find the substring that matched the last capturing **group of the regex**?

		import re

		text = "The cat is fat."
		match = re.search(r"(\w+)", text)
		captured_group = match.group(1)

		print(captured_group) # Output: 'cat'
Ví dụ khác:

	import re
	string = "hello world"
	pattern = r"(\w+) (\w+)"
	re_obj = re.compile(pattern)
	match = re_obj.search(string)
	print(match.group(2))

10. Pattern

The string r"{\n}" is a raw string that contains two characters: '{' and '\n'.
The string r"\n" là một raw string có chứa một ký tự là dòng mới.

13. Pattern
How do you capture any two characters except a newline between "py" and "on"?

Ký tự "." thường được sử dụng để biểu thị một ký tự bất kỳ trừ ký tự xuống dòng => pattern = r"py..on"


# 13. Exeption Handler - Xử lý ngoại lệ
6. xác định các hành động sẽ được thực thi, cho dù có ngoại lệ nào xảy ra hay không

		try:
		    # code that may raise an exception
		    number = int("abc")
		except ValueError as e:
		    print("Caught a ValueError exception:", e)
		finally:
		    # code in this block will always be executed, whether an exception was raised or not
		    print("Executing finally block")
In this example, the code in the finally block will always be executed, whether an exception was raised in the try block or not. This can be useful for performing clean-up actions, such as closing files, releasing resources, or rolling back transactions, to ensure that they are always executed regardless of the outcome of the try block.

9. define actions that should be executed when there was no exception in the "try" block

		try:
		    # code that may raise an exception
		    number = int("123")
		except ValueError as e:
		    print("Caught a ValueError exception:", e)
		else:
		    # code in this block will only be executed if no exception was raised in the try block
		    print("No exception raised, number =", number)
In this example, the code inside the try block will attempt to convert the string "123" to an integer. Since the string is a valid representation of an integer, no exception will be raised, and the code inside the else block will be executed. The result of the code will be:
No exception raised, number = 123

10. Which is a built-in exception type?

- AttributeError: Raised when an attribute reference or assignment fails.
- TypeError: Raised when an operation or function is applied to an object of inappropriate type.
- NameError: Raised when an undefined variable or function is referenced.
- IndexError: Raised when an index is out of range.
- KeyError: Raised when a dictionary key is not found.
- ValueError: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
- ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero.
- OSError: Raised when a function returns a system-related error.
- FileNotFoundError: Raised when a file or directory is requested but doesn't exist.
- StopIteration is raised when the next() function is called on an iterator and there are no more items to return.
- Warning is a base class for warning categories. When raised, it indicates a situation that is not an error, but might cause problems in the future. StopIteration is raised when the next() function is called on an iterator and there are no more items to return.

11.How do you reraise the current exception?
Để tái nạp (reraise) ngoại lệ hiện tại, bạn có thể sử dụng câu lệnh raise mà không có tham số trong một xử lý ngoại lệ. Điều này sẽ tái nạp cùng một ngoại lệ đã bị bắt và lan truyền nó đến mức độ kỹ thuật gọi tiếp theo.

	try:
	    # code that might raise an exception
	except Exception as e:
	    # Handle the exception
	    print("An exception was raised:", e)
	    # Reraise the same exception
	    raise
Trong ví dụ này, nếu một ngoại lệ được nổ trong khối try, nó sẽ bị bắt và xử lý bởi khối except. Câu lệnh raise trong khối except sau đó sẽ tái nạp cùng một ngoại lệ, lan truyền nó đến mức độ kỹ thuật gọi tiếp theo.

12. How can you conditionally raise and handle an exception during debugging?
Để tạo và xử lý ngoại lệ có điều kiện trong quá trình debug, người ta sử dụng một câu lệnh assert. Câu lệnh assert cho phép kiểm tra một điều kiện và tạo ra một ngoại lệ (AssertionError mặc định) nếu điều kiện không đạt được. Khi câu lệnh assert thất bại, ngoại lệ sẽ được tạo ra và chương trình sẽ dừng thực thi tại điểm đó, trừ khi ngoại lệ được bắt và xử lý.
Xử lý ngoại lệ do câu lệnh assert gây ra bằng cách sử dụng một khối try...except. Điều này cho phép bạn bắt ngoại lệ, in ra thông tin debug và tiếp tục thực thi chương trình nếu cần.
Ví dụ:

	def divide(a, b):
	    assert b != 0, "division by zero"
	    return a / b

	try:
	    result = divide(10, 0)
	except AssertionError as e:
	    print("Caught exception:", e)
	    result = float("inf")

	print("Result:", result)

13. How can you customize how a user-defined exception is displayed with the "print" function?
Để tùy chỉnh cách hiển thị cho một ngoại lệ do người dùng xác định bằng sử dụng "print" function, bạn cần ghi đè method __str__ trong lớp ngoại lệ của bạn. Method này trả về một chuỗi, mà sẽ được sử dụng như một chuỗi gốc khi ngoại lệ được in. Ví dụ: 

	class MyException(Exception):
	    def __init__(self, message):
		self.message = message

	    def __str__(self):
		return self.message

	try:
	    raise MyException("This is a custom exception")
	except MyException as e:
	    print(e)
Kết quả: This is a custom exception

14.Which of the following won't print a traceback of the exception being handled?
We can use traceback.print_tb(tb) to print the traceback information for a particular traceback object tb.
Example:

import traceback

try:
    1/0
except Exception as e:
    tb = sys.exc_info()[2]
    print("An error occurred:", e)
    traceback.print_tb(tb)
Kết quả:

An error occurred: division by zero
  File "<stdin>", line 2, in <module>

Or, we can use traceback.print_exception(etype, value, tb) to print the traceback information for an exception.

		import traceback

		try:
		    1/0
		except Exception as e:
		    print("An error occurred:", e)
		    traceback.print_exception(type(e), e, e.__traceback__)
Thao tác này sẽ in traceback cùng với thông báo lỗi:

		An error occurred: division by zero
		Traceback (most recent call last):
		  File "<stdin>", line 2, in <module>
		ZeroDivisionError: division by zero

or, we can use traceback.print_exc() to print the traceback information for the most recent exception that was raised

		import traceback

		try:
		    1/0
		except Exception as e:
		    print("An error occurred:", e)
		    traceback.print_exc()
Thao tác này sẽ in traceback cùng với thông báo lỗi:

		An error occurred: division by zero
		Traceback (most recent call last):
		  File "<stdin>", line 2, in <module>
		ZeroDivisionError: division by zero

