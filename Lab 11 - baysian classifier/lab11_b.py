import numpy as np
 
dataset= {2:0,1:0,3:0,1.5:0,4.1:0,6:1,5:1,7:1, 8:1,7.6:1}
test = 5

x_train = np.array(list(dataset.keys()))
y_train = np.array(list(dataset.values())) 

p_pos = len(y_train[y_train==1])/len(y_train) 
p_neg = len(y_train[y_train==0])/len(y_train) 

mean_n=np.mean(x_train[y_train==0])
mean_p=np.mean(x_train[y_train==1])

var_n=np.var(x_train[y_train==0])
var_p=np.var(x_train[y_train==1])

def gaussian_pdf(x,mean,var):
	return (1/np.sqrt(2*np.pi*var))* np.exp(-(x-mean)*2/(2*var))

g_pdf_n=gaussian_pdf(test,mean_n,var_n)
g_pdf_p=gaussian_pdf(test,mean_p,var_p)

# compute posterior probability of each class
posterior_0=g_pdf_n*p_neg
posterior_1=g_pdf_p*p_pos

if(posterior_1>posterior_0): print("Class 1")
else:print("Class 0")