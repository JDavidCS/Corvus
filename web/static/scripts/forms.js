function sendRequest(e, form) {
  e.preventDefault()
  for (const pair of new FormData(form)) {
   console.log(pair)
  }
}


const form = document.querySelector('#signup')

if (form) {
  form.addEventListener('submit', function(e) {
    sendRequest(e, form)
  })
}
