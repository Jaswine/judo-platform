const inputs = document.querySelectorAll('input');
const selects = document.querySelectorAll('select');
const textareas = document.querySelectorAll('textarea');
const create__tournire = document.getElementById('create__tournire')


// Save in Local Storage and get value from him
const saveInLoacalstorage = (fields) => {
   for (let i = 0; i < fields.length; i++) {
      // Get From Local Storage
      fields[i].value = localStorage.getItem(`${fields[i].localName}-${i}`);
      
      fields[i].addEventListener('change', (e) => {
         // Set This Value into Local Storage
         localStorage.setItem(`${e.originalTarget.localName}-${i}`, e.target.value);
      })
   }
}

saveInLoacalstorage(inputs)
saveInLoacalstorage(selects)
saveInLoacalstorage(textareas)

document.body.addEventListener("mousemove", (e) => {
   x = e.clientX
   y = e.clientY

  if (310 < x < 190 && y > 617 && y < 664) {
   localStorage.clear()
  } 
})