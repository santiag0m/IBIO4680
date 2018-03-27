
globDir = '~/BSR/BSDS500/data';
imDir = fullfile(globDir,'images','test');
outDir1 = fullfile(globDir,'segs','function1');
mkdir(outDir1)
outDir2 = fullfile(globDir,'segs','function2');
mkdir(outDir2)

k = 20;
k = linspace(2,30,k);
k = round(k);

fl = dir(fullfile(imDir,'*.jpg'));
total = numel(fl);

for i=1:total
    % Segmentation matrix
    segs = cell(numel(k),1);
    imname = fl(i).name;
    img = imread(fullfile(imDir,imname));
    os = size(img);
    os = os(1:2);
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
        parfor j=1:numel(k)
            try
                segs{j}=segmentByClustering(img,'hsv',segfun,k(j));
            catch
                segs{j}=ones(os);
                warning('Selected method did not found a solution');
            end
            segs{j}=imresize(segs{j},os,'nearest');
            disp(j)
        end
        save(matname,'segs');
    end
    disp(i/total)
end


