console.log('Upload JS')

const download = document.querySelector('#download')
const upload = document.querySelector('#upload-list')

const participants = document.querySelectorAll('.participant')

// Download
download.addEventListener('click', () => {
   for (const participant in participants) {

      console.log(participant)
   }
})

upload.onclick = () => {

}