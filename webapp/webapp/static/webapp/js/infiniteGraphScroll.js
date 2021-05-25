const graphContainer = document.getElementById("graph-container");
let nofPlots = 5

function addCanvas() {
    const div = document.createElement('div')
    const canvas = document.createElement("canvas")
    div.style.width = "75%"
    canvas.classList.add('line-chart')
    div.append(canvas)
    graphContainer.appendChild(div)
    return canvas
}

async function addPlot(datasetIndex) {
    canvas = addCanvas()
    const ctx = canvas.getContext("2d")
    console.log(ctx)

    dataset = await fetchData(datasetIndex)
    const data = {
        datasets: [
        {
          data: dataset.series1.values,
          label: dataset.series1.axis_label.english,
          yAxisID: 'y',
          backgroundColor: '#CD5C5C',
          borderColor: '#CD5C5C',
        },
        {
          data: dataset.series2.values,
          label: dataset.series2.axis_label.english,
          yAxisID: 'y1',
          backgroundColor: '#ADD8E6',
          borderColor: '#ADD8E6',
        }],
        labels: [2014, 2015, 2016, 2017, 2018, 2019, 2020]
    };
    const title = dataset.series1.title.english.concat(" vs. ", dataset.series2.title.english)

    const config = {
    type: 'line',
    data: data,
    options: {
        responsive: true,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        stacked: false,
        plugins: {
            title: {
                display: true,
                text: title
            }
        },
        scales: {
              y: {
                  type: 'linear',
                  display: true,
                  position: 'left',
              },
              y1: {
                  type: 'linear',
                  display: true,
                  position: 'right',

                  // grid line settings
                  grid: {
                      drawOnChartArea: false, // only want the grid lines for one axis to show up
                    },
              },
            }
        },
    };
    new Chart(ctx, config)
}

async function fetchData(datasetIndex) {
    const response = await fetch('/data', {method: 'POST', body: JSON.stringify({index: datasetIndex})})
    const data = await response.json()
    return data
}

window.onscroll = function(ev) {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        nofPlots++
        addPlot(nofPlots)
    }
};

function init(initialNofPlots) {
    for (i = 0; i < initialNofPlots; i++) {
        addPlot(i)
    }
}

init(nofPlots);