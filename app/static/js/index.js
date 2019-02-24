
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import Chart from 'chart.js';

var xhr = new XMLHttpRequest();

xhr.addEventListener('load', function() {
  if (this.status == 200) {
    var result = JSON.parse(this.responseText);
    var parties = result.dataset
    var labels = result.labels
    var partyData = [];
    var labelData = [];

    for (var key in labels) {
      var field = labels[key];
      if (field != 'Afkorting' && field != 'Naam') {
        labelData.push(field);
      }
    }

    parties.forEach(function(party) {
      var data = [];
      for (var key in party) {
        if (key != 'Afkorting' && key != 'Naam') {
          data.push(party[key]);
        }
      }
      partyData.push({
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff',
        data: data
      });
    });

    // Graphs
    var ctx = document.getElementById('myChart')
    // eslint-disable-next-line no-unused-vars
    var myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labelData,
        datasets: partyData,
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: false
            }
          }]
        },
        legend: {
          display: false
        }
      }
    })
  }
});

xhr.open('GET', 'http://127.0.0.1:8080/statics/parliament');

xhr.send();
