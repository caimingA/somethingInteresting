sampleNum = 1000000;

sum = 0;
for i = 1: sampleNum
    u = rand(1, 1, 'double');
    sample = -sign(u - 1/2) * log(1 - 2 * abs(u - 1/2));
    sum = sum + (sample^2) * (1/2 * exp(-abs(sample))) / (1/2 * exp(-abs(sample)));
end

ans = sum / sampleNum;
disp('ÆÚ´ý‚Ž¤Ï')
disp(ans)