import tensorflow as tf

# The ways tensorflow works is nothing but graph theory
# All the nodes are called as ops or Operations
# Operation may input zero or many tensors
# Where tensors are n dimentional array or list 
# Rank, shape and dimention are properties of a tensor
# While using tensorflow there are two steps
# Construction phase and exection phase

# ********************
# Construction phase
# ********************

# Defining constant op 
# Defining some inputs
mat1 = tf.constant([[3,3])
mat2 = tf.Variable([[3],[3]],name="spidy")
bias = tf.constant([[3],[9]]) 

# Defining some Operations
# Adding bias to mat2
spidy_add = tf.add(mat2,bias)
# Updating the variable using assign method
spidy_update = tf.assign(mat2,spidy_add)

 
# Defining matrix multiplication op
product = tf.matmul(mat1,mat2)

# initialize all variables object
init_var = tf.initialize_all_variables()

# Defining placehoders for playing with feed
mat3 = tf.placeholder("float",shape=(1,2))
mat4 = tf.placeholder("float",shape=(2,1))
product2 = tf.matmul(mat3,mat4)




# *******************
# Execution phase
# *******************

# Session is an environment in which the graph runs
# Session has to closed for releasing the resources
# or With can be used to close the session after running it
with tf.Session() as sess:
	#merged_summary_op = tf.merge_all_summaries()
	#summary_writer = tf.train.SummaryWriter('/tmp/mnist_logs', sess.graph)
	# Should initialize the varibles first
	sess.run(init_var)
	# updating and running
	for _ in range(3):
		# Running the product between mat1 and mat2
		print sess.run(product)
		# Updating mat2 matrix by adding a bias matrix to it
		sess.run(spidy_update)

	for _ in range(3):	
		# Or to run them simultaneously use fetch
		# this command provides us with list of numpy arrays
		print sess.run([product,spidy_update])

	for _ in range(3):
		# Or to temperoryly feed the placeholders with an tensor	
		print sess.run(product2, feed_dict={mat3: [[2,10]],mat4: [[10],[2]]})
		

