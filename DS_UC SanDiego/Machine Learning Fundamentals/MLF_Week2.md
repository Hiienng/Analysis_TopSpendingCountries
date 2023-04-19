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
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233092693-cc66e04e-e2d6-4a6c-b753-dbd066dd150e.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233093307-993efc0d-34d3-47eb-a7f4-c870a3ec965a.png">
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233095189-481c9ac3-0528-4f87-ab2b-a9159f1203c2.png">



<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233081653-aacecbd0-16f4-446e-8e4c-33f5047eca2c.png">
- Explanation: 
    - If the first roll is a 6, then there are 6 possible outcomes for that roll (namely, rolling a 1, 2, 3, 4, 5, or 6). We need to determine the number of those outcomes that result in a sum of 10 when the second die is rolled.
    - Out of the six possible outcomes for the first roll (which is a 6), only one of them results in a sum of 10 when the second die is rolled (namely, rolling a 4). Therefore, the probability of rolling a sum of 10 given that the first roll is a 6 is:
    - P(sum is 10 | first roll is 6) = 1/6
<img width="700" alt="image" src="https://user-images.githubusercontent.com/89530538/233083367-09c7fc0d-7504-4f31-bd67-4391714a50fa.png">

### 2.3 Generative Modeling in One Dimension
### 2.4 Probability Review II: Random Variables, Expectation, and Variance
### 2.5 Probability Review III: Measuring Dependence
### 2.6 Two Dimensional Generative Modeling with the Bivariate Gaussian

## Week 3: Linear algebra basics, the multivariate Gaussian, and more generative modeling
## Week 4: Linear regression and logistic regression
## Week 5: Optimization
## Week 6: Support vector machines
## Week 7: Beyond linear prediction: kernel methods, decision trees, boosting, random forests
## Week 8: Clustering
## Week 9: Informative projections
## Week 10: Deep learning
