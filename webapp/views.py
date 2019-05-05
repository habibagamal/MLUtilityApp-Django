from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from webapp.forms import predictionForm
from django.shortcuts import redirect
from webapp.model import printD
from webapp.model import produceTree
from webapp.model import predict
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'webapp/home.html')

#class formView(TemplateView):
#    template_name = 'webapp/form.html'
#    def get(self, request):




def form(request):
    if request.method == 'POST':
        form = predictionForm(request.POST)
        print('700000')
        if form.is_valid():
            print("a5eeran")
            printD(form.cleaned_data)
            # root = produceTree()
            prediction = predict(None, form.cleaned_data)
            print(form.cleaned_data) 
            if (prediction == 1):
                messages.success(request, "WIll pay")
                return render(request, 'webapp/form.html', {'form': form})
                # return HttpResponse("Will Pay")
            else: 
                messages.warning(request, "Will not pay")
                return render(request, 'webapp/form.html', {'form': form})
                # return HttpResponse("Will NOT Pay")
        else: 
            form = predictionForm(request.POST)
            return render(request, 'webapp/form.html', {'form': form})

    form = predictionForm()
    return render(request, 'webapp/form.html', {'form': form})

# def submit(request):
#     form = predictionForm(request.POST)
#     if form.is_valid():
#         NORM_recoveries = form.cleaned_data['NORM_recoveries']
#     args = {'form':form, 'NORM_recoveries':NORM_recoveries}
#     return render(request, 'webapp/form.html', args)
        
        
#
#def submit(request):
##    return render(request, 'webapp/home.html')
#    if request.method == 'GET':
#        NORM_recoveries = request.GET.get('NORM_recoveries')
#        if (NORM_recoveries == 10):
#            return render(request, 'webapp/home.html')
#!/usr/bin/env python
# coding: utf-8

# In[67]:


#        import numpy as np
#        import math
#
#
#        # In[68]:
#
#
#        f = open("Desktop\\outputtree.txt","r")
#
#
#        # In[69]:
#
#
#        data = f.read()
#
#
#        # In[70]:
#
#
#        class node():
#            def __init__(self, name, isLeaf):
#                self.name = name
#                self.branch = None
#                self.isLeaf = isLeaf
#                self.children = []
#                self.prediction = []
#                self.parent = None
#
#
#        # In[71]:
#
#
#        d = data.split("\n")
#
#
#        # In[ ]:
#
#
#
#
#
#        # In[72]:
#
#
#        temp = []
#        for i in range (len(d)):
#            temp.append(d[i])
#            if (d[i] == ''):
#                if ("prediction" not in temp[len(temp)-3]):# not a leaf
#                    if (temp[len(temp)-2] == 'parent = None'): #root
#                        z = temp[len(temp)-3][(temp[len(temp)-3].find('=') + 2):]
#                        exec(z +" = node(z,0)")
#                        exec("rrrr = "+z+"")
#                        temp = []
#                    else:#not a root
#                        z = temp[len(temp)-3][(temp[len(temp)-3].find('=') + 2):]
#                        exec(z+" = node(z,0)")
#                        y = temp[len(temp)-4][(temp[len(temp)-4].find('=') + 2):]
#                        exec(z+".branch = float(y)")
#                        p = temp[len(temp)-2][(temp[len(temp)-2].find('=') + 2):]
#                        exec (z+".parent = p")
#                        exec(p+".children.append("+z+")")
#                        temp = []
#                else:#leaf
#                    res = node("res",1)
#                    b = temp[0][(temp[0].find('=') + 2):]
#                    res.branch = float(b)
#                    res.prediction = float(temp[1][(temp[1].find('=') + 2):])
#                    p = temp[2][(temp[2].find('=') + 2):]
#                    res.parent = p
#                    exec(p+".children.append(res)")
#                    temp = []
#
#
#        # In[73]:
#
#
#        def printTree (node,file):
#
#            if (node.isLeaf == 1):
#                print ("prediction = ",node.prediction)
#                print ("parent = ",node.parent)
#
#                file.write("prediction = ")
#                file.write(str(node.prediction))
#                file.write("\n")
#
#                file.write("parent = ")
#                file.write(str(node.parent))
#                file.write("\n")
#
#                return
#
#            print ("node name = ",node.name)
#            print ("parent is = ",node.parent)
#
#        file.write("node name = ")
#        file.write(node.name)
#        file.write("\n")
#
#            file.write("parent = ")
#            file.write(str(node.parent))
#            file.write("\n")
#
#            for i in range (len(node.children)):
#                print ("\n")
#                print("value is =", str(node.children[i].branch))
#
#                file.write("\n")
#                file.write("value is = ")
#                file.write(str(node.children[i].branch))
#                file.write("\n")
#
#                printTree(node.children[i],file)
#
#
#        # In[74]:
#
#
#        file = open("Desktop\\TEST.txt","w")
#        printTree(rrrr,file)
#        file.close()
#
#
#        # In[75]:
#
#
#        def predict(node, df, index):
#
#            if (node.isLeaf == 1):
#                x = node.prediction
#                return x
#
#            min_diff = 100
#            min_index = 0
#            for i in range (len(node.children)):
#                if(df.iloc[index][node.name] == node.children[i].branch):
#                    return predict(node.children[i], df, index)
#                else:
#                    diff = abs (float(df.iloc[index][node.name]) - float(node.children[i].branch))
#                    if (diff < min_diff):
#                        min_diff = diff
#                        min_index = i
#            print(df.iloc[index][node.name], "No branch found", node.children[min_index].branch)
#        return predict(node.children[min_index], df, index)
#
#
#        # In[76]:
#
#
#        def predictDF(df):
#            y = []
#            for index, row in df.iterrows():
#                y.append(predict(root, df, index))
#            return pd.DataFrame({'Y':y})
#
#
#        # In[77]:
#
#
#        import pandas as pd
#        import matplotlib.pyplot as plt
#        dataset = pd.read_csv('Desktop\\excel\\cleanFinal.csv')
#        dataset = dataset.round(2)
#        dataset = dataset.iloc[0:188145]
#        X = dataset
#
#
#        # In[80]:
#
#
#        from sklearn.model_selection import train_test_split
#        Train, Test = train_test_split(X, test_size= 0.2, random_state = 0)
#        x_Test = Test.loc[:,'NORM_loan_amnt':'hardship_completed'].iloc[0:188145]
#        y_Test = Test['loan_status']
#
#
#        # In[ ]:
#
#
#        index = np.arange(37629)
#        y_predict = predictDF(x_Test.set_index(index))
#
#
#        # In[ ]:
#
#
#        def accuracy_metrics(y_true, y_predict):
#            from sklearn.metrics import accuracy_score
#            accuracy = accuracy_score(y_true, y_predict)
#            error_rate = 1 - accuracy
#            from sklearn.metrics import precision_score
#            precision = precision_score(y_true, y_predict, average='binary')
#            from sklearn.metrics import recall_score
#            recall = recall_score(y_true, y_predict, average='binary')
#            from sklearn.metrics import confusion_matrix
#            tn, fp, fn, tp = confusion_matrix(y_true, y_predict).ravel()
#            TNR = tn / (tn + fp)
#            FPR = fp / (fp + tn)
#            fscore = (2 * precision * recall) / (precision + recall)
#            from sklearn.metrics import roc_auc_score
#            auc = roc_auc_score(y_true, y_predict)
#            return (accuracy, error_rate, precision, recall, TNR, FPR, fscore, auc)
#
#
#        # In[ ]:
#
#
#        metricsfile = open("Desktop\\METRICSAHOOO.txt","w")
#        (accuracy_logist, logist_error_rate, precision_logist, recall_logist, TNR_logist, FPR_logist, f1score_logist, auc_logist) = accuracy_metrics(y_Test, y_predict)
#        print ("Accuracy = ", accuracy_logist)
#        print ("Error Rate = ",logist_error_rate)
#        print ("Precision = ",precision_logist)
#        print ("Recall = ",recall_logist)
#        print ("True Negative Rate = ", TNR_logist)
#        print ("False Positive Rate = ",FPR_logist)
#        print ("F-score = ", f1score_logist)
#        print ("AUC = ", auc_logist)
#
#        metricsfile.write("Accuracy = ")
#        metricsfile.write(str(accuracy_logist))
#        metricsfile.write("\n")
#
#        metricsfile.write("Error Rate = ")
#        metricsfile.write(str(logist_error_rate))
#        metricsfile.write("\n")
#
#        metricsfile.write("Precision = ")
#        metricsfile.write(str(precision_logist))
#        metricsfile.write("\n")
#
#        metricsfile.write("Recall = ")
#        metricsfile.write(str(recall_logist))
#        metricsfile.write("\n")
#
#
#        metricsfile.write("True Negative Rate = ")
#        metricsfile.write(str(TNR_logist))
#        metricsfile.write("\n")
#
#
#        metricsfile.write("False Positive Rate = ")
#        metricsfile.write(str(FPR_logist))
#        metricsfile.write("\n")
#
#        metricsfile.write("F-score = ")
#        metricsfile.write(str(f1score_logist))
#        metricsfile.write("\n")
#
#        metricsfile.write("AUC = ")
#        metricsfile.write(str(auc_logist))
#        metricsfile.write("\n")
#
#        metricsfile.close()
#
#
#            # In[ ]:
#
#
#
#

            # In[ ]:
            
            
            
            
            
            # In[ ]:

    






    # else:
    # 	return render(request, 'webapp/home.html')
#        form = predictionForm(request.POST)
#        if form_is_valid():
#            return render(request, 'webapp/home.html', {'form': form})
#        else:
#            form = predictionForm()
#        return render(request, 'webapp/form.html', {'form': form})
#
#        # import function to run
#        from path_to_script import function_to_run
#
#        # call function
#        function_to_run()

        # return user to required page
#            return render(request, 'webapp/home.html')


#def post_new(request):
#    if request.method == "POST":
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.published_date = timezone.now()
#            post.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = PostForm()
#    return render(request, 'blog/post_edit.html', {'form': form})
