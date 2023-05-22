const weight_category = document.querySelector('#weight_category')
const toss_title = document.querySelector('#tossTitle')
const weight = document.querySelector('#weight')
const place_for_participants = document.querySelector('.toss__right__participants')

const toss__title__weight = document.querySelector('.toss__title__weight')
const toss__title__weight__category = document.querySelector('.toss__title__weight__category')

let weight_category_select = ''

const get_from_api = async (url, renderto = '') => {
   let response = await fetch(url)
   let data = await response.json()

   if (renderto) {
      renderto(data)
   }

   return data
}

const weight_categories_render = (weight_categories) => {
   for (let weight_cat of weight_categories) {
      weight_category.innerHTML += `
         <option 
         value="${weight_cat.id}"
         >${weight_cat.gender} ${weight_cat.year}</option>
      `
   }
}

const weight_render = (weights) => {
   weight.innerHTML = `
   <option value="" selected disabled >Select Weight</option>
   `
   for (let weight_cat of weights) {
      weight.innerHTML += `
         <option 
         value="${weight_cat.id}"
         >${weight_cat.name}</option>
      `
   }
}

const participants_render = (participants) => {
   place_for_participants.innerHTML = ''

   for (let weight_cat of participants) {
      place_for_participants.innerHTML += `
         <div class='toss__right__participant' draggable='True'>
            ${weight_cat.firstName}
            ${weight_cat.lastName}
            ${weight_cat.thirdName}
         </div>
      `

      if (participants.count == 0) {
         place_for_participants.innerHTML = 'not found'
      }
   }
}

get_from_api(`http://127.0.0.1:8000/api/tournaments/${toss_title.value}/weight_categories`, weight_categories_render)

// if (weight_categories) {
//    console.log(weight_categories)
//    weight_categories_render(weight_categories)
// }

weight_category.addEventListener('change', (e) => {
   let weights = get_from_api(`/api/tournaments/${toss_title.value}/weight_categories/${e.target.value}/weights`, weight_render)
   
   // toss__title__weight__category.innerHTML = e.target.value
   weight_category_select = e.target.value
})

// http://127.0.0.1:8000/api/tournaments/grant-pri-the-best-xxi-2023-may/weight_categories/3/weights/15/participants

weight.addEventListener('change', (e) => {
   get_from_api(`/api/tournaments/${toss_title.value}/weight_categories/${weight_category_select}/weights/${e.target.value}/participants`, participants_render)
})
