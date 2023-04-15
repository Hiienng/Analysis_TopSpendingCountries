# Machine Learning with Python-From Linear Models to Deep Learning
## Unit 0 Vectors, Planes, and Optimization
### Project 0
#### 5. Exercise - Neutral Netwwork
Here, we will write a function neural_network, which will apply a neural network operation with 2 inputs and 1 output and a given weight matrix.
**Available Functions:** You have access to the NumPy python library as np
Your function should take two arguments: inputs and weights, two NumPy arrays of shape (2,1) and should return a NumPy array of shape (1,1), the output of the neural network. Do not forget the tanh activation.
**Grader note**: If the grader appears unresponsive and displays “Processing", it means (most likely) it has crashed. Please resubmit your answers, and leave a message in the forum and we will work on fixing it as soon as possible.

        def neural_network(inputs, weights):
            """
             Takes an input vector and runs it through a 1-layer neural network
             with a given weight matrix and returns the output.

             Arg:
               inputs - 2 x 1 NumPy array
               weights - 2 x 1 NumPy array
             Returns (in this order):
               out - a 1 x 1 NumPy array, representing the output of the neural network
            """
            wT = np.transpose(weights)
            prod = np.matmul(wT, inputs)
            out = np.tanh(prod)
            return (out)
            # Alternatively:
            # return np.tanh(weights.T @ inputs)
            # or even:
            # return np.tanh(np.dot(inputs.T, weights))

#### 6. Vectorize function
##### Scalar function
![image](https://user-images.githubusercontent.com/89530538/220587527-c9c8f84d-166f-45f3-a11d-bba363103edc.png)


        def scalar_function(x, y):
            """
            Returns the f(x,y) defined in the problem statement.
            """
            if x<y:
                f_x = x*y
            else:
                f_x = x/y
            return f_x
            x=3
            y=2
            scalar_function(x, y)
##### Vector function
![image](https://user-images.githubusercontent.com/89530538/220587968-1a9e2d4a-b1e3-48eb-80ff-cbb15a04190c.png)

        def vector_function(x, y):
            """
            Make sure vector_function can deal with vector input x,y 
            """
            vector_function = np.vectorize(scalar_function)
            return vector_function(x, y)
#### 8. Debugging exercise

        def get_sum_metrics(predictions, metrics = None):
            if metrics is None:
                metrics = []
            for i in range(0,3):
                f = lambda x, i=i: x + i
                metrics.append(f)
            sum_metrics = 0
            for metric in metrics:
                sum_metrics += metric(predictions)
            return sum_metrics
or,

        def get_sum_metrics(prediction, metrics=None):
            if not metrics:
                metrics = []
            for i in range(3):
                metrics.append(gen_add_i(i))

            sum_metrics = 0
            for metric in metrics:
                sum_metrics += metric(prediction)

            return sum_metrics

        def gen_add_i(i):
            return lambda x: x + i

## Unit 1 Linear Classifiers and Generalizations
At the end of this lecture, you will be able to
- understand the goal of machine learning from a movie recommender example
- understand elements of supervised learning, and the difference between the training set and the test set
- understand the difference of classification and regression - two representative kinds of supervised learning
### 5. A Concrete Example of a Supervised Learning Task

