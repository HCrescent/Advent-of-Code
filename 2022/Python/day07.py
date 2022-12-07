"""Day 07 Advent_of_Code 2022"""
with open("input/day07.txt", 'r') as infile:
	data = [line.rstrip().split() for line in infile]


class Folder:
	def __init__(self, name):
		self.subFolders = []
		self.files = {}
		self.size = 0
		self.name = name
		self.parent = None

	def printTreeTop(self):
		print(f"- {self.name} (dir) {self.size}")
		self.printTree()

	def printTree(self, depth=1):
		indent = "".join('\t' for _ in range(depth))
		for key, size in self.files.items():
			print(f"{indent}- {key} (file, size={size})")
		for each in self.subFolders:
			print(f"{indent}- {each.name} (dir) {each.size}")
			each.printTree(depth+1)

	def addSubFolder(self, other):
		self.subFolders.append(other)
		other.parent = self

	def addFile(self, file):
		self.files[file[1]] = int(file[0])

	def updateSizes(self):
		size_sum = 0
		for key, size in self.files.items():
			size_sum += size
		if not self.subFolders:
			self.size = size_sum
		else:
			for each in self.subFolders:
				each.updateSizes()
				size_sum += each.size
			self.size = size_sum

	def findDirsMin(self, size):
		dir_size_l = []
		if self.size <= size:
			dir_size_l.append(self.size)
		if not self.subFolders:
			return dir_size_l
		for each in self.subFolders:
			dir_size_l = dir_size_l + each.findDirsMin(size)
		return dir_size_l

	def findDirsMax(self, size):
		dir_size_l = []
		if self.size >= size:
			dir_size_l.append(self.size)
		if not self.subFolders:
			return dir_size_l
		for each in self.subFolders:
			dir_size_l = dir_size_l + each.findDirsMax(size)
		return dir_size_l


def buildSubstructure(commands):
	current_folder = root
	for line in commands:
		match line[0]:
			case '$':
				match line[1]:
					case 'cd':
						match line[2]:
							case '/':
								current_folder = root
							case '..':
								current_folder = current_folder.parent
							case _:
								for each in current_folder.subFolders:
									if each.name == line[2]:
										current_folder = each
			case 'dir':
				current_folder.addSubFolder(Folder(line[1]))
			case _:
				current_folder.addFile(line)


if __name__ == "__main__":
	root = Folder("/")
	disk_size = 70_000_000
	update_size = 30_000_000
	buildSubstructure(data)
	root.updateSizes()
	free_space = disk_size - root.size
	extra_space_needed = update_size - free_space
	print("part 1: ", sum(root.findDirsMin(100_000)))
	print("part 2: ", min(root.findDirsMax(extra_space_needed)))
