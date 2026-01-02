
import random
import matplotlib.pyplot as plt
random.seed(7)

color_list  = ['-r', 'm-', 'y-', 'c-', 'b-', 'g-']
color_index = 0

def show_learning_new(w):
	global color_index
	print('w0 =', '%5.2f' % w[0], ', w1 =', '%5.2f' % w[1], ', w2 =', '%5.2f' % w[2])

	if color_index == 0:
		plt.plot([1.0], [1.0], 'b_', markersize=12)
		plt.plot([-1.0, 1.0, -1.0], [1.0, -1.0, -1.0], 'r+', markersize=12)
		plt.axis([-2, 2, -2, 2])
		plt.xlabel('x1')
		plt.ylabel('x2')
	x = [-2.0, 2.0]
	if abs(w[2])  < 1e-5:
		y = [-w[1]/(1e-5)*(-2.0)+(-w[0]/(1e-5)),-w[1]/(1e-5)*(2.0)+(-w[0]/(1e-5))]
	else:
		y = [-w[1]/w[2]*(-2.0)+(-w[0]/w[2]),-w[1]/w[2]*(2.0)+(-w[0]/w[2])]

	print("Running plot!")
	plt.plot(x, y, color_list[color_index])
	if color_index < (len(color_list) -1):
		print("increase color index")
		color_index += 1
def show_learning(w):
	print('w0 =', '%5.2f' % w[0], ', w1 =',  '%5.2f' % w[1], ', w2 =', '%5.2f' % w[2])

def compute_output(w, x):
	z = 0.0
	for i in range(len(w)):
		z += x[i] * w[i]
	if z < 0:
		return -1
	else:
		return 1

LEARNING_RATE = 0.1
index_list = [0,1,2,3]
x_train = [(1.0, -1.0, -1.0), (1.0, -1.0, 1.0), (1.0, 1.0, -1.0), (1.0, 1.0, 1.0)]
y_train = [1.0, 1.0, 1.0, -1.0]

w = [0.2, -0.6, 0.25]

show_learning_new(w)
show_learning(w)


def perceptron():
	ITERATIONS = 1
	all_correct = False
	while not all_correct:
		all_correct = True
		random.shuffle(index_list)
		print("Updated index_list:", index_list)
		for i in index_list:
			x = x_train[i]
			y = y_train[i]
			p_out = compute_output(w, x)

			print("Current value: ", i, " Percepton value: ", p_out, "Truth value: ", y, "ITERATION: ", ITERATIONS)

			if y != p_out:
				for j in range(0, len(w)):
					w[j] += (y * LEARNING_RATE * x[j])
				all_correct = False
				show_learning_new(w)
		ITERATIONS +=1
		print("\n")
perceptron()

#show_learning_new(w)

x_test = [1.0,-1.0,1.0]
p_test = compute_output(w, x_test)

print("Testing with values: ", x_test)
print("Result is: ", p_test)


x_second_test = [1.0, -1.0, 0.0]
p_second_test = compute_output(w, x_second_test)

print("Testing with values: ", x_second_test)
print("Result is: ", p_second_test)
plt.show()
