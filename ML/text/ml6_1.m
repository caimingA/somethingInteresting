load digit.mat
mu1 = mean(X(:, :, 1), 2);
mu2 = mean(X(:, :, 2), 2);

S = (cov(X(:, :, 1)') + cov(X(:, :, 2)')) / 2;

t = T(:, :, 1);
invS = inv(S);
p1 = t' * invS*mu1 - mu1'*invS*mu1 / 2;
p2 = t' * invS*mu2 - mu2'*invS*mu2 / 2;
result = sign(p2 - p1);

correctNum = sum(result == -1)
mistakeNum = sum(result ~= -1)

mistake = find(result ~= -1);
mistake
imagesc(reshape(t(:, mistake), [16, 16])')