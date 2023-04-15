# Machine Learning Fundamentals
Road map of the course:
- Prediction: Classification, regression, probability estimation
- Reresentation: Clustering, projecction, dictionary, autoencoder
- Deep learning

# Week 1: Introduction: nearest neighbor, and a host of prediction problems
## MNIST
`MNIST` is a classic dataset in machine learning, consisting of 28x28 gray-scale images handwritten digits. The original training set contains 60,000 examples and the test set contains 10,000 examples. In this notebook we will be working with a subset of this data: a training set of 7,500 examples and a test set of 1,000 examples.

### Accuracy of nearest neighbor on MNIST
- Training error: is an overly optimistic predictor of the future performance
- Test error: fraction of test points incorrectly classified
- Ex test set of 10,000 points and 309 are misclassified => Error rate 3.09%
### Improving Nearest Neighbor
- To classify a new point:
  - Find the k nearest neighbors in the training set
  - Return the most common label amongst them
    - k = 1 : test error% 3.09
    - k = 3 : test error% 2.94
    - k = 5 : test error% 3.13
### Excercise

## LOOCV - Leave-one-out cross-validation
- LOOCV là một phương pháp cross-validation thường được sử dụng để đánh giá một thuật toán học máy. Trong phương pháp này, ta sẽ xây dựng một mô hình trên tất cả các điểm dữ liệu ngoại trừ một điểm, sau đó sử dụng mô hình này để dự đoán nhãn cho điểm bị loại bỏ. Quá trình này được lặp lại cho tất cả các điểm dữ liệu, và ta tính tỷ lệ các dự đoán sai như một ước lượng cho tỷ lệ lỗi của thuật toán.
- **Example**: 4-fold cross-validation
  - We decide to use 4-fold cross-validation to figure out the right value of  to choose when running -nearest neighbor on a data set of size 10,000. When checking a particular value of , we look at four different training sets. What is the size of each of these training sets?

- To determine the size of each training set, we need to first calculate the size of each fold:
    - Size of each fold = Total size of data set / Number of folds
    - Size of each fold = 10,000 / 4
    - Size of each fold = 2,500

- Therefore, the size of each fold is 2,500. Since we are using three folds as the training set, the size of each training set is:
    - Size of each training set = Size of each fold * (Number of folds - 1)
    - Size of each training set = 2,500 * (4 - 1)
    - Size of each training set = 7,500

- Therefore, the size of each training set is 7,500, and the size of the validation set is 2,500 in 4-fold cross-validation.

- **Exercise**: 
- x = (1,2,3,4) in R4. Compute below:
  - L1 norm => ||x||1 = |1| + |2| + |3| + |4| = 1 + 2 + 3 + 4 = 10
  - L2 norm => ||x||2 = sqrt(1^2 + 2^2 + 3^2 + 4^2) = sqrt(30)
  - L-infinity norm => ||x||infinity = max{|1|, |2|, |3|, |4|} = 4

## k-NN
- k-NN - k-nearest neighbors: dựa trên việc xác định k điểm gần nhất (theo một khoảng cách được xác định trước) đến điểm dữ liệu đang xét, và sử dụng các nhãn của các điểm này để dự đoán nhãn của điểm đang xét. Thuật toán này thường được sử dụng cho các bài toán phân loại, nhưng cũng có thể được sử dụng cho các bài toán hồi quy
- **Excercise**:
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231743942-7fa4d623-d750-4afd-ba38-4ece5e6f0cf9.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231747621-cc115035-fb8c-4017-9919-265017fe503a.png">


## 1.4 Distance Functions for Machine Learning
### Mesuaring distance in Rm 
For P>=1 , lP distance:

    〖∥x- z∥〗_p  =〖( ∑_(i=1)^m▒〖    〖(xi- zi)〗^p  〗  )〗^(1/p)
    
P = 2, Euclidean distance 

     〖∥x- z∥〗_2  =√(∑_(i=1)^m▒〖    〖(xi- zi)〗^2  〗)
P = ∞,

    〖∥x- z∥〗_∞     = max_i⁡|x_i-z_i|
---
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231709216-73f1117e-ed75-4b54-8684-093394df7d82.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231709771-d14f5a52-4352-4176-88f8-1d2b5b50e813.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231711947-5b59a54f-184f-4727-9218-6f63570ab566.png">

#### Metric Space

<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231720483-de691fe2-d81e-47ec-b67f-6a6f580e16d3.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231722913-c3c5fedd-e666-4f11-bce4-4f181527b558.png">

### Distance Function
- Example: d(x,y) = # section, deletion, subsitution to get from x to y => yes, this is metric space
- Edit distance:
    - Edit distance là số lần các phép chèn, xóa hoặc thay thế một ký tự cần thiết để chuyển đổi một chuỗi thành chuỗi khác. Ví dụ, để chuyển đổi từ "dog" thành "cat", ta có thể thực hiện các phép thay thế "d" thành "c" và "g" thành "t", hoặc chèn "c" và "a" và xóa "o" và "g". Edit distance của hai chuỗi này là 3.
    - Sử dụng edit distance để xác định khoảng cách giữa hai chuỗi trong không gian metric này, ta có thể định nghĩa d(x, y) là edit distance giữa hai chuỗi x và y. Khoảng cách này sẽ thỏa mãn các điều kiện trong quy tắc metric space, đảm bảo rằng nếu x = y, thì d(x, y) = 0, và d(x, y) luôn là một số không âm. Khoảng cách d(x, y) cũng thỏa mãn tính đối xứng (symmetry) và bất đẳng thức tam giác (triangle inequality) như đã được nêu trong quy tắc metric space. 
- Hamming distance:
    - Hamming distance là một đo lường khoảng cách giữa hai chuỗi có cùng độ dài bằng cách đếm số lượng vị trí khác nhau giữa chúng. Cụ thể, nếu ta có hai chuỗi A và B cùng độ dài n, thì Hamming distance giữa chúng được định nghĩa là số lượng các vị trí i (0 <= i < n) mà ký tự tại vị trí i trong chuỗi A khác với ký tự tại vị trí i trong chuỗi B.
    - Ví dụ, nếu ta có hai chuỗi "101010" và "111000" có độ dài 6, thì Hamming distance giữa chúng sẽ là 3, bởi vì có ba vị trí tương ứng với các ký tự khác nhau: vị trí thứ 2, 4 và 5.
    - Hamming distance thường được sử dụng trong các ứng dụng liên quan đến mã hóa, kiểm tra lỗi và xử lý tín hiệu số. 

<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231732478-70b86de6-e5cc-4039-8356-76dbac4d23d3.png">

## 1.5 A Host of Prediction Problems
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231734330-8d1a6edd-3540-4cf0-8d32-7c216f77602b.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/231735072-64d7c1a1-dea7-4682-bf91-110a35906fe3.png">

## Algorithm
- The difference between algorithms and machine learning
**IT IS TRUE THAT **A key difference between algorithms and machine learning is that an algorithm designer provides a clearly defined process for mapping an input to an output, whereas a person designing a classifier does not need to provide a clearly defined process for mapping inputs to outputs.
- Discrete: rời rạc
- Các mô hình:
  - Classification: Phân loại, output space của class là rời rạc (descreate)
  - Regression: output space của re là liên tục (Continuous)
  - Probability estimation output space của pro là Probability Values as value in [0,1]
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/232182707-182dab73-dda6-4dc8-a7a3-7dd68c80b17f.png">
