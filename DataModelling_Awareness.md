# DATA MODELLING - BUILDING A DATAMART
Content: (1) Một data modelling cơ bản (2) Một data modelling cơ bản trong lĩnh vực tài chính tiêu dùng
## Khái niệm, mục đích
## 1. A Basic Data modelling 
1. Phân tích > Nhận biết thực thể (Store, item, order, customer, cashier)
4. Nhận biết thuộc tính mỗi thực thể
- Order: order_id, order_date, total_due
- Item: item_id, item_name, item_price, amount, quantity
- Customer: order_id, customer_name, customer_point
4. Sắp xếp thực thể yếu, mạnh
5. Phân loại thuộc tính
- Thuộc tính khóa
- Thuộc tính đa trị
- Thuộc tính kết hợp (amount: amount = price * quantity)
- Thuộc tính dẫn xuất (total_due: = total amount)
6. Xác định mối liên hệ thực thể
- Customer - Order (1-N)
- Order - Item (1-N)

![image](https://user-images.githubusercontent.com/89530538/223070499-029b0e62-c0d6-414b-90da-3dbd6387c55d.png)

7. Chuyển ERD thành các bảng trong CSDL quan hệ
- Mỗi thực thể là một bảng, một bảng có một key primary và các bảng có quan hệ với nhau thông qua khóa ngoại
![image](https://user-images.githubusercontent.com/89530538/223071274-a9d4695a-63bc-4da9-9a76-5e2e77410cc8.png)
![image](https://user-images.githubusercontent.com/89530538/223071321-644ec5b4-4f35-47af-bdfd-56bd98c419c3.png)
![image](https://user-images.githubusercontent.com/89530538/223071358-729fadc1-b61c-45ea-90a7-91d5be2042a3.png)
![image](https://user-images.githubusercontent.com/89530538/223071834-7cdefe34-63a0-48ef-b740-207a9ae2e464.png)
- Trong quan hệ N-N, bảng được tách thành 2 quan hệ 1-N
![image](https://user-images.githubusercontent.com/89530538/223072433-8e8c524b-c26b-4e7a-b4e7-de4ae9d59441.png)

## 2. A Basic Data modelling in Consumer Finance Business
2. Các thực thể trong nhóm 1
- Group 1: Customer - Sales & UW
  - Application, Customer, Sale_channel, Sale_agent, Disbursement_method, Product_parametor
- Group 2: Repayment - Collection
  - Contract
3. Thuộc tính trong nhóm 1
- Group 1:
  -   Application: Application_id, Product_type, App_time_lev1, App_status_lev1, App_time_lev2, App_status_lev2, _Customer_id (foreign key)_, _Product_parametor_id (foreign key)_,_ Sale_name_id(foreign key), Channel_id(foreign key)_
  -   Product_parametor: Product_parametor_id, App_amount, App_tennor, App_IR, App_Insurance_amount
  -   Customer: Customer_id, cus_name, cus_sex, cus_DOB, cus_NID, cus_phone, cus_address, cus_reference, cus_init_riskgroup, cus_NTB_f, 
  -   Sale_channel _(Web/App/BNPL/3P)_: Channel_id, Channel_system_name
  -   Sale_agent: Sale_type_(TSA/DSA)_, Sale_name, Sale_name_id, Sale_region, ASM_ID, ASM_Name, RSM_ID, RSM_Name
- Group 2: 
  - Contract: Contract_id, Approval_date, Disbursement_date, Payment_date
