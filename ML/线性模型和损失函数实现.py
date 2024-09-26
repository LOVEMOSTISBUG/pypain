import numpy as np
import matplotlib.pyplot as plt

def compute_model_output(x, w, b):
    """输入训练数据x轴 参数w与b 返回预测Y"""
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
        
    return f_wb


def compute_cost(x, y, w, b): 
    """输入训练XY轴 参数w和b 返回损失函数值"""
    m = x.shape[0] 
    
    cost_sum = 0 
    for i in range(m): 
        f_wb = w * x[i] + b   
        cost = (f_wb - y[i]) ** 2  
        cost_sum = cost_sum + cost  
    total_cost = (1 / (2 * m)) * cost_sum  

    return total_cost

x_train =  np.array([1.0, 2.0,3.0,4.0,5.0])
y_train = np.array([13.2,23.6,45.2,31.5,52.0])

w = 5
b = 10

tmp_f_wb = compute_model_output(x_train, w, b)


plt.rcParams['font.family'] = 'STSong'#设置中文字体防止口口

# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c='b',label='预测值')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r',label='实际值')


# Set the title
plt.title(f"此时的损失函数数值为：{ compute_cost(x_train,y_train,w, b)}")
plt.ylabel('Y轴')
plt.xlabel('X轴')

plt.show()