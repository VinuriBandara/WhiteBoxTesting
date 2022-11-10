import argparse

class BST:
	def __init__(self, arr):
		self.arr = arr
		self.len = len(arr)
		self.tree = [None for i in range(self.len)]

	def complete(self):
		if self.height() > 10:
			return False
		if self.len != (2 ** self.height() - 1):
			return False

		return True

	def check(self):
		for i in range(self.len):
			val = self.arr[i]
			pos = 0

			while pos < self.len and self.tree[pos]:
				if val > self.tree[pos]:
					pos = 2*pos+2
				elif val < self.tree[pos]:
					pos = 2*pos + 1
				else:
					return False

			if pos != i:
				return False

			self.tree[pos] = val

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

	def validateInput(array):
		for i in array:
			if not i.isdigit():
				return "[ERROR] All provided items should be integers!"
			if int(i) > 10000: 
				return "[ERROR] Provided numbers should not exceed 10000!"

		return True 

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
		inputValid = validateInput(arr.split())

		if inputValid == True:

			arr = list(map(int, arr.strip().split()))
			bst = BST(arr)

			if bst.complete():
				if bst.check():
					print("valid")

					if args.top: print("top: " + " ".join(str(i) for i in bst.top()))
					if args.bottom: print("bottom: " + " ".join(str(i) for i in bst.bottom()))
					if args.right: print("right: " + " ".join(str(i) for i in bst.right()))
					if args.left: print("left: " + " ".join(str(i) for i in bst.left()))
					if args.diameter: print("diameter: " + " ".join(str(i) for i in bst.diameter()))
					if args.height: print("height: {}".format(bst.height()))

				else:
					print("invalid")
			else:
				print("[ERROR] The provided list of numbers should build a complete binary tree!")

		else: 
			print(inputValid)







