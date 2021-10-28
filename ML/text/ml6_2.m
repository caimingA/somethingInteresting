load digit.mat X T
[d, n, nc] = size(X);
S = zeros(d, d);
for c = 1: nc
    mu(:, c) = mean(X(:, :, c), 2);
    S = S + cov(X(:, :, c)')/nc;
end
invS = inv(S);

for ct=1: nc
    for c=1: nc
        muc = mu(:, c);
        t = T(:, :, ct);
        p(ct,: , c) = t' * invS*muc - muc' * invS * muc / 2;
    end
end

[pmax, P] = max(p, [], 3);
for ct = 1: nc
    for c = 1: nc
        C(ct, c) = sum(P(ct, :)==c);
    end
end

C