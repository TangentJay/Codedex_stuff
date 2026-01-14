x = [False, True, '2', 3.0]
print(type(x))


print(round(1.335,4))
# import random
# r=0
# while r < 50:
#     print('roll to 50')
#     r=random.randint(1,50)
   
#     print(r)

b=[4,77,89,23,56,59]
print(sorted(b,reverse=True))
#key parameter sort by len example
s=('bob','jane','lake','eve','zuri','jayro')
print(sorted(s))

#11/8/2025 11:59 Am
grid_size = 10
import matplotlib.pyplot as plt
f, axarr = plt.subplots(grid_size, grid_size)
for i in range(grid_size):
    for j in range(grid_size):
        ax = axarr[i,j]
        ax.imshow(train_images[i * grid_size + j], cmap='gray')
