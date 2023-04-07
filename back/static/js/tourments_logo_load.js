const logos_upload = document.getElementById('logos_upload');

logos_upload.addEventListener('change', (e) => {
   console.log(e.target.files[0]);
})