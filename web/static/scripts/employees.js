function listEmployees() {
  let headers = new Headers()
  headers.append('Content-Type', 'application/json')
  headers.append('Authorization', 'Basic '
    + btoa(sessionStorage.getItem('token') + ':unused'))
  const req = new Request('http://127.0.0.1:5000/api/employees', {
    method: 'GET',
    headers: headers,
    mode: 'cors'
  })
  fetch(req).then(response => {
    if (response.ok) {
      return response.json()
    } else {
      return null
    }
  }).then(data => {
    if (data) {
      for (let i in data){
        document.getElementById('table').innerHTML +=
          `<tr class="table__tr">
              <td id="id" class="table__td tr__id">${data[i]['id']}</td>
              <td id="forenames" class="table__td column">${data[i]['forenames']}</td>
              <td id="names" class="table__td column ">${data[i]['names']}</td>
              <td id="position" class="table__td less">${data[i]['position']}</td>
              <td id="c_type" class="table__td less">${data[i]['c_type']}</td>
              <td id="salary" class="table__td table__salary column">$${data[i]['salary']}</td>
           </tr>`
      }
    }
  })
}

listEmployees()
