import numpy as np

r = int(input("Number of rows in reg_data: "))
c = int(input("Number of columns in reg_data: "))

print("Enter reg_data in a single line separated with comma: ")
reg_data = list(map(int, input().split()))

matrix = np.array(reg_data).reshape(r, c)
print(matrix)

# import numpy as np

# reg_data_r = int(input("Number of rows in reg_data: "))
# reg_data_c = int(input("Number of columns in reg_data: "))

# print("Enter reg_data in a single line separated with comma: ")
# reg_data = list(map(int, input().split()))

# cluster_data_r = int(input("Number of rows in cluster_data: "))
# cluster_data_c = int(input("Number of columns in cluster_data: "))

# print("Enter cluster_data in a single line separated with comma: ")
# cluster_data = list(map(int, input().split()))


# X = np.array(reg_data).reshape(reg_data_r, reg_data_c)
# print(X)

# Y = np.array(cluster_data).reshape(cluster_data_r, cluster_data_c)
# print(Y)
