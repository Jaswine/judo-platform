const messages = document.querySelectorAll('.message');
const message_closes = document.querySelectorAll('.message_close');

for (let i=0; i<messages.length; i++) {
   message_closes[i].onclick = () => {
      messages[i].style.display = 'none';
   }  
}