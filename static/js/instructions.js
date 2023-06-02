const instructions = document.querySelectorAll('.instruction__body')
const buttons = document.querySelectorAll('.open__instruction')

for (let i = 0; i < buttons.length; i++) {
   buttons[i].addEventListener('click', () => {
      let instruction = instructions[i]

      if (instruction.style.display == 'none') {
         instruction.style.display = 'block'
         console.log('open')
      } else {
         instruction.style.display = 'none'
      }
   })
}
