const images = document.querySelectorAll('.slider__image');

const slider__left = document.getElementById('slider__left'); 
const slider__gallery = document.getElementById('slider__gallery');
const slider__right = document.getElementById('slider__right');

let item = 0
let images_count = images.length - 1

const changeSrc = (slider__gallery, images, item) => {
   slider__gallery.src = images[item].src;
}

changeSrc(slider__gallery, images, 0)

slider__left.addEventListener('click', () => {
   if ( item >  0) {
      item-=1;
   } else {
      item = images_count
   }
   changeSrc(slider__gallery, images, item)
})

slider__right.addEventListener('click', () => {
   if (item < images_count) {
      item += 1;
   } else {
      item = 0;
   }
   changeSrc(slider__gallery, images, item)
})