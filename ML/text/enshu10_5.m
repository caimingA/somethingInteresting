n = 1000000;
t = zeros(2, n);
S1 = [0.5 0; 0 4];
m1 = x - [0; -2];
w1 = 0.7;
S2 = [4 0; 0 1];
m2 = x - [2; 0];
w2 = 0.3;
%rand
for i=2: n
    u = randn(2, 1)+t(:, i-1);
    if rand<=w1*
end