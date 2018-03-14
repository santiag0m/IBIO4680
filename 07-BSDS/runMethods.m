
globDir = '/datos1/vision/GonzalezMolina/BSR/BSDS500/data';
imDir = fullfile(globDir,'images','test');
outDir1 = fullfile(globDir,'segs','function1');
mkdir(outDir1)
outDir2 = fullfile(globDir,'segs','function2');
mkdir(outDir2)

k = 10;
k = logspace(0,1.7,k);
k = round(k);

fl = ls(imDir);
fl = strsplit(fl);
fl(1:2) = [];

for i=1:numel(fl)
    % Segmentation matrix
    segs = cell(numel(k),1);
    imname = fl{i};
    img = imread(fullfile(imDir,imname));
    for w=1:2
        switch w
            case 1
            matname = fullfile(outDir1,strcat(imname(1:end-4),'.mat'));
            segfun = 'gmm';
            case 2
            matname = fullfile(outDir2,strcat(imname(1:end-4),'.mat'));
            segfun = 'hierarchical';
            img = imresize(img,0.5) % Run faster
        end
        for j=1:numel(k)
            segs{j}=segmentByClustering(img,'hsv',segfun,k(j));
            if w==2
                segs{j}=imresize(segs{j},2,'nearest');
            end
            disp(j)
        end
        save(matname,'segs');
    end
end


