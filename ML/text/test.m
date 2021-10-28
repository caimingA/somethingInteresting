% 读取数据集，变量data存储的是一个尺寸为150×5的矩阵
data = load('iris.data');
% 只取前100个样本的信息，即前100行，变量useful_data存储的是一个尺寸为100×5的矩阵
useful_data = data(1:100, :);
% 将特征与类别标签分开存放
% 特征存放在变量X中，X存储的是一个尺寸为100×4的矩阵
% 类别标签存放在变量y中，y存储的是一个尺寸为100×1的矩阵
X = useful_data(:, 1:4)
y = useful_data(:, 5)
% 变量m存储的是变量X的行数，在这里为100
% 变量n存储的是变量X的列数，在这里为4
[m,n] = size(X);
% 在变量X后加一列“1”，便于后面使用矩阵运算简化步骤
X = [X ones(m, 1)];
% 初始化模型参数β=(ω,b)为0
beta = zeros(n+1, 1);
% 设置梯度下降迭代次数为1500次
iteration = 1500;
% 设置学习率为0.01
alpha = 0.01;
% 开始循环，用梯度下降更新参数
for iter = 1 : iteration
    z = X * beta;
    h = 1 ./ (1 + exp(-z));
    error = h - y;
    graident = X' * error;
    beta = beta - alpha / m * graident;
end