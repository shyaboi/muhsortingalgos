var derta = [325, 333, 533, 452, 222, 344, 554, 366, 454, 634]
var datts = [[12, 333, 3, 5, 2, 3,554,3,454,634],[13, 343, 33, 5, 44444444, 3,554,3,454,634],[325, 333, 533, 452, 222, 344,554,366,454,634],[2, 3, 3, 5, 2, 3,4,3,4,4]]
var dertLen = derta.length

var slider = document.getElementById("test5");
var slideVal = document.getElementById('val')
// var output = document.getElementById("demo");
// output.innerHTML = slider.value;

slider.oninput = function() {
  console.log(this.value)
  slideVal.innerHTML = this.value
}


$( "#butt" ).click(()=> {
  var currentSlideVal= slideVal.innerHTML
  var str = $("#inpuut").val();
    $.post("/", {"myData": str, 'otherData':currentSlideVal},(data)=> {
          $.each(data, function( index, value ) {
                $( ".result" ).append(`<li>[${value}] : Array itteration index#: ${index}</li>`);
              });
        // console.log(data)
        console.log(str)
      });
      })
      var ctx = document.getElementById('myChart').getContext('2d');
      var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'index', 'voltron', 'dinnfds', 'fdjkdsf'],
          datasets: [{
            label: '# of Votes',
            data: derta,
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(12, 159, 64, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 159, 64, 0.2)'
              
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 159, 64, 0.2)',
              'rgba(255, 159, 64, 0.2)'
            ],
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            yAxes: [{
                ticks: {
                  beginAtZero: true
                }
              }]
            }
          }
        });
        
        
        function removeData(chart) {
          chart.data.labels.pop();
          chart.data.datasets.forEach((dataset) => {
            dataset.data.pop();
          });
          chart.update();
        }
        
        console.log(derta.length)
        setTimeout(() => {
          for (let i = 0; i < dertLen+dertLen; i++) {removeData(myChart)}  
        }, 4000);
        
        
        function addData(chart, label, data) {
          chart.data.labels.push(label);
          chart.data.datasets.forEach((dataset) => {
            dataset.data.push(data);
          });
          chart.update();
        }
   var two =  [2, 3, 3, 5, 2, 3,4,3,4,4]

    setTimeout(() => {
        for (let i = 0; i < two.length; i++) {
            let twoo = two[i]
          addData(myChart, 'things', twoo)
          
        }
      },4000);


