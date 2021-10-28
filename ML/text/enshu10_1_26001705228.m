sampleNum = 1000000;

sum = 0;
for i = 1: sampleNum
    x = rand(1, 1, 'double');
    y = rand(1, 1, 'double');
    
    if x^2 + y^2 < 1
        sum = sum + 1;
        %sum = sum + 1/sampleNum;
    end
end

sum = sum*4/sampleNum;
%sum = sum*4;

disp('ƒÒÖÜÂÊ¤Ï')
disp(sum)