
globDir = '/datos1/vision/GonzalezMolina/BSR/BSDS500/data';
imDir = fullfile(globDir,'images','test');
outDir1 = fullfile(globDir,'segs','function1');
mkdir(outDir1)
outDir2 = fullfile(globDir,'segs','function2');
mkdir(outDir2)

k = 10;
k = logspace(0.31,1.5,k);
k = round(k);
k = [2, 3, 4, 5, 6, 7];

fl = ls(imDir);
fl = strsplit(fl);
fl(1:2) = [];

for i=1:numel(fl)
    % Segmentation matrix
    segs = cell(numel(k),1);
    imname = fl{i};
    img = imread(fullfile(imDir,imname));
    img = imresize(img,0.25); % Run faster
    for w=1:2
        switch w
            case 1
            matname = fullfile(outDir1,strcat(imname(1:end-4),'.mat'));
            segfun = 'gmm'
            case 2
            matname = fullfile(outDir2,strcat(imname(1:end-4),'.mat'));
            segfun = 'hierarchical'
        end
        for j=1:numel(k)
            segs{j}=segmentByClustering(img,'hsv',segfun,k(j));
            segs{j}=imresize(segs{j},4,'nearest');
            disp(j)
        end
        save(matname,'segs');
    end
    disp(i)
end


