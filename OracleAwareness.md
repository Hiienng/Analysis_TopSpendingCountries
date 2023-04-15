# ORACLE / PLSQL RECAP
## 1. LÝ THUYẾT
#### 1. Phân biệt drop, delette, truncate
#### 2. Phân biệt các loại join (inner join, outer join, left join) và (union, intersect, except/minus)
#### 3. Phân biệt view  và table
- Một bảng (**table**) là một đối tượng lưu trữ dữ liệu có cấu trúc, được sắp xếp thành các hàng và cột. Mỗi bảng có một tên riêng và chứa các thuộc tính (cột) mô tả thông tin về các đối tượng trong bảng
- Một **view** (còn được gọi là "virtual table" hoặc "logical table") trong Oracle là một cái nhìn ảo của một bảng hoặc nhiều bảng, được tạo ra bằng cách chọn một số cột và hàng từ các bảng gốc và xếp chúng theo một cách nào đó. View không chứa dữ liệu trong nó, nhưng nó cung cấp một cách tiếp cận rất thuận tiện để truy vấn các dữ liệu từ nhiều bảng khác nhau.
- Sự khác nhau
  - Lưu trữ dữ liệu: Một table lưu trữ dữ liệu trong bảng, trong khi một view không lưu trữ dữ liệu trong nó.
  - Cấu trúc: Một table có cấu trúc rõ ràng với các cột và kiểu dữ liệu cụ thể cho mỗi cột, trong khi một view không có cấu trúc cụ thể và sử dụng cấu trúc của các bảng gốc để tạo ra view.
  - Cập nhật dữ liệu: Dữ liệu trong một table có thể được cập nhật trực tiếp, trong khi dữ liệu trong view chỉ có thể được cập nhật thông qua các bảng gốc mà view dựa trên.
  - Hiệu suất: Do view không lưu trữ dữ liệu, nên truy vấn dữ liệu thông qua view thường sẽ chậm hơn so với truy vấn dữ liệu trực tiếp từ bảng.
  - An ninh: Quyền truy cập vào bảng và view có thể được quản lý riêng lẻ trong Oracle, giúp bảo mật hơn cho dữ liệu.
## 2. BASIC CHEATSHEET

## 3. ADVANCED ISSUES
#### 1. Xử lý duplicate value
Find duplicate row (1 column) 
  
    Select colume_a, count(colume_a) 
    from table 
    group by colume_a
    having count() > 1
    
Find duplicate row (multible columns)

    Select colume_a, colume_b, count(colume_a) No_of_dup
    from table 
    group by colume_a, colume_b
    having count() > 1
    
Select dataset without dup value

    Select 
    
Delete dup value from current dataset -> This will impact the dataset

    #Sử dụng Delete from [table] where [conditions] COMMIT

### 2. Sử dụng rank, dense_rank và row_number
#### 2.1 Rank
Sắp xếp thứ tự trong bảng 

    select * rank () over (
                    partition by comlume 
                    order by price desc 
                        ) as price_rank from table

Tìm giá trị tại một điểm giá trị hoặc một xếp hạng cụ thể

    #statement Return the rank of an employee with a salary of $1,000 and a bonus of $500 from within the employees table.
    select RANK(1000, 500) WITHIN GROUP (ORDER BY salary, bonus)
    from employees;

#### 2.1 Dense_rank
Ta có bảng dữ liệu sau

![image](https://user-images.githubusercontent.com/89530538/222034104-efcb7f1b-9ce9-4a3c-83dc-aff20a7348a0.png)

      SELECT deptno,
             ename,
             hiredate,
             sal,
             RANK () OVER (PARTITION BY deptno ORDER BY sal) rank_sal,
             DENSE_RANK () OVER (PARTITION BY deptno ORDER BY sal) dense_rank_sal
        FROM emp
      ORDER BY deptno;

Khác nhau:
+ Hàm RANK sẽ bỏ qua thứ hạng tiếp theo cho những dòng có cùng hạng trước đó
+ Hàm DENSE_RANK không bỏ qua thứ hạng tiếp theo cho những dòng có cùng hạng trước đó

### 3. Sử dụng pivod để đổi chiều của bảng
### 4. Sử dụng procedure
Ứng dụng của procedure:
- Thực hiện tính toán phức tạp 
- Thực hiện các tác vụ ETL: Procedure được xem như 1 hàm và được sử dụng trong việc update một các MASS các bảng (table) dữ liệu cuối ngày. Cụ thể, trong một tổ chức thường các dataset được phân tầng được (1) API dữ liệu từ đối tác vào nội bộ bởi IT, (2) từ database cấp công ty xuống các database nhỏ hơn sang database cấp phòng ban bởi DI/BI, (3) và nhỏ hơn nữa... 

Thực hành:
![image](https://user-images.githubusercontent.com/89530538/222035357-94774c21-094f-407d-b7e5-39e625369d7c.png)

- Câu lệnh cơ bản để tạo một procedure:

      create or replace procedure [pro_name]
      as begin
      [comment queries]
      end;

- Câu lệnh thực hiện chạy precedure đã tạo
  
      Exec [pro_name]

##### 1. Tìm dữ liệu theo yêu cầu chưa biết trước
Tìm 2 bài hát có chữ d bên trong

![image](https://user-images.githubusercontent.com/89530538/222038292-f1cf0957-2519-4f2c-91b4-19cad804305d.png)

![image](https://user-images.githubusercontent.com/89530538/222038354-2c1708b0-2093-4332-b87a-d95bd5d9e552.png)

##### 2. Thực hiện các tác vụ ETL
- Để minh họa cho tác vụ ETL sử dụng procedure trong Oracle, hãy giả sử chúng ta có hai bảng trong cơ sở dữ liệu, một là bảng chứa thông tin sản phẩm và một là bảng chứa thông tin đơn hàng. Chúng ta muốn lấy dữ liệu từ hai bảng này để tạo một bảng mới chứa thông tin về đơn hàng và sản phẩm liên quan đến đơn hàng đó.
- Để thực hiện việc này, chúng ta có thể sử dụng một procedure với các bước sau:

1. Extract: Lấy dữ liệu từ hai bảng sản phẩm và đơn hàng bằng cách sử dụng một câu lệnh SELECT. Trong ví dụ này, chúng ta sẽ lấy thông tin về mã đơn hàng, tên sản phẩm và giá sản phẩm:

        CREATE OR REPLACE PROCEDURE perform_etl
        IS
        BEGIN
            DECLARE
                CURSOR c1 IS SELECT order_table.order_id, product_table.product_name, product_table.product_price
                            FROM order_table
                            INNER JOIN order_product ON order_table.order_id = order_product.order_id
                            INNER JOIN product_table ON order_product.product_id = product_table.product_id;
            BEGIN
    
2. Transform: Chuyển đổi dữ liệu theo yêu cầu của chúng ta. Trong ví dụ này, chúng ta sẽ tính toán tổng số tiền cho mỗi đơn hàng bằng cách nhân số lượng sản phẩm với giá của sản phẩm:

              FOR r1 IN c1 LOOP
                  INSERT INTO order_product_info(order_id, product_name, product_price, total_price)
                  VALUES(r1.order_id, r1.product_name, r1.product_price, r1.product_price * r1.quantity);
              END LOOP;
          END;
3. Load: Lưu trữ dữ liệu được chuyển đổi vào bảng mới:

        END;
        /

##### 3. Vì sao câu lệnh thông thường không thể thay thế Procedure
Giả sử chúng ta có một bảng employee trong cơ sở dữ liệu, với các cột employee_id, employee_name và employee_salary. Chúng ta muốn tăng lương cho tất cả các nhân viên trong bảng này bằng cách thêm vào số lượng lương được chỉ định. Ta sẽ dùng câu lệnh SELECT để cập nhật bảng như sau:

    UPDATE employee SET employee_salary = employee_salary + 1000;

Tuy nhiên, nếu chúng ta muốn thực hiện việc tăng lương này theo một tiến trình phức tạp hơn, ví dụ như tính toán số tiền thưởng dựa trên nhiều tiêu chí như kết quả kinh doanh và hiệu suất cá nhân của từng nhân viên, thì việc sử dụng chỉ câu lệnh SELECT sẽ không đủ. Trong trường hợp này, chúng ta cần sử dụng một procedure để tính toán số tiền thưởng và tăng lương cho từng nhân viên trong bảng employee. Procedure này có thể được thực hiện như sau:

    CREATE OR REPLACE PROCEDURE increase_salary
    IS
    BEGIN
        FOR emp IN (SELECT employee_id, employee_salary FROM employee)
        LOOP
            -- Calculate bonus based on business results and personal performance
            -- Update employee salary with bonus
            UPDATE employee
            SET employee_salary = emp.employee_salary + bonus_amount
            WHERE employee_id = emp.employee_id;
        END LOOP;
    END;

Như vậy, ta có thể thấy rằng, trong trường hợp này, việc sử dụng câu lệnh SELECT để cập nhật bảng không đủ để thực hiện tiến trình tăng lương phức tạp. Thay vào đó, chúng ta cần sử dụng một procedure để thực hiện các tính toán phức tạp và cập nhật bảng.

##### 4. Tính thời điểm trong việc cập nhật dữ liệu 
1. Một table được lấy dữ liệu từ một view, vậy khi view thay đổi các giá trị trong nó thì table có tự động cập nhật không
- Khi một view thay đổi các giá trị trong nó, các table được lấy dữ liệu từ view đó sẽ không tự động cập nhật để phản ánh những thay đổi đó. Tuy nhiên, nếu bạn muốn table có thể cập nhật dữ liệu mới từ view, bạn có thể sử dụng các trigger hoặc các procedure để đồng bộ hóa dữ liệu giữa view và table.
- Một trigger là một đoạn mã được kích hoạt tự động bởi một sự kiện nào đó trong cơ sở dữ liệu. Bằng cách sử dụng trigger, bạn có thể định nghĩa một hành động để thực hiện khi dữ liệu trong view thay đổi. Ví dụ, bạn có thể tạo một trigger sau khi cập nhật view để cập nhật lại các table tương ứng.
- Một procedure là một chương trình được định nghĩa bởi người dùng để thực hiện một hoặc nhiều hành động trong cơ sở dữ liệu. Bằng cách sử dụng procedure, bạn có thể thực hiện các hành động cập nhật dữ liệu trực tiếp trong các table từ view.
- Tuy nhiên, nên lưu ý rằng việc cập nhật dữ liệu trong table từ view có thể gây ra hiệu suất chậm, đặc biệt là khi view và table lớn và phức tạp. Do đó, nên cân nhắc cẩn thận trước khi sử dụng các trigger hoặc procedure để đồng bộ hóa dữ liệu giữa view và table.

2. Vậy, ví dụ Tại ngày 5, table1 có 2.000 dòng, tại ngày 10, table1 có 5.000 dòng. View2 lấy fetch dữ liệu từ table1 tại ngày 6, sau đó view1 fetch dữ liệu tư view2 và share dữ liệu đến excel tại ngày 7 . Vậy nếu không có một procedure này được chạy từ ngày 5 - 11 thì dữ liệu được refresh tại ngày 11 sẽ là bao nhiêu dòng và lấy dữ liệu từ table nào, bảng nào

- Nếu không có một procedure để đồng bộ hóa dữ liệu từ ngày 5 đến ngày 11 thì khi refresh dữ liệu tại ngày 11, view1 sẽ lấy dữ liệu từ view2 tại thời điểm fetch dữ liệu, tức là tại ngày 6, và view2 lấy dữ liệu từ table1 cũng tại thời điểm fetch dữ liệu, tức là tại ngày 6. Do đó, dữ liệu được refresh tại ngày 11 sẽ có số lượng dòng là 2.000, bằng với số lượng dòng của table1 tại ngày 5.
