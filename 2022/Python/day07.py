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
		""" this separate function that calls the print function is to have the top root
		be on the least indented folder before the recursive print function finishes the rest
		:return: None
		"""
		print(f"- {self.name} (dir) {self.size}")
		self.printTree()
		return

	def printTree(self, depth=1):
		""" prints out the nested structure, with indentation based on recursion depth

		:param depth: Int - tracks recursion depth so we can print out a nice indented representation
		:return: None
		"""
		indent = "".join('\t' for _ in range(depth))  # gives indent the right amount of tabs
		for key, size in self.files.items():  # print files first
			print(f"{indent}- {key} (file, size={size})")
		for each in self.subFolders:  # print sub-folders last but also print their sub-structure before continuing
			print(f"{indent}- {each.name} (dir) {each.size}")
			each.printTree(depth+1)
		return

	def addSubFolder(self, other: 'Folder'):
		""" adds a Folder object to current objects subFolders list

		:param other: Folder - custom class Folder object
		:return: None
		"""
		self.subFolders.append(other)
		other.parent = self  # update the parent
		return

	def addFile(self, file):
		""" adds a file to the Folders file dictionary, then calls the size updater

		:param file: List - List of [str, str] as [size, name] as provided by puzzle input
		:return: None
		"""
		size = int(file[0])
		self.files[file[1]] = int(size)
		self.updateSizes(size)  # update file sizes of directories
		return

	def updateSizes(self, size):
		""" updates the sizes of all folder containers above added file

		:param size: Int - size of file or folder passed
		:return: None
		"""
		self.size += size
		if self.parent is not None:
			self.parent.updateSizes(size)
		return

	def findDirsMin(self, size):
		""" finds folders <= a specific size and returns a list of their sizes

		:param size: Int - file size
		:return: List - list of sizes of dirs that meet the size criteria
		"""
		dir_size_l = []
		if self.size <= size:
			dir_size_l.append(self.size)  # add director size to current list
		if not self.subFolders:  # if no sub-folders start tracing back up the stack
			return dir_size_l
		for each in self.subFolders:
			dir_size_l = dir_size_l + each.findDirsMin(size)  # combine current list with returned list
		return dir_size_l  # bring list up the stack

	def findDirsMax(self, size):
		""" finds folders >= a specific size and returns a list of their sizes

		:param size: Int - file size
		:return: List - list of sizes of dirs that meet the size criteria
		"""
		dir_size_l = []
		if self.size >= size:
			dir_size_l.append(self.size)  # add director size to current list
		if not self.subFolders:  # if no sub-folders start tracing back up the stack
			return dir_size_l
		for each in self.subFolders:
			dir_size_l = dir_size_l + each.findDirsMax(size)  # combine current list with returned list
		return dir_size_l  # bring list up the stack


def buildSubstructure(commands):
	""" takes the puzzle data and reconstructs the folder and file hierarchy based on terminal commands and outputs

	:param commands: List - list of terminal output lines
	:return: None
	"""
	current_folder = root
	for line in commands:
		match line[0]:
			case '$':  # line is a command
				match line[1]:
					case 'cd':  # change directory command
						match line[2]:
							case '/':  # return to root
								current_folder = root
							case '..':  # move out to parent
								current_folder = current_folder.parent  # our current folder becomes parent folder
							case _:  # move to a sub-folder if it exists
								for each in current_folder.subFolders:
									if each.name == line[2]:
										current_folder = each  # our current folder becomes the changed dir
			case 'dir':  # line is an output and a listed director
				current_folder.addSubFolder(Folder(line[1]))
			case _:  # line is an output and a listed file
				current_folder.addFile(line)
	return


if __name__ == "__main__":
	root = Folder("/")
	disk_size = 70_000_000
	update_size = 30_000_000
	buildSubstructure(data)
	free_space = disk_size - root.size
	extra_space_needed = update_size - free_space
	print("part 1: ", sum(root.findDirsMin(100_000)))
	print("part 2: ", min(root.findDirsMax(extra_space_needed)))
