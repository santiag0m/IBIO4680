imDir = fullfile(pwd,'images','test');
outDir = fullfile(pwd,'segs');
mkdir(outDir)

k = 10;
k = logspace(1,3,k);
k = round(k);

fl = ls(imDir);
fl(1:2,:) = [];