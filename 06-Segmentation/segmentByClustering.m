function segmentation = segmentByClustering( rgbImage, featureSpace, clusteringMethod, numberOfClusters)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

% featureSpace : 'rgb', 'lab', 'hsv', 'rgb+xy', 'lab+xy' or 'hsv+xy'
% clusteringMethod = 'kmeans', 'gmm', 'hierarchical' or 'watershed'.
% numberOfClusters positvie integer (larger than 2)
[n, m, ~] = size(rgbImage);
switch featureSpace
    case {'rgb', 'rgb+xy'}
        image = rgbImage;
        features = reshape(image(:), [n*m, 3]);
    case {'lab', 'lab+xy'}
        image = rgb2lab(rgbImage);
        features = reshape(image(:), [n*m, 3]);
    case {'hsv', 'hsv+xy'}
        image = rgb2hsv(rgbImage);
        features = reshape(image(:), [n*m, 3]);
    otherwise
        error('Unexpected feature space. No segmentation created.')
end

if (~isempty(strfind(featureSpace, '+xy')))
    x = repmat((0:n-1)', [m, 1]);
    y = repmat(0:m-1, [n, 1]);
    features(:, end+1) = x;
    features(:, end+1) = y(:);
end
features = double(features);

if(numberOfClusters < 2 || mod(numberOfClusters, 1) ~= 0)
    error('The number of cluster must be a positive integer larger that 2')
end

switch clusteringMethod
    case 'kmeans'
        features = double(features);
        segmentation = kmeans(features, numberOfClusters);
        segmentation = reshape(segmentation, [n m]);
    case 'gmm'
        GMModel = gmdistribution.fit(features, numberOfClusters);
        segmentation = cluster(GMModel, features);
        segmentation = reshape(segmentation, [n m]);
    case 'hierarchical'
        segmentation = clusterdata(features,'Maxclust', numberOfClusters);
        segmentation = reshape(segmentation, [n m]);
    case 'watershed'
        image = rgb2gray(rgbImage);
        hy = fspecial('sobel');
        hx = hy';
        Iy = imfilter(double(image), hy, 'replicate');
        Ix = imfilter(double(image), hx, 'replicate');
        grad = sqrt(Ix.^2 + Iy.^2);
        grad = imdilate(grad, ones(10));
        
        hmin = min(grad(:));
        hmax = max(grad(:));
        h = hmax/2;
        
        ws = watershed(imhmin(grad, h));
        k = max(ws(:));
        
        while(h < hmax && k ~= numberOfClusters)
            if(k > numberOfClusters)
                hmin = h;
                h = (hmax+h)/2;
            elseif( k < numberOfClusters)
                hmax = h;
                h = (h+hmin)/2;
            end
            ws = watershed(imhmin(grad, h));
            k = max(ws(:));
        end
        segmentation = ws;
    otherwise
        error('Unexpected clustering method. No segmentation created')
end
end

