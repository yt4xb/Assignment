import numpy
if __name__ == '__main__':
	u = numpy.random.uniform(0,1,1)
	print u
	temp = (-(u*pow(1000,2)-u*pow(1,2)-pow(1000,2)))/(pow(1000,2)*pow(1,2))
	print temp
	x = pow(temp,-0.5)
	print x

