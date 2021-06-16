var ctx = document.getElementById('payroll')


function getData() {
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
      let payment = 0
      let arl = 0
      let health = 0
      let pension = 0
      let p_f = 0
      for (let i in data){
        arl += data[i]['arl']
        payment = data[i]['salary']
        health = data[i]['health']
        pension = data[i]['pension']
        p_f = data[i]['parafiscales']
      }
      if (payment === 0) {
        payment += 1
      }
      var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['Salarios', 'ARL', 'Salud', 'Pensión', 'Para Fiscales'],
          datasets: [{
            label: '# of Votes',
            data: [payment, arl, health, pension, p_f],
            backgroundColor: [
              'rgba(255, 99, 132)',
              'rgba(54, 162, 235)',
              'rgba(255, 206, 86)',
              'rgba(75, 192, 192)',
              'rgba(153, 102, 255)',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
            ],
            borderWidth: 1
          }]
        },
      });
    }
  })
}

getData()
