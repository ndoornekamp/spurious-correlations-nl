import { getConfig } from './graphConfig.js';
import { addDownloadButton } from './downloadGraph.js';

const canvas = document.getElementById("line-chart");

if (canvas) {
    const dataset = JSON.parse(canvas.dataset.result);
    const config = getConfig(dataset);
    const chart = new Chart(canvas.getContext("2d"), config);
    addDownloadButton(canvas, chart);
}
