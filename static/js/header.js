const mobile__menu = document.querySelector('.mobile__menu')

const header__center = document.querySelector('.header__center')
const header__right = document.querySelector('.header__right')

mobile__menu.onclick = () => {
   if (header__center.style.display == 'none') {
      console.log('open')
      header__center.style.display = 'flex'
      header__right.style.display = 'flex';

      setTimeout(() => {
         header__right.style.right = '0'
      }, 300)
   } else {
      console.log('close')
      header__center.style.display = 'none'
      header__right.style.display = 'none'
   }
}

document.getElementById("changeLanguage").addEventListener("change", function() {
   document.getElementById("LanguageForm").submit();
 });