function img = createhybrid(img1, img2, sigma, ksize)

if numel(sigma)<2
    sigma = [sigma sigma];
elseif numel(sigma)>3
    error('Sigma must contain two elements')
end

if size(img1,2)>size(img2,2)
    img1 = imresize(img1,size(img2));
elseif size(img1,2)<size(img2,2)
    img2 = imresize(img2,size(img1));
end
    

nim1 = imgaussfilt(img1,sigma(1),'FilterSize',ksize);
nim2 = imgaussfilt(img2,sigma(2),'FilterSize',ksize);

img = img1-nim1+nim2;
% img = imadd(imsubtract(img1,nim1),nim2);