def printD(dict):
	for key in dict:
		print (key, dict[key])

class node():
    def __init__(self, name, isLeaf):
        self.name = name
        self.branch = None
        self.isLeaf = isLeaf
        self.children = []
        self.prediction = []
        self.parent = None

def produceTree():
	f = open("/Users/habibabassem/Desktop/outputtree.txt","r")
	data = f.read()
	d = data.split("\n")
	temp = []
	for i in range (len(d)):
	    temp.append(d[i])
	    if (d[i] == ''):
	        if ("prediction" not in temp[len(temp)-3]):# not a leaf
	            if (temp[len(temp)-2] == 'parent = None'): #root
	                root = temp[len(temp)-3][(temp[len(temp)-3].find('=') + 2):]
	                NORM_recoveries = node(root, 0)
	                # exec(root +" = node(root,0)")
	                # exec("root = "+z+"")
	                temp = []
	            else:
	            #not a root
	                z = temp[len(temp)-3][(temp[len(temp)-3].find('=') + 2):]
	                exec(z+" = node(z,0)")
	                y = temp[len(temp)-4][(temp[len(temp)-4].find('=') + 2):]
	                exec(z+".branch = float(y)")
	                p = temp[len(temp)-2][(temp[len(temp)-2].find('=') + 2):]
	                exec (z+".parent = p")
	                exec(p+".children.append("+z+")")
	                temp = []
	        else:#leaf
	            res = node("res",1)
	            b = temp[0][(temp[0].find('=') + 2):]
	            res.branch = float(b)
	            res.prediction = float(temp[1][(temp[1].find('=') + 2):])
	            p = temp[2][(temp[2].find('=') + 2):]
	            res.parent = p
	            exec(p+".children.append(res)")
	            temp = []
	return NORM_recoveries

def predict(node, dict):
    if(node == None):
	    node = produceTree()
    
    if (node.isLeaf == 1):
        x = node.prediction
        return x
    
    min_diff = 100
    min_index = 0
    for i in range (len(node.children)):
        if(dict[node.name] == node.children[i].branch):
            return predict(node.children[i], dict)
        else:
            diff = abs (float(dict[node.name]) - float(node.children[i].branch))
            if (diff < min_diff):
                min_diff = diff
                min_index = i
    print(dict[node.name], "No branch found", node.children[min_index].branch)           
    return predict(node.children[min_index], dict)




