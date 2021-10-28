load digit.mat
data1 = X(:, :, 1);
data2 = X(:, :, 2);
data3 = T(:, :, 1);
data4 = T(:, :, 2);

train = [data1, data2]';%train data
[m, n] = size(train);%m = 256; n = 1000 <- (500+500)
test = [data3, data4]';
[i, j] = size(test);

label = [zeros(1, m / 2), ones(1, m / 2)]';%l is 0(label), 2 is 1(label)

train = [train ones(m, 1)];
test = [test ones(i, 1)];

theta = zeros(n+1, 1);

iteration = 200;
alpha = 0.01;

for iter = 1: iteration
    z = train * theta;
    h = 1./(1 + exp(-z));
    loss = h - label;
    graident = train' * loss;
    theta = theta - (alpha / m) * graident;
end
result = sign(0.5 - exp(-test * theta)./exp(test * theta));%-1 -> 1; 1 -> 2
result1 = result(1: 200);
result2 = result(201: 400);
error1 = find(result1 == 1)
error2 = find(result2 == -1)

for iter = 1: size(error2)
   figure(iter);
   imagesc(reshape(data4(:, error2(iter)), [16, 16])')
end


    