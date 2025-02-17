import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.


# Task 1: Compute Output Size for 1D Convolution
# Instructions:
# Write a function that takes two one-dimensional numpy arrays (input_array, kernel_array) as arguments.
# The function should return the length of the convolution output (assuming no padding and a stride of one).
# The output length can be computed as follows:
# (input_length - kernel_length + 1)

# Your code here:
# -----------------------------------------------

def compute_output_size_1d(input_array, kernel_array):
    return len(input_array) - len(kernel_array) + 1

# -----------------------------------------------
# Example:
input_array = np.array([1, 2, 3, 4, 5])
kernel_array = np.array([1, 0, -1])
print(compute_output_size_1d(input_array, kernel_array))


# Task 2: 1D Convolution
# Instructions:
# Write a function that takes a one-dimensional numpy array (input_array) and a one-dimensional kernel array (kernel_array)
# and returns their convolution (no padding, stride 1).

# Your code here:
# -----------------------------------------------

def convolve_1d(input_array, kernel_array):
    # Tip: start by initializing an empty output array (you can use your function above to calculate the correct size).
    # Then fill the cells in the array with a loop.
    length = compute_output_size_1d(input_array, kernel_array)
    output = []
    for i in range(length):
        conv_res = np.sum(input_array[i:i+len(kernel_array)]*kernel_array)
        output.append(conv_res)
    return output

# -----------------------------------------------
# Another tip: write test cases like this, so you can easily test your function.
input_array = np.array([1, 2, 3, 4, 5])
kernel_array = np.array([1, 0, -1])
print(convolve_1d(input_array, kernel_array))

# Task 3: Compute Output Size for 2D Convolution
# Instructions:
# Write a function that takes two two-dimensional numpy matrices (input_matrix, kernel_matrix) as arguments.
# The function should return a tuple with the dimensions of the convolution of both matrices.
# The dimensions of the output (assuming no padding and a stride of one) can be computed as follows:
# (input_height - kernel_height + 1, input_width - kernel_width + 1)

# Your code here:
# -----------------------------------------------

def compute_output_size_2d(input_matrix, kernel_matrix):
    input_height = input_matrix.shape[0]
    input_width = input_matrix.shape[1]
    kernel_height = kernel_matrix.shape[0]
    kernel_width = kernel_matrix.shape[1]
    return (input_height - kernel_height + 1, input_width - kernel_width + 1)

# -----------------------------------------------

# Task 4: 2D Convolution
# Instructions:
# Write a function that computes the convolution (no padding, stride 1) of two matrices (input_matrix, kernel_matrix).
# Your function will likely use lots of looping and you can reuse the functions you made above.

# Your code here:
# -----------------------------------------------
def convolute_2d(input_matrix, kernel_matrix):
    # Tip: same tips as above, but you might need a nested loop here in order to
    # define which parts of the input matrix need to be multiplied with the kernel matrix.
    
    dims = compute_output_size_2d(input_matrix, kernel_matrix)
    output = np.zeros(dims)
    kernel_height = kernel_matrix.shape[0]
    kernel_width = kernel_matrix.shape[1]
    for row in range(dims[0]):
        for col in range(dims[1]):
            input_patch = input_matrix[row:row+kernel_height, col:col+kernel_width]
            conv = np.sum(input_patch*kernel_matrix)
            output[row, col] = conv
    return output

# -----------------------------------------------