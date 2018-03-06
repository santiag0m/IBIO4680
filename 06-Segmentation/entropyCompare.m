function coef = entropyCompare(estimate,truth)

if ~prod(size(estimate)==size(truth))
    error('The estimate and ground truth must have the same size')
end

[r,c] = size(estimate);
k = max(truth(:))- min(truth(:)) + 1; % Number of expected regions
k = double(k);
coef = zeros(r,c); % Entropy difference coeficient matrix

dr = zeros(r,1);
dc = zeros(c,1);
mr = zeros(r,1);
mc = zeros(c,1);

for i=1:r
    er = discEntropy(estimate(i,:),k); % Estimate entropy per row
    tr = discEntropy(truth(i,:),k); % Truth entropy per row
    dr(i) = abs(er-tr);
    mr(i) = max(abs([tr,log(k)-tr])); % Maximum entropy difference possible
end

for j=1:c
    ec = discEntropy(estimate(:,j),k); % Estimate entropy per column
    tc = discEntropy(truth(:,j),k); % Truth entropy per column
    dc(j) = abs(ec-tc);
    mc(j) = max(abs([tc,log(k)-tc])); % Maximum entropy difference possible
    for i=1:r
        d = [dr(i),dc(j)];
        md = [mr(i),mc(j)];
        [val,ind] = max(d);
        coef(i,j) = val/md(ind);
    end
end

coef = sum(coef(:))/(r*c); % Normalized total entropy difference
coef = 1-coef; % Similarity


function etp = discEntropy(x,k)

% Calcualte discrete entropy
h = histcounts(x, k, 'Normalization', 'probability');
h(h==0) = 1;
etp = -sum(log(h).*h);

