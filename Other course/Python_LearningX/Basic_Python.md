# PYTHON CƠ BẢN

# Chương 2. Toán tử
## 2.2 Cấu trúc điều kiện
    If condition 1:
      iden
    Elif condition 2: 
      iden
    else :
      iden

## For ... in
    For letter in 'Hien'
      print("the letters are: ", letter)
## While
    count = 0
    while count <5:
      print(count)
      count = count + 1
## 2.5 Hàm - Function
    def cute_square(a):
        return a3 + 1
    print(cute_square(3))
## 2.6 Xử lý chuỗi
1. Trích suất chuỗi con - Sử dụng phương thức Str[]

    str = 'Hello world'
    print str[0:4]

2. Lấy độ dài của chuỗi - Sử dụng phương thức count = len("Hello world")

3. Tìm & thay thế nội dung - Sử dụng phương thức str.replace
    str = 'Hello world'
    newstr = str.replace('Hello', 'Bye')
    print newstr

4. Tìm vị trí chuỗi con - Sử dụng phương thức str.find('world')

5. Tách chuỗi
6. Sử dụng phương thức str.split(' ')
....

## 2.7 List
#### 1. Add a new element to a list

    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]

or

    my_list = [1, 2, 3]
    my_list += [4, 5]
    print(my_list)  # Output: [1, 2, 3, 4, 5]

or

    my_list = [1, 2, 3]
    my_list.extend([4, 5])
    print(my_list)  # Output: [1, 2, 3, 4, 5]


#### 2. Access the first element

    my_list = [1, 2, 3, 4, 5]
    first_element = my_list[0]
    print(first_element)  # Output: 1

### 2.7.2 LIST COMPREHENSION
#### 1. Tạo một từ điển với các khóa được in hoa theo cách comprehension

        original_dict = {"a": 1, "b": 2}
        capitalized_dict = {k.upper(): v for k, v in original_dict.items()}
hoặc, dùng vòng lặp

        original_dict = {"a": 1, "b": 2}
        capitalized_dict = {}
        for key, value in original_dict.items():
            capitalized_dict[key.upper()] = value
            
 hoặc, sử dụng list comprehensie
 
        {key.capitalize(): value for key, value in original_dict.items()}

#### 2. Cách tính tổng giá trị tuyệt đối của một danh sách

        my_list = [-1, -2, 3, 4, -5]
        absolute_sum = sum(abs(x) for x in my_list)
        print(absolute_sum)


## 2.8 Tuple 
Tuple cũng là một cấu trúc mảng, tương tự như cấu trúc List. Một số điểm khác nhau cơ bản là khai báo Tuple sử dụng cặp dấu ngoặc (...) và một tuple đã được khai báo
rồi thì không thay đổi được giá trị (immutable) và không hỗ trợ các phương thức như append() , pop() …Ví dụ:

## 2.9 Dictionary
#### 1. Xóa giá trị của khóa "key" trong một từ điển - Delete the value of a key "key" from a dictionary:
a. You can delete the value of a key "key" from a dictionary in Python 

    del my_dict["key"]

b. or, use the pop() method

    my_dict.pop("key")

c. If the key is not found, the pop() method will raise a KeyError, but you can use pop() method with a second parameter, this parameter is the default value that will be returned if the key is not found.

    my_dict.pop("key", None)

d. or, use the popitem() method to remove and return an arbitrary (key, value) item pair from the dictionary.

    my_dict.popitem()
e. or, use the del statement with the dict.items() method and a for-loop

    for key in list(my_dict.keys()):
        if key == 'key':
            del my_dict[key]

f. or, use the del statement with the dict.keys() method and a for-loop.

    for key in my_dict.keys():
        if key == 'key':
            del my_dict[key]

g. or, use the dict.clear() method to remove all the key-value pairs from the dictionary.

    my_dict.clear()

#### 2. Tạo một từ điển từ hai danh sách tương ứng của khóa và giá trị? - Creating a dictionary from two corresponding lists of keys and values
a. Using the zip function and the dict constructor:

    keys = [1, 2, 3]
    values = ['a', 'b', 'c']
    my_dict = dict(zip(keys, values))
    print(my_dict) # {1: 'a', 2: 'b', 3: 'c'}

b. Using a dictionary comprehension:

    keys = [1, 2, 3]
    values = ['a', 'b', 'c']
    my_dict = {keys[i]: values[i] for i in range(len(keys))}
    print(my_dict) # {1: 'a', 2: 'b', 3: 'c'}

c. Using the zip function and a dictionary comprehension:

    keys = [1, 2, 3]
    values = ['a', 'b', 'c']
    my_dict = {k: v for k, v in zip(keys, values)}
    print(my_dict) # {1: 'a', 2: 'b', 3: 'c'}

d. Using the dict.fromkeys() method:

    keys = [1, 2, 3]
    values = ['a', 'b', 'c']
    my_dict = dict.fromkeys(keys, values)
    print(my_dict) # {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c'], 3: ['a', 'b', 'c']}

e. Using the collections.OrderedDict() class

    from collections import OrderedDict
    keys = [1, 2, 3]
    values = ['a', 'b', 'c']
    my_dict = OrderedDict(zip(keys, values))
    print(my_dict) # {1: 'a', 2: 'b', 3: 'c'}

Note that if you want to create a dict with keys and values from different size lists, you may want to use the zip_longest function from the itertools module.

# Chương 3. MODULE
Có 3 loại module thường thấy là:
1. Viết bằng Python: có phần mở rộng là .py
2. Các thư viện liên kết động: có phần mở rộng là .dll , .pyd , .so , .sl ,…
3. C-Module liên kết với trình phiên dịch.



#### 1. Chỉ định module - Import module
Chỉ định một module có thể theo cách thông thường:

    import module_name

Hoặc, chỉ định một module có công thức toán học - import module which contains mathematical functions and constants:

    import math

Once a module is imported, you can use its functions and variables by referencing them with the module name followed by a dot (.) and the function or variable name.
Use the pi constant from the math module:

    import math
    print(math.pi) # Output: 3.141592653589793

Import a module is using the from keyword, with this way you can import a specific function or variable from a module without importing the whole module.

    from module_name import function_or_variable

Import the pi constant from the math module:

    from math import pi
    print(pi) # Output: 3.141592653589793

Import multiple functions or variables from a module, separating them by a comma:

    from module_name import function1, function2, variable1, variable2

You can also use * to import all functions and variables from a module:

    from module_name import *

#### 2. Ổ chứa module

    import sys
    sys.path.append('/path/to/my/module')

Set the PYTHONPATH environment variable to a list of directories separated by : on UNIX or ; on Windows. These directories will be added to the search path.

    export PYTHONPATH=$PYTHONPATH:/path/to/my/module

#### 3. Chỉ định module theo điều kiện trước - Conditionally importing a module

    import sys

    if sys.version_info >= (3,0):
        import mymodule3 as mymodule
    else:
        import mymodule2 as mymodule
    # Use the imported module
    mymodule.some_function()

#### 4. Chỉ định module trong cùng 1 gói - Imported module located within the same package
Khi nhập khẩu một module từ trong cùng một gói, bạn không cần chỉ định tên gói bằng cú pháp "."
Ví dụ, giả sử bạn có một gói tên là mypackage và nó chứa hai module: module1 và module2. Nếu bạn muốn nhập khẩu module2 từ trong module1, bạn có thể sử dụng một nhập khẩu tương đối như sau:

    from . import module2
Hoặc nhập khẩu module như bình thường

    import mypackage.module2
Hoặc,

    from mypackage import module2
    
Trong tất cả các ví dụ trên, Python sẽ tìm kiếm module2 trong gói mypackage, và không trong bất kỳ gói khác.

#### 5. Tự động nhập một MODULE bằng HÀM - Dynamically import a module using a function
1. Thông qua importlib

        import importlib

        def import_module(module_name):
            return importlib.import_module(module_name)

        my_module = import_module("my_module")
hoặc,

        def import_module(module_name):
            return __import__(module_name)

        my_module = import_module("my_module")

hoặc,

        def import_module_attribute(module_name, attribute):
            module = importlib.import_module(module_name)
            return getattr(module, attribute)

2. Sử dụng hàm built-in "__import__()", không thông qua importlib. Hàm này có thể được gọi với một tham số là một chuỗi tên của module mà bạn muốn nạp và nó sẽ trả về đối tượng module.

        def import_module(module_name):
            return __import__(module_name)

        my_module = import_module("my_module")

Có thể nạp một thuộc tính cụ thể của một module bằng hàm

        def import_module_attribute(module_name, attribute):
            module = __import__(module_name)
            return getattr(module, attribute)
Lưu ý rằng khi gọi hàm này lần đầu, module sẽ được nạp và các lần gọi tiếp theo sẽ sử dụng module đã nạp.

# Chương 4. CLASS
## 1. Khai báo class
    
    class animal():
        name = ''
        age = 0
        def __init__(self, name = '', age = 0):
            self.name = name
            self.age = age
        def show(self):
            print('My name is ', self.name)
        def run(self):
            print('Animal is running...')
        def go(self):
            print('Animal is going...')

    class dog(animal):
            def run(self):
            print('Dog is running...')
   
    myanimal = animal()
    myanimal.show()
    myanimal.run()
    myanimal.go()
    mydog = dog('Lucy')
    mydog.show()
    mydog.run()
    mydog.go()

Trong ví dụ trên thì:
- animal và dog là 2 class. Trong đó class dog kế thừa từ class cha là animal nên sẽ có các phương thức của class animal  
- name và age là thuộc tính (Attribute) của class.
- Phương thức __init__(self) là hàm tạo của class. Hàm này sẽ được gọi mỗi khi có một object mới được tạo (từ một class), gọi là quá trình tạo instance 
- show() , run() và go() là 2 phương thức của 2 class. Khi khai báo phương thức có kèm tham số self dùng để truy cập ngược lại object đang gọi. Lúc gọi phương thức thì không cần truyền tham số này
- Phương thức run() của class dog gọi là override của phương thức run() của class animal


# Chương 4. RE - REGULAR EXPRESSION
Tìm kiếm một số điện thoại ở đầu chuỗi bằng cách thêm ký tự ^ vào trước mẫu biểu thức chính quy r'\d{3}-\d{3}-\d{4}' để tìm kiếm số điện thoại.

    import re
    # Tạo một đối tượng biểu thức chính quy tìm kiếm số điện thoại tại đầu chuỗi
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}')
    
    # Tìm kiếm trong chuỗi
    result = pattern.search("My phone number is 555-555-5555")

    # In kết quả
    print(result.group())  # 555-555-5555

1 match 
Hàm này khớp với mẫu regex trong chuỗi với cờ tùy chọn. Nó trả về true nếu một kết quả khớp được tìm thấy trong chuỗi nếu không nó trả về false.

2 search 
Hàm này trả về đối tượng khớp nếu có một kết quả khớp được tìm thấy trong chuỗi.

3 findall
Nó trả về một danh sách chứa tất cả các kết quả khớp của một mẫu trong chuỗi.

4 split
Trả về một danh sách trong đó chuỗi đã được phân chia theo mỗi kết quả khớp.

5 sub
Thay thế một hoặc nhiều kết quả khớp trong chuỗi.


