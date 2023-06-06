// const toss__content = document.querySelector('.toss__content')
const slug = document.querySelector('#tossTitle').value

const place_participants = document.querySelector('.toss__content__show__athletes')
const place_sort = document.querySelector('.toss__content__right')

const weight_category__select = document.querySelector('#weight_category')
const weight__select = document.querySelector('#weight')

const drawButton = document.querySelector('#draw')
const confirmButton = document.querySelector('#confirm')
const clearButton = document.querySelector('#clear')


// Get data from API
const getDataFromApi = async (url) => {
   try {
      let response = await fetch(url)
      let data = await response.json()
      return data
   } catch (error) {
      throw new Error(`Error fetching data from API: ${error}`);
   }
}

// Without reload page
window.addEventListener('beforeunload', function(event) {
   // Отменить перезагрузку страницы по умолчанию
   event.preventDefault();

   // Отобразить пользовательское сообщение
   event.returnValue = 'Вы уверены, что хотите покинуть эту страницу?';  // Старые браузеры
   return 'Вы уверены, что хотите покинуть эту страницу?';  // Современные браузеры
});

let category__weight = localStorage.getItem('category__weight') ?? ''
let weight = localStorage.getItem('weight') ?? ''

// get data from local storage
if (category__weight != null && weight!= null || category__weight != '' && weight != '') {   
   console.log(category__weight, weight)
   showParticipants()
}

// Add weight categories
getDataFromApi(`/api/tournaments/${slug}/weight_categories`)
   .then((data) => {
      // render all weight categories in options
      data.map(item => {
         weight_category__select.innerHTML += `<option value="${item.id}">${item.gender} ${item.year}</option>`
      })
   })

// when user select some category
weight_category__select.onchange = (e) => {
   weight__select.innerHTML = '<option value="" selected disabled >Select Weight</option>'
   
   category__weight =  e.target.value
   localStorage.setItem('category__weight', category__weight)

   getDataFromApi(`/api/tournaments/${slug}/weight_categories/${category__weight}/weights`)
      .then((data) => {
         // render all weight in options
         data.map(item => {
            console.log(data)
            weight__select.innerHTML += `<option value="${item.id}">${item.name} - (${item.participants_count})</option>`
         })
      })
}

// when user select some weight
weight__select.onchange = (e) => {
   weight = e.target.value
   localStorage.setItem('weight', weight)
   showParticipants()
}

// Show participants
function showParticipants() {
   place_participants.innerHTML = ''
   place_sort.innerHTML = ''

   getDataFromApi(`/api/tournaments/${slug}/weight_categories/${category__weight}/weights/${weight}/participants`)
      .then((data) => {
         if (data.length > 0) {
            for (let i = 0; i < data.length; i++) {
               place_participants.innerHTML += `<div class='toss__participant' draggable='true'>${data[i].firstName} ${data[i].lastName} ${data[i].thirdName} (${data[i].discharge})</div>` 
               
               let div = document.createElement('div');
               div.classList.add('place');
               div.classList.add(`seet${i}`)
   
               if (i % 2 == 0) {
                  div.classList.add('place__top')
               } else {
                  div.classList.add('place__bottom')
               }
   
               place_sort.appendChild(div)
            }
         } else {
            place_sort.innerHTML = '<h1>Participants Not Found</h1>'
            place_participants.innerHTML = '<h5>Participants Not Found</h5>'
         }
      })
}

// If You Click on Clear Button (clear everything)
clearButton.onclick = () => {
   let result = confirm('Вы уверены, что хотите очистить?');

   if (result) {
      showParticipants()
   }
}