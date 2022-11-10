import argparse

class BST:
	def __init__(self, arr):
		self.arr = arr
		self.len = len(arr)

	def validateInput(self):
		for i in self.arr:
			if not isinstance(i, int):
				return False 
			if i >= 10000: 
				return False 

			return True 

	def check(self):
		for i in range(self.len):
			x = 2*i + 1
			y = 2*i + 2
			if x < self.len and self.arr[i] < self.arr[x]:
				return False
			if y < self.len and self.arr[i] > self.arr[y]:
				return False

			return True

	def top(self):
		left = self.left()
		right = self.right()

		top = left[::-1] + right[1:]

		return top


	def left(self):
		i = 0
		left = []

		while i < self.len:
			left.append(self.arr[i])
			i = 2*i+1

		return left

	def right(self):
		i = 0
		right = []

		while i < self.len:
			right.append(self.arr[i])
			i = 2*i+2

		return right

	def bottom(self):
		l = self.len + 1

		return self.arr[l//2-1:]

	def height(self):
		return len(bin(self.len))-2

	def diameter(self):
		return self.top()


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='BST.', add_help=False)
	parser.add_argument('--file', '-f', type=str, required=True)	
	parser.add_argument('--top', '-t', action='store_true')
	parser.add_argument('--bottom', '-b', action='store_true')
	parser.add_argument('--right', '-r', action='store_true')
	parser.add_argument('--left', '-l', action='store_true')
	parser.add_argument('--diameter', '-d', action='store_true')
	parser.add_argument('--height', '-h', action='store_true')

	args = parser.parse_args()

	file_name = args.file

	with open(file_name, 'r') as f:
		arr = f.read()
		arr = list(map(int, arr.strip().split()))

		bst = BST(arr)

		if bst.check():
			print("valid")

			if args.top: print("top\t" + " ".join(str(i) for i in bst.top()))
			if args.bottom: print("bottom\t" + " ".join(str(i) for i in bst.bottom()))
			if args.right: print("right\t" + " ".join(str(i) for i in bst.right()))
			if args.left: print("left\t" + " ".join(str(i) for i in bst.left()))
			if args.diameter: print("diameter\t" + " ".join(str(i) for i in bst.diameter()))
			if args.height: print("height : {}".format(bst.height()))

		else:
			print("invalid")







