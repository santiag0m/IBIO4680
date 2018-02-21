%% Hybrid image
d1 = imread('dog12.png');
d2 = imread('dog22.png');
img = createhybrid(d1, d2, [64,16],[29 29]);
figure;imshow(img)
imwrite(img,'hybrid.png')

%% Gaussian pyramid
pyramid_down{1} = imread('hybrid.png');
sigma = 1;

figure
subplot(2, 3, 1)
imshow(pyramid_down{1})
for i = 2:6
    down = imgaussfilt(pyramid_down{i-1}, sigma);
    pyramid_down{i} = down(1:2:end, 1:2:end, :);
    subplot(2, 3, i)
    imshow(pyramid_down{i})
end

%% Pyramid blending
dog1 = imread('dog12.png');
dog2 = imread('dog22.png');
blended = zeros(size(dog1), 'uint8');
blended(:, 1:end/2, :) = dog2(:, 1:end/2, :); 
blended(:, end/2:end, :) = dog1(:, end/2:end, :); 

pyramid_laplacian{1} = blended;
pyramid_down{1} = blended;

sigma = 3;

for i = 2:6
    down = imgaussfilt(pyramid_down{i-1}, sigma);
    pyramid_down{i} = down(1:2:end, 1:2:end, :);
    [r, c, w] = size(pyramid_down{i-1});
    pyramid_laplacian{i} = imsubtract(pyramid_down{i-1}, imresize(pyramid_down{i}, [r c])); 
end

pyramid_up{6} = pyramid_down{end};
for i = 6:-1:2
    [r, c, w] = size(pyramid_laplacian{i});
    pyramid_up{i-1} = imadd(imresize(pyramid_up{i}, [r c]), pyramid_laplacian{i});
end

figure
imshow(pyramid_up{2})