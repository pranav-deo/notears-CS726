import numpy as np
import matplotlib.pyplot as plt
import argparse
import pandas

def plot_matrix(args):
	if args.W_path[-3:] == 'csv':
		W = np.loadtxt(args.W_path, delimiter=',')
	# elif args.X_path[:-3] == 'xls':
	else:
		W = pandas.read_excel(args.W_path)
		W = np.array(W)

	# W = np.clip(W,np.mean(W)-2,np.mean(W)+2)
	fig, axs = plt.subplots()
	psm = axs.pcolormesh(W, cmap=plt.cm.viridis)
	fig.colorbar(psm, ax=axs)
	plt.show()

def parse_args():
	parser = argparse.ArgumentParser(description='Visualize the adjacency matrix')
	parser.add_argument('--W_path', type=str, default='W_est.csv', help='p by p weighted adjacency matrix of estimated DAG in csv format')
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	args = parse_args()
	plot_matrix(args)