# MODEL LAB QUESTION PAPER - SIMPLE PYTHON PROGRAMS
# SET 1 TO SET 8
# Run one question section at a time. Change sample values or uncomment input lines as needed.

import numpy as np

# ============================================================
# SET 1
# ============================================================

# SET 1 - Q1(a): Fibonacci population for first n months
def set1_q1_a():
    n = int(input("Enter number of months: "))
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# SET 1 - Q1(b): Multiplication table
def set1_q1_b():
    rate = int(input("Enter rate: "))
    for i in range(1, 11):
        print(rate, "x", i, "=", rate * i)

# SET 1 - Q1(c): Highest rent among three properties
def set1_q1_c():
    rents = [int(input("Enter rent: ")) for i in range(3)]
    print("Highest rent:", max(rents))

# SET 1 - Q2(a): Read CSV, inspect and fill missing values
def set1_q2_a():
    import pandas as pd
    df = pd.read_csv("transactions.csv")
    print(df.head())
    print(df.shape)
    print(df.dtypes)
    print(df.isnull().sum())
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["Amount"] = df["Amount"].fillna(df["Amount"].median())
    print(df.isnull().sum())

# SET 1 - Q2(b): Scale, standardize, remove outliers and plot
def set1_q2_b():
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import MinMaxScaler, StandardScaler

    df = pd.read_csv("transactions.csv")
    df["Amount"] = MinMaxScaler().fit_transform(df[["Amount"]])
    df["Age"] = StandardScaler().fit_transform(df[["Age"]])

    q1 = df["Amount"].quantile(0.25)
    q3 = df["Amount"].quantile(0.75)
    iqr = q3 - q1
    df = df[(df["Amount"] >= q1 - 1.5 * iqr) &
            (df["Amount"] <= q3 + 1.5 * iqr)]

    df["Date"] = pd.to_datetime(df["Date"])
    df.groupby("Category")["Amount"].sum().plot(kind="bar")
    plt.title("Spending by Category")
    plt.show()

    df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum().plot(kind="line")
    plt.title("Monthly Spending")
    plt.show()

# SET 1 - Q3(a): Combine four 2x2 matrices into one 4x4 matrix
def set1_q3_a():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = np.array([[9, 1], [2, 3]])
    d = np.array([[4, 5], [6, 7]])
    top = np.hstack((a, b))
    bottom = np.hstack((c, d))
    result = np.vstack((top, bottom))
    print(result)

# SET 1 - Q3(b): Reshape 12 values to 3x4 and cube
def set1_q3_b():
    a = np.arange(1, 13)
    b = a.reshape(3, 4)
    print("Matrix:\n", b)
    print("Cubed:\n", b ** 3)

# SET 1 - Q3(c): Row and column totals
def set1_q3_c():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Row totals:", np.sum(a, axis=1))
    print("Column totals:", np.sum(a, axis=0))


# ============================================================
# SET 2
# ============================================================

# SET 2 - Q1(a): Generate heights and verify z-scores
def set2_q1_a():
    z = np.random.randn(1000)
    height = 170 + 8 * z
    z_score = (height - 170) / 8
    print("Mean:", np.mean(z_score))
    print("Standard deviation:", np.std(z_score))

# SET 2 - Q1(b): Exponential waiting times
def set2_q1_b():
    waiting = np.random.exponential(2, 1000)
    print("Simulated mean:", np.mean(waiting))

# SET 2 - Q1(c): Compare t and normal tails
def set2_q1_c():
    from scipy.stats import t, norm
    print("t probability:", t.sf(2, 10))
    print("Normal probability:", norm.sf(2))

# SET 2 - Q2(a): Prime PIN
def set2_q2_a():
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    n = int(input("Enter PIN: "))
    print("Prime" if is_prime(n) else "Not prime")

# SET 2 - Q2(b): Perfect number
def set2_q2_b():
    n = int(input("Enter number: "))
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    print("Perfect number" if total == n else "Not a perfect number")

# SET 2 - Q2(c): Runner-up score
def set2_q2_c():
    scores = [10, 20, 30, 40, 40, 30]
    scores = sorted(set(scores))
    print("Runner-up:", scores[-2])

# SET 2 - Q3(a): Matrix rank and row dependency
def set2_q3_a():
    a = np.array([[1, 2, 3], [2, 4, 6], [1, 1, 1]])
    rank = np.linalg.matrix_rank(a)
    print("Rank:", rank)
    print("Rows are linearly dependent" if rank < a.shape[0]
          else "Rows are linearly independent")

# SET 2 - Q3(b): Show AB is not equal to BA
def set2_q3_b():
    a = np.array([[0, -1], [1, 0]])
    b = np.array([[2, 0], [0, 3]])
    print("AB:\n", a @ b)
    print("BA:\n", b @ a)
    print("AB equals BA:", np.array_equal(a @ b, b @ a))

# SET 2 - Q3(c): Block diagonal and determinant
def set2_q3_c():
    from scipy.linalg import block_diag
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[2, 0], [0, 3]])
    c = block_diag(a, b)
    print("Block matrix:\n", c)
    print("Determinant of big matrix:", np.linalg.det(c))
    print("Product of determinants:", np.linalg.det(a) * np.linalg.det(b))


# ============================================================
# SET 3
# ============================================================

# SET 3 - Q1(a): Print words containing a digit
def set3_q1_a():
    text = input("Enter sentence: ")
    for word in text.split():
        if any(ch.isdigit() for ch in word):
            print(word)

# SET 3 - Q1(b): Vowels uppercase, consonants lowercase
def set3_q1_b():
    text = input("Enter text: ")
    result = ""
    for ch in text:
        if ch.lower() in "aeiou":
            result += ch.upper()
        else:
            result += ch.lower()
    print(result)

# SET 3 - Q1(c): First and last letter of every word
def set3_q1_c():
    title = input("Enter project title: ")
    result = ""
    for word in title.split():
        result += word[0].upper() + word[-1].upper()
    print("Acronym:", result)

# SET 3 - Q2(a): Central 2x2 region and last column
def set3_q2_a():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8],
                  [9, 10, 11, 12], [13, 14, 15, 16]])
    print("Central 2x2:\n", a[1:3, 1:3])
    print("Last column:\n", a[:, -1])

# SET 3 - Q2(b): Multiply 2x3 and 3x2 matrices
def set3_q2_b():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[1, 2], [3, 4], [5, 6]])
    print(a @ b)

# SET 3 - Q2(c): Multiply random 2x2 integer matrices (seed 7)
def set3_q2_c():
    np.random.seed(7)
    a = np.random.randint(1, 10, (2, 2))
    b = np.random.randint(1, 10, (2, 2))
    print("A:\n", a)
    print("B:\n", b)
    print("Product:\n", a @ b)

# SET 3 - Q3(a): Count words longer than 6 characters
def set3_q3_a():
    text = input("Enter paragraph: ")
    words = text.split()
    count = sum(1 for word in words if len(word) > 6)
    print("Long words count:", count)

# SET 3 - Q3(b): Count tokens containing repeated digits
def set3_q3_b():
    tokens = input("Enter tokens separated by spaces: ").split()
    count = 0
    for token in tokens:
        digits = [ch for ch in token if ch.isdigit()]
        if len(digits) != len(set(digits)):
            count += 1
    print("Tokens with repeated digits:", count)

# SET 3 - Q3(c): Right-angle/Pythagorean triples
def set3_q3_c():
    limit = int(input("Enter limit: "))
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            for c in range(b + 1, limit + 1):
                if a*a + b*b == c*c:
                    print(a, b, c)


# ============================================================
# SET 4
# ============================================================

# SET 4 - Q1(a): Fibonacci numbers below n
def set4_q1_a():
    n = int(input("Enter limit: "))
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()

# SET 4 - Q1(b): Armstrong numbers in a range
def set4_q1_b():
    low = int(input("Enter lower limit: "))
    high = int(input("Enter upper limit: "))
    for n in range(low, high + 1):
        digits = str(n)
        total = sum(int(d) ** len(digits) for d in digits)
        if total == n:
            print(n)

# SET 4 - Q1(c): Merge lists without duplicates, keeping order
def set4_q1_c():
    a = ["a@mail.com", "b@mail.com"]
    b = ["b@mail.com", "c@mail.com"]
    result = list(dict.fromkeys(a + b))
    print(result)

# SET 4 - Q2(a): Random 3x3 matrix, sum, row sums and squares
def set4_q2_a():
    a = np.random.randint(1, 10, (3, 3))
    print("Matrix:\n", a)
    print("Total:", np.sum(a))
    print("Row sums:", np.sum(a, axis=1))
    print("Squares:\n", a ** 2)

# SET 4 - Q2(b): 4x4 block matrix
def set4_q2_b():
    i = np.eye(2, dtype=int)
    z = np.zeros((2, 2), dtype=int)
    bottom_right = 2 * i
    top = np.hstack((i, z))
    bottom = np.hstack((z, bottom_right))
    print(np.vstack((top, bottom)))

# SET 4 - Q2(c): Element-wise square and cube
def set4_q2_c():
    a = np.array([[1, 2], [3, 4]])
    print("Square:\n", a ** 2)
    print("Cube:\n", a ** 3)

# SET 4 - Q3(a): Simulate Poisson probability and compare exact value
def set4_q3_a():
    from scipy.stats import poisson
    data = np.random.poisson(4, 100000)
    print("Simulated P(X > 6):", np.mean(data > 6))
    print("Exact P(X > 6):", poisson.sf(6, 4))

# SET 4 - Q3(b): Most frequent number of heads in 10 tosses
def set4_q3_b():
    results = np.random.binomial(10, 0.5, 1000)
    values, counts = np.unique(results, return_counts=True)
    print("Most frequent heads:", values[np.argmax(counts)])

# SET 4 - Q3(c): Beta samples and expected probability
def set4_q3_c():
    samples = np.random.beta(2, 5, 1000)
    print("Sample mean:", np.mean(samples))
    print("Theoretical mean:", 2 / (2 + 5))


# ============================================================
# SET 5
# ============================================================

# SET 5 - Q1(a): Extract rows 1 to 2 and columns 1 to 2
def set5_q1_a():
    a = np.arange(1, 17).reshape(4, 4)
    print(a[1:3, 1:3])

# SET 5 - Q1(b): Reshape 9 values to 3x3 and cube
def set5_q1_b():
    a = np.arange(1, 10).reshape(3, 3)
    print("Image:\n", a)
    print("Cubed:\n", a ** 3)

# SET 5 - Q1(c): 4x4 block matrix
def set5_q1_c():
    i = np.eye(2, dtype=int)
    z = np.zeros((2, 2), dtype=int)
    x = np.ones((2, 2), dtype=int) * 2
    y = np.ones((2, 2), dtype=int) * 3
    print(np.block([[i, z], [x, y]]))

# SET 5 - Q2(a): Longest strictly increasing continuous period
def set5_q2_a():
    values = [2, 3, 5, 4, 6, 7, 8, 1]
    longest = current = 1
    for i in range(1, len(values)):
        if values[i] > values[i - 1]:
            current += 1
        else:
            current = 1
        longest = max(longest, current)
    print("Longest increasing length:", longest)

# SET 5 - Q2(b): Check circular rotation
def set5_q2_b():
    a = input("Enter first code: ")
    b = input("Enter second code: ")
    print("Circular rotation" if len(a) == len(b) and b in a + a
          else "Not a circular rotation")

# SET 5 - Q3(a): Generate sensor values lazily and standardize
def set5_q3_a():
    values = np.fromiter((np.random.randint(1, 1001) for _ in range(1000)),
                         dtype=float, count=1000)
    z = (values - np.mean(values)) / np.std(values, ddof=1)
    print("Mean:", np.mean(z))
    print("Sample standard deviation:", np.std(z, ddof=1))

# SET 5 - Q3(b): Broadcasting for final bill and highest revenue
def set5_q3_b():
    s = np.array([[100, 200, 300], [120, 220, 320],
                  [140, 240, 340], [160, 260, 360]], dtype=float)
    d = np.array([0.10, 0.05, 0.15])
    t = np.array([[0.05], [0.08], [0.06], [0.07]])
    billed = s * (1 - d) * (1 + t)
    print("Final billed amounts:\n", billed)
    totals = billed.sum(axis=1)
    print("Workgroup with maximum revenue:", np.argmax(totals) + 1)


# ============================================================
# SET 6
# ============================================================

# SET 6 - Q1(a): Unique scores in ascending order
def set6_q1_a():
    marks = [70, 80, 70, 90, 60, 80]
    print(sorted(set(marks)))

# SET 6 - Q1(b): Remove lowest and highest, reverse remaining
def set6_q1_b():
    marks = [70, 80, 60, 90, 75]
    marks.remove(min(marks))
    marks.remove(max(marks))
    print(marks[::-1])

# SET 6 - Q1(c): Sort a copy in descending order
def set6_q1_c():
    marks = [70, 80, 60, 90, 75]
    merit = marks.copy()
    merit.sort(reverse=True)
    print("Original:", marks)
    print("Merit list:", merit)

# SET 6 - Q2(a): Line plot of 100 random readings
def set6_q2_a():
    import matplotlib.pyplot as plt
    values = np.random.randint(1, 101, 100)
    plt.plot(range(1, 101), values, label="Stress")
    plt.xlabel("Sample index")
    plt.ylabel("Stress value")
    plt.legend()
    plt.show()

# SET 6 - Q2(b): Scatter plot of same readings
def set6_q2_b():
    import matplotlib.pyplot as plt
    values = np.random.randint(1, 101, 100)
    plt.scatter(range(1, 101), values, label="Stress")
    plt.xlabel("Sample index")
    plt.ylabel("Stress value")
    plt.legend()
    plt.show()

# SET 6 - Q2(c): Vertical and horizontal bar charts
def set6_q2_c():
    import matplotlib.pyplot as plt
    values = np.random.randint(1, 101, 100)
    plt.bar(range(1, 101), values, label="Stress")
    plt.xlabel("Sample index")
    plt.ylabel("Stress value")
    plt.legend()
    plt.show()
    plt.barh(range(1, 101), values, label="Stress")
    plt.xlabel("Stress value")
    plt.ylabel("Sample index")
    plt.legend()
    plt.show()

# SET 6 - Q3(a): Total sales
def set6_q3_a():
    sales = {"A": 60, "B": 45, "C": 80, "D": 55}
    print("Total sales:", sum(sales.values()))

# SET 6 - Q3(b): Brands with sales greater than 50
def set6_q3_b():
    sales = {"A": 60, "B": 45, "C": 80, "D": 55}
    result = {k: v for k, v in sales.items() if v > 50}
    print(result)

# SET 6 - Q3(c): Brand with maximum sales
def set6_q3_c():
    sales = {"A": 60, "B": 45, "C": 80, "D": 55}
    print("Top brand:", max(sales, key=sales.get))


# ============================================================
# SET 7
# ============================================================

# SET 7 - Q1(a): Average marks
def set7_q1_a():
    marks = [70, 80, 90, 60, 85]
    print("Average:", sum(marks) / len(marks))

# SET 7 - Q1(b): Function returns highest mark
def set7_q1_b():
    def highest(marks):
        return max(marks)
    print("Highest:", highest([70, 80, 90, 60, 85]))

# SET 7 - Q1(c): Count even marks
def set7_q1_c():
    marks = [70, 81, 90, 63, 84]
    count = sum(1 for x in marks if x % 2 == 0)
    print("Even marks count:", count)

# SET 7 - Q2(a): Monte Carlo estimate of pi using generator
def set7_q2_a():
    points = ((np.random.random(), np.random.random()) for _ in range(10000))
    inside = sum(1 for x, y in points if x*x + y*y <= 1)
    print("Estimated pi:", 4 * inside / 10000)

# SET 7 - Q2(b): Sliding windows and covariance
def set7_q2_b():
    values = np.random.random(200)
    windows = (values[i:i+10] for i in range(191))
    for window in windows:
        print(np.cov(window, window)[0, 1])

# SET 7 - Q2(c): Generate 500 values with fromiter
def set7_q2_c():
    values = np.fromiter((np.random.random() for _ in range(500)), count=500)
    print("Mean:", np.mean(values))
    print("Variance:", np.var(values))
    print("Median:", np.median(values))

# SET 7 - Q3(a): Alphabetic words in lowercase
def set7_q3_a():
    tokens = ["Hello", "AI123", "WORLD!", "Python"]
    result = [x.lower() for x in tokens if x.isalpha()]
    print(result)

# SET 7 - Q3(b): Reverse words longer than 4 characters
def set7_q3_b():
    text = input("Enter sentence: ")
    result = [word[::-1] for word in text.split() if len(word) > 4]
    print(result)

# SET 7 - Q3(c): First and last two-letter abbreviations
def set7_q3_c():
    tags = ["data", "AI", "science", "ML"]
    result = [x[0] + x[-1] for x in tags if len(x) >= 2]
    print(result)


# ============================================================
# SET 8
# ============================================================

# SET 8 - Q1(a): Multiple line plot
def set8_q1_a():
    import matplotlib.pyplot as plt
    years = [1, 2, 3, 4, 5]
    s1 = [40, 48, 55, 62, 70]
    s2 = [35, 42, 45, 50, 58]
    plt.plot(years, s1, marker="o", label="Series 1")
    plt.plot(years, s2, marker="s", label="Series 2")
    plt.xlabel("Academic year")
    plt.ylabel("Hiring count")
    plt.legend()
    plt.show()

# SET 8 - Q1(b): Pie chart
def set8_q1_b():
    import matplotlib.pyplot as plt
    labels = ["Tuition", "Rent", "Food", "Books"]
    values = [45, 25, 18, 12]
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Student Budget")
    plt.show()

# SET 8 - Q1(c): Bar chart
def set8_q1_c():
    import matplotlib.pyplot as plt
    departments = ["A", "B", "C", "D", "E"]
    visits = [18, 32, 24, 28, 15]
    plt.bar(departments, visits, label="Company visits")
    plt.xlabel("Department")
    plt.ylabel("Visits")
    plt.title("Company Visits by Department")
    plt.legend()
    plt.show()

# SET 8 - Q2(a): IDs appearing more than n/3 times
def set8_q2_a():
    ids = [1, 2, 3, 1, 1, 2, 1, 3, 3, 3]
    n = len(ids)
    result = [x for x in set(ids) if ids.count(x) > n / 3]
    print(result)

# SET 8 - Q2(b): Maximum product of any three numbers
def set8_q2_b():
    values = [-10, -10, 5, 2, 3]
    values.sort()
    product1 = values[-1] * values[-2] * values[-3]
    product2 = values[0] * values[1] * values[-1]
    print("Maximum product:", max(product1, product2))

# SET 8 - Q3(a): Eigenvalues, eigenvectors and orthogonality
def set8_q3_a():
    a = np.array([[2, 1], [1, 2]])
    values, vectors = np.linalg.eigh(a)
    print("Eigenvalues:", values)
    print("Eigenvectors:\n", vectors)
    print("Dot product:", np.dot(vectors[:, 0], vectors[:, 1]))

# SET 8 - Q3(b): Verify A v = lambda v
def set8_q3_b():
    a = np.array([[2, 1], [1, 2]])
    values, vectors = np.linalg.eig(a)
    for i in range(len(values)):
        v = vectors[:, i]
        print(np.allclose(a @ v, values[i] * v))

# SET 8 - Q3(c): Check whether matrix is singular
def set8_q3_c():
    a = np.array([[1, 2], [2, 4]])
    det = np.linalg.det(a)
    print("Determinant:", det)
    if np.isclose(det, 0):
        print("Matrix is singular; inverse does not exist")
    else:
        print("Inverse:\n", np.linalg.inv(a))


# ============================================================
# HOW TO RUN
# ============================================================
# 1. Save this file as model_lab_solutions.py
# 2. Run: python model_lab_solutions.py
# 3. To execute a question, remove the # from its function call below.
# Example:
# set2_q1_a()
# set3_q1_a()
#
# NumPy is needed for most matrix/statistics questions.
# Install if needed: pip install numpy pandas matplotlib scipy scikit-learn
