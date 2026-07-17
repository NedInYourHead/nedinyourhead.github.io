const fullImg = document.getElementById('full-image');
const caption = document.getElementById('full-image-caption');

galleryFunction(document.getElementById('thumbnail'));

function galleryFunction(thumb) {
    fullImg.src = thumb.src;
    caption.innerHTML = thumb.title;
    thumb.active;
}