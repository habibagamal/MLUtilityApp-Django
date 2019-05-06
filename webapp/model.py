import pandas as pd
import math
def printD(inp):
	for key in inp:
		print (key, inp[key])

class node():
    def __init__(self, name, isLeaf):
        self.name = name
        self.branch = None
        self.isLeaf = isLeaf
        self.children = []
        self.prediction = []
        self.parent = None

# def norm(inp):
#     f = pd.read_csv("/Users/habibabassem/Desktop/mysite/MinMax.csv")
#     for key in inp:
#          inp[key] = (float(inp[key])-f[key][0])/(f[key][1]-f[key][0])
#     return inp

def formDictionaryMax():
	maxi = {}
	maxi['NORM_recoveries'] = 39444.37
	maxi['NORM_last_pymnt_amnt'] = 35760.2
	maxi['NORM_int_rate'] = 0.2606
	maxi['NORM_loan_amnt'] = 35000
	maxi['NORM_dti'] = 34.99
	maxi['NORM_mo_sin_old_il_acct'] = 649
	maxi['NORM_total_rec_late_fee'] = 494.3000001
	maxi['NORM_num_actv_rev_tl'] = 37
	maxi['NORM_total_rec_int'] = 27884.8
	maxi['NORM_revol_util'] = 1.404
	maxi['NORM_installment'] = 1408.13
	maxi['NORM_earliest_credit_line'] = 2010
	maxi['NORM_total_pymnt'] = 62884.79738
	maxi['NORM_total_rec_late_fee'] = 494.3000001
	maxi['NORM_pct_tl_nvr_dlq'] = 100
	maxi['NORM_total_pumnt_inv'] = 62862.51
	maxi['NORM_open_acc'] = 62
	maxi['NORM_mths_since_recent_inq'] = 24
	maxi['NORM_total_acc'] = 105
	maxi['NORM_mort_acc'] = 31
	maxi['mths_since_recent_revol_delinq'] = 165
	maxi['NORM_delinq2Yrs'] = 29
	maxi['NORM_annual_inc'] = 7141778
	maxi['NORM_mo_sin_old_rev_tl_op'] = 760
	maxi['NORM_last_pymnt_d'] = 2020
	maxi['issue_d'] = 24
	maxi['NORM_bc_util'] = 339.6
	maxi['NORM_num_rev_accts'] = 94
	maxi['term'] = 60
	maxi['mths_since_last_delinq'] = 156
	maxi['mths_since_last_record'] = 121
	maxi['mths_since_recent_bc_dlq'] = 152
	maxi['NORM_pct_tl_nvr_dlq'] = 100
	maxi['NORM_acc_open_past_24mths'] = 40
	maxi['NORM_funded_amnt_inv'] = 35000
	return maxi

def formDictionaryMin():
	mini = {}
	mini['NORM_recoveries'] = 0
	mini['NORM_last_pymnt_amnt'] = 0
	mini['NORM_int_rate'] = 0.06
	mini['NORM_loan_amnt'] = 1000
	mini['NORM_dti'] = 0
	mini['NORM_total_rec_late_fee'] = 0
	mini['NORM_num_actv_rev_tl'] = 0
	mini['NORM_total_rec_int'] = 0
	mini['NORM_revol_util'] = 0
	mini['NORM_installment'] = 4.93
	mini['NORM_earliest_credit_line'] = 1950
	mini['NORM_total_pymnt'] = 0
	mini['NORM_total_rec_late_fee'] = 0
	mini['NORM_pct_tl_nvr_dlq'] = 0
	mini['NORM_total_pumnt_inv'] = 0
	mini['NORM_open_acc'] = 0
	mini['NORM_mths_since_recent_inq'] = 0
	mini['NORM_mo_sin_old_il_acct'] = 0
	mini['NORM_total_acc'] = 2
	mini['NORM_mort_acc'] = 0
	mini['mths_since_recent_revol_delinq'] = 0
	mini['NORM_delinq2Yrs'] = 0
	mini['NORM_annual_inc'] = 4800
	mini['NORM_mo_sin_old_rev_tl_op'] = 0
	mini['NORM_last_pymnt_d'] = 1900.083333
	mini['issue_d'] = 1
	mini['NORM_bc_util'] = 0
	mini['NORM_num_rev_accts'] = 0
	mini['term'] = 36
	mini['mths_since_last_delinq'] = 0
	mini['mths_since_last_record'] = 1
	mini['mths_since_recent_bc_dlq'] = 0
	mini['NORM_pct_tl_nvr_dlq'] = 0
	mini['NORM_acc_open_past_24mths'] = 0
	mini['NORM_funded_amnt_inv'] = 950
	return mini

def normalize(inp):
	mini = formDictionaryMin()
	maxi = formDictionaryMax()
	for key in inp:
#        print(key)
		inp[key] = round((float(inp[key]) - mini[key]) / (maxi[key] - mini[key]),2)
	return inp

def produceTree():
	f = open("/Users/habibabassem/Desktop/mysite/outputtree.txt","r")
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

def predict(node, inp):
	# printD(inp)
	# printD(inp)
	if(node is None):
		inp = normalize(inp)
		node = produceTree()
	if (node.isLeaf == 1):
		x = node.prediction
		return x
	min_diff = 100
	min_index = 0
	for i in range (len(node.children)):
		if(inp[node.name] == node.children[i].branch):
			return predict(node.children[i], inp)
		else:
			diff = abs (float(inp[node.name]) - float(node.children[i].branch))
			if (diff < min_diff):
				min_diff = diff
				min_index = i
	return predict(node.children[min_index], inp)




