const images = ["img1.jpg","img2.png","img3.jpg"];

const chosenImage = images[parseInt(Math.random() * images.length)];

const bgImage = document.createElement("img");

bgImage.src = `img/${chosenImage}`;

document.body.appendChild(bgImage);