class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1
    

def add(root, word):
    node = root
    for char in word:
        found_in_child = False
        
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True


def find_prefix(root, prefix):
    node = root
    if not root.children:
        return [False, 0]
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return [False]
    return [True, node]
def suggestions(root,prefix):
    temp=find_prefix(root,prefix)

    if temp[0]:
        count=1
        l=[]
        def printSuggestions(node,str):
            nonlocal count
            if node.word_finished:
                print(count,". ",str,sep="")
                l.append(str)
                count+=1
                return
            for i in node.children:
            
                printSuggestions(i,str+i.char)
        node=temp[1]
        printSuggestions(node,prefix)
        return l
    else:
        print("No result with the prefix entered")
            

class hash:
	def __init__(self):
		self.size = 100
		self.arr = [None for i in range(self.size)]
	
	def get_hash(self, key):
		h = 0
		for char in key:
			h += ord(char)
		return h % 100
	
	def add(self, key, a):
		x = self.get_hash(key)
		if self.arr[x]:
			self.arr[x].append(a)
		else:
			self.arr[x]=[a]
	
	def check(self, key):
		x = self.get_hash(key)
		if self.arr[x] != None:
			for i in range(len(self.arr[x])):
				if self.arr[x][i].adminId==key:
					return True
		return False
	def getVal(self,key):
		x = self.get_hash(key)
		if self.arr[x] != None:
			for i in range(len(self.arr[x])):
				if self.arr[x][i].adminId==key:
					return self.arr[x][i]


class admin:
	def __init__(self):
		self.adminId = None
		self.password = None
		self.name = None
		self.phNo = None
		self.email = None
		self.fresh = True
		self.Shname = None
		self.Loc = None
		self.Pcode = None
	
	def signin(self):
		print("_____SignIn_____\n", "Enter your name : ", end=" ")
		self.name = input()
		print("Enter your phone number : ", end=" ")
		self.phNo = int(input())
		print("Enter your Email address : ", end=" ")
		self.email = input()
		print("Create your Admin Id : ", end=" ")
		self.adminId = input()
		t = 1
		while t:
			print("Create your password : ", end=" ")
			pwd = input()
			print("Confirm your password : ", end=" ")
			pwdcheck = input()
			if pwd == pwdcheck:
				self.password = pwd
				hash_t.add(a.adminId, a)
				print("Successfully Signed In , proceed to login......")
				t = 0
			
			else:
				print("Password not matched!!! Please try again...")
			if t == 0:
				while True:
					print("Enter your Admin ID : ")
					adminid = input()
					if hash_t.check(adminid):
						break
					print("Admin Id entered doesn't exist. Please try again...")
				hash_t.getVal(adminid).login()
	
	def login(self):
		for i in range(3):
			print("Enter Your Password : ", end=" ")
			pwd = input()
			if pwd == self.password:
				self.shop()
				break
			print("Password Incorrect. Please try again...")
			print(2 - i, "Attempt(s) more")
		else:
			print("Too many attempts taken!!")
			return
	
	def shop(self):
	
		if self.fresh:
			self.fresh = False
			print("Welcome,", self.name)
			print("_____Register your shop_____ : ")
			print("Enter Your Shop Name : ")
			self.Shname = input()
			add(root,self.Shname)
			dic[self.Shname]=self.adminId
			print("Enter Your Shop Location : ")
			self.Loc = input()
			print("Enter Pincode : ")
			self.Pcode = int(input())
			print("Successfully Registered")
			self.update()
		else:
			print("Welcome Back,", self.name)
			self.update()
	
	def update(self):
		print("Any updates you want to do?",
			  "1.Update Details",
			  "2.EXIT",
			  sep="\n")
		n2 = int(input())
		if n2 == 1:
			print("What do you want to update?\n1.Shop Name\n2.Location")
			n3 = int(input())
			if n3 == 1:
				print("Enter the shop name : ")
				self.Shname = input()
				print("Successfully Updated")
				self.update()
			else:
				print("Enter the shop Location :")
				self.Loc = input()
				print("Enter the Pincode : ")
				self.Pcode = int(input())
				print("Successfully Updated")
				self.update()

root = TrieNode('*')
hash_t = hash()
dic = {}

a = admin()
a.adminId = "Tarun"
a.password = "Raj123"
a.name = "Rajtarun"
a.phNo = 8972352471
a.email = "tarun@gmail.com"
a.fresh = False
a.Shname = "Dominos"
a.Loc = "Vizag"
a.Pcode = 534442
hash_t.add(a.adminId, a)
add(root,a.Shname)
dic[a.Shname]=a.adminId

a = admin()
a.adminId = "Venkat"
a.password = "v123"
a.name = "Venkat"
a.phNo = 6788681230
a.email = "venkat@gmail.com"
a.fresh = False
a.Shname = "picsart"
a.Loc = "Ongole"
a.Pcode = 634442
hash_t.add(a.adminId, a)
add(root,a.Shname)
dic[a.Shname]=a.adminId


while True:
	print("Welcome!!", "Who are you?", "1.Admin", "2.User","3.Exit", sep="\n")
	print("Enter your choice : ", end=" ")
	n = int(input())
	if n == 1:
		print("Welcome Admin!!",
			  "What would you like to?",
			  "1.SignUp",
			  "2.LogIn",
			  sep="\n")
		print("Enter your choice: ", end=" ")
		n1 = int(input())
		if (n1 == 1):
			a = admin()
			a.signin()
		else:
	
			while True:
				print("Enter your Admin ID : ", end=" ")
				adminid = input()
				if hash_t.check(adminid):
					break
				print("Admin Id entered doesn't exist. Please try again...")
				
			hash_t.getVal(adminid).login()
	elif n == 2:
		print("Search for Services")
		print("Search Through : \n1.Shop Name\n2.Exit\nEnter your choice:")
		n4=int(input())
		if(n4==1):
			selshop=0
			while selshop==0:
				print("Enter the search name : ")
				shval=input()
				print("Select a Shop : ")
				print("Shops with prefix entered :")
				names=suggestions(root,shval)
				if names==None:
				    continue
				print("0. Search again\nEnter Your Choice : ")
				selshop=int(input())
			print("Shop details")
			node=hash_t.getVal(dic[names[selshop-1]])
			print("Shop Name : ",node.Shname)
			print("Shop Location : ",node.Loc)
       
		
	else:
		break
		