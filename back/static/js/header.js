console.log("Header has been loaded")
const nav__menu__button = document.querySelector('.nav__menu__button');
const mobile__menu = document.querySelector('.mobile__menu')

nav__menu__button.addEventListener('click', () => {
   console.log("Header clicked")
   if (mobile__menu.style.display == 'none') {
      mobile__menu.style.display = 'flex';

      setTimeout(() => {
         mobile__menu.style.top = '60px'
      }, 10)
   } else {
      mobile__menu.style.display = 'none';
      mobile__menu.style.top = '-100%'
   }
})