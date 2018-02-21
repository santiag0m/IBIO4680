d1 = imread('dog12.png');
d2 = imread('dog22.png');
img = createhybrid(d1, d2, [64,16],[29 29]);
figure;imshow(img)
imwrite(img,'hybrid.png')