const messages = document.querySelectorAll('.message');
const message_closes = document.querySelectorAll('.message_close');

/**
 *  TODO: Закрытие сообщений по нажатию на спец кнопку
 */
for (let i=0; i<messages.length; i++) {
   message_closes[i].onclick = () => {
      messages[i].style.display = 'none';
   }
}

/**
 *  TODO: Закрытие сообщений по нажатию на Escape
 */
addEventListener('keydown', (e) => {
   for (let i=0; i<messages.length; i++) {
      if (e.key === 'Delete' || e.key === 'Escape') {
         messages[i].style.display = 'none';
      }
   }
})