sampleNum = 1000000;

sum = 0;

for i = 1: sampleNum
    sample = normrnd(0, 1);
    sum = sum + (sample^2) * (1/2 * exp(-abs(sample))) / normpdf(sample, 0, 1);
end

ans = sum / sampleNum;
disp('ÆÚ´ý‚Ž¤Ï')
disp(ans)