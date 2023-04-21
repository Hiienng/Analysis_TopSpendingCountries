## Week 2: Probability basics and generative modeling
### 2.1 The Generative Approach to Classification
- Generative approach: Generative approach trong machine learning là một phương pháp giúp huấn luyện một **mô hình xác suất** để ước lượng xác suất của các lớp và sử dụng chúng để phân loại các dữ liệu mới.
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233060739-891dfe6f-631a-4da3-ba88-6edc6e9fa4e2.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233059540-891b06f7-5ac4-4614-a176-6cafbfeda084.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233061323-a09822d3-4b0c-4999-92f5-88ad63902861.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233061376-c3bdeb91-c647-4c14-acf4-e2721d0c06a0.png">

### 2.2 Probability Review I: Probability Spaces, Events, and Conditioning
- Probability Space
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233081030-1004e011-cc27-4b12-a187-65c0891676f2.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233081470-c63425a6-ac70-4804-acf9-3d65e8660c44.png">

- Events
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233081266-b935e919-be33-4a59-9e45-e1d59fe7f5bc.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233083574-39977a86-a395-4468-b782-4a6624bc144e.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233085190-ce0f2bde-9038-4a31-837b-feb1dc4978d4.png">
- Explanation: The difference of their faces is 3: chênh lệch giá trị giữa hai mặt = 3. Như vậy có 6 trường hợp trên 36 trường hợp có thể xảy ra
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233085538-da9c6e94-1dbb-4e8e-a408-de06410e5471.png">

- Multiple events
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233093745-e8a7ab51-7b09-48cd-bc9e-7c1a7edd22b8.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233128455-f7227063-ab7f-435e-b1e5-494440773277.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233092693-cc66e04e-e2d6-4a6c-b753-dbd066dd150e.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233093307-993efc0d-34d3-47eb-a7f4-c870a3ec965a.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233095189-481c9ac3-0528-4f87-ab2b-a9159f1203c2.png">

<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233100584-2c8dff55-8b93-4c4e-a977-56eace78bfaf.png">
- Explanation: Đề bài yêu cầu tìm sác xuất lấy được túi Redx3 trong đó có 1 túi 3 banh đỏ (Redx3) và 2 túi loại 1 xanh dương, 1 đỏ, 1 xanh lá(non-Redx3). Biết trước rằng khi lấy 1 trái từ 1 túi random, sau đó bỏ trái banh ấy vào lại túi rồi lấy một quả random ra, và hai quả này đều màu đỏ.<space><space>
    - Giải đề bài theo phương pháp Baye's Rules.  
        - A: Sự kiện lấy được túi Redx3 \\
        - B: Sự kiện hai quả banh đỏ được lấy ra \\
        - Xác suất lấy được túi Redx3: P(A\cup B) = 1/3 \\
        - Xác suất tất cả sự kiện : P(All) = P(Redx3, 2 Red balls) + P(non-Redx3, 2 Red balls) = 1/3 x 1 + 2/3 x (1/3 x 1/3) = 0.818 \\
    - Giải theo cách khác \\
        - Let the event of red balls be E. \\
            - The probability of 2 red balls from first non-redx3 bag is  1/3 x 1/3 = 1/9 \\
            - The probability of 2 red balls from second non-redx3 bag is 1/9 \\
            - The probability of 2 red balls from Redx3 bag is 1 \\
        - The bag with the 3 red balls is (1/3 x 1) / (1/3 x 1/9 + 1/3 x 1/9 + 1/3 x1) = 0.818 \\


<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233081653-aacecbd0-16f4-446e-8e4c-33f5047eca2c.png">
- Explanation: \\
    - If the first roll is a 6, then there are 6 possible outcomes for that roll (namely, rolling a 1, 2, 3, 4, 5, or 6). We need to determine the number of those outcomes that result in a sum of 10 when the second die is rolled. \\
    - Out of the six possible outcomes for the first roll (which is a 6), only one of them results in a sum of 10 when the second die is rolled (namely, rolling a 4). Therefore, the probability of rolling a sum of 10 given that the first roll is a 6 is: \\
    - P(sum is 10 | first roll is 6) = 1/6
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233083367-09c7fc0d-7504-4f31-bd67-4391714a50fa.png">

### 2.3 Generative Modeling in One Dimension

<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233599092-abe1f915-7585-4b3c-83f7-d58ce2f99faa.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233599642-d124cdfe-2c52-4e78-8394-de22bd68c264.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233599922-e6def5e2-ddd0-4e29-9c2b-213130e222cd.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233600200-43f02cd7-b644-4a84-bc72-9b155e6e5dd5.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233600692-cb30fc24-3c77-49b7-bfed-7ac0eb525ff3.png">
Explaination:   
    - Nếu nồng độ cồn = 15 => Bình rượu có khả năng là loại rượu 1   
    - Nếu nồng độ cồn = 11 => Bình rượu có khả năng là loại rượu 2 \\
    - Nếu nồng độ cồn = 12.5 => Bình rượu có thể là 2 hoặc 3 dựa trên P (density). Tuy nhiên trong 3 bình thì tỷ lệ xác suất của Loại 2 cao hơn nên dự đoán theo phương pháp generative sẽ ra loại 2 \\
 
- TEST ERROR
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233601751-47a5f740-0803-4176-82b8-b1a9f20bf679.png">
- MODEL này hiện tại chỉ dựa trên một feature là Nồng độ cồn, do đó ta thấy được kết quả lỗi khá lớn như trên. Khi mô hình được chạy áp dụng với nhiều feature hơn sẽ giúp kết quả của mô hình chính xác hơn

### 2.4 Probability Review II: Random Variables, Expectation, and Variance
#### Topic cover:
#### Random Variables:
- Random Variables: RVs là các biến số mà giá trị của chúng phụ thuộc vào kết quả của một thử nghiệm ngẫu nhiên. Ví dụ RVs có thể là 0, 1 hoặc 2, tùy thuộc vào số lần xuất hiện của mặt sấp khi tung một đồng xu đồng chất 2 lần
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233604316-4819247c-6d3b-4a0f-bc24-28a30aa878d3.png">

#### Expected value:
- Expected value là E(X), trong đó X là một biến ngẫu nhiên. 
- Property of E(X): Các tính chất quan trọng của expected value bao gồm: 
    - Tính tuyến tính: E(aX + bY) = aE(X) + bE(Y), với a và b là các hằng số và X, Y là các biến ngẫu nhiên.
    - Phép chuyển đổi đổi biến số: Nếu Y = g(X) là một hàm số của X, thì E(Y) = E(g(X)) = ∑g(x)*P(X=x), với x là các giá trị có thể của X và P(X=x) là xác suất tương ứng. 
    - Tính không âm: E(X) >= 0, với X là một biến ngẫu nhiên không âm. 
    - Tính đồng nhất: Nếu X là một biến ngẫu nhiên có cùng phân phối với Y, tức là P(X=x) = P(Y=x) cho mọi giá trị có thể của X và Y, thì E(X) = E(Y).
    - Tính đồng nhất của trung bình: Nếu X1, X2, ..., Xn là các biến ngẫu nhiên độc lập và có cùng phân phối, thì E(X1 + X2 + ... + Xn) = nE(X1).
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233605374-a8099789-d075-470b-b9de-9fee6f20de6a.png">

#### Variance:
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233606213-93b9e3cb-8ae5-4108-86e3-859e3c10f9d8.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233611616-ac8b5797-a8f9-466f-b32d-5d76a3831fbe.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233611875-6e725101-719f-4661-ad3b-0cad57e5fe6f.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233612428-262b7c5f-4703-440f-b105-01a2f754a28b.png">

#### Property of Variance
<img width="500" alt="image" src="https://user-images.githubusercontent.com/89530538/233612082-e08834df-0f37-447a-a7c2-2bcad19d4e26.png">


### 2.5 Probability Review III: Measuring Dependence
#### Topic cover:
    - When are two random variable independent?
    - Qualitatively assessing dependence
    - Quantifying dependence: covarience and correlation
#### Details:
- Random variable X and Y independent if `Pr(X = x, Y = y) =  Pr(X = x)Pr(Y = y)`
- Example 1: Pick out a card with X = suit and Y = number, then `Pr(X = heart, Y = 6) = 1/52` equal `Pr(X = heart) = 1/4` x `Pr(Y = 6) = 1/13` so X and Y is independent
- Example 2: Toss a coin 10 times with X = # Heads and Y = Value of Last toss, then toss 10 time and there are 10 Heads but the last toss is Tails: `Pr(X = 10, Y = Tails) = 0` while `Pr(X = 10) = 1/2^10` and `Pr(Y = Tails) = 1/2`
- Example 3: X, Y in range {-1,0,1} and the probability is:
    
| . | Y | . | . | . |
|-------|-------|-------|-------|-------|
| . |   | -1 | 0 | 1 |
| X | -1 | .4  | .16  | .24 |
| . | 0 | .05 | .02 | .03 |
| . | 1 | .05 | .02 | .03 |


    
### 2.6 Two Dimensional Generative Modeling with the Bivariate Gaussian

## Week 3: Linear algebra basics, the multivariate Gaussian, and more generative modeling
## Week 4: Linear regression and logistic regression
## Week 5: Optimization
## Week 6: Support vector machines
## Week 7: Beyond linear prediction: kernel methods, decision trees, boosting, random forests
## Week 8: Clustering
## Week 9: Informative projections
## Week 10: Deep learning
