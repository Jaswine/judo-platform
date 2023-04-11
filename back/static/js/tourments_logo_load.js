 
// let formdata = new FormData();
// formdata.append("image", fileInput.files[0], "150003.jpg");

// Logotips
const logos = document.querySelector('#logos')
const output = document.querySelector(".print__logos");

// Sponsors
const sponsors = document.querySelector('#sponsors-logos')
const print__sponsors__logos = document.querySelector('#print__sponsors__logos')


const ShowImages = (objects, output) => {
   objects.addEventListener('change', (e) => {
      output.innerHTML = "";
      let files = e.target.files
   
      for (let i = 0; i < files.length; i++) {
         let file = files[i]
   
         if (!file.type.match('image'))
            continue;
   
         let picReader = new FileReader();
         picReader.addEventListener("load", function(event) {
            let picFile = event.target;
            let div = document.createElement("div");
            div.innerHTML = "<img class='thumbnail' src='" + picFile.result + "'" +
              "title='" + picFile.name + "'/>";
            output.insertBefore(div, null);
          });
         picReader.readAsDataURL(file);
      }
   })
}

ShowImages(logos, output)
ShowImages(sponsors, print__sponsors__logos)