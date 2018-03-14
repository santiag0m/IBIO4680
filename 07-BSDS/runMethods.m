
globDir = '/datos1/vision/GonzalezMolina/BSR/BSDS500/data'
imDir = fullfile(globDir,'images','test');
outDir = fullfile(globDir,'segs');
mkdir(outDir)

k = 10;
k = logspace(1,3,k);
k = round(k);

fl = ls(imDir);
fl = strsplit(fl);
fl(1:2) = [];

for i=1:numel(fl)
    % Segmentation matrix
    segs = cell(10,1);


