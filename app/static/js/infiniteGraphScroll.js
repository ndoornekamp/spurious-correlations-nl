import { getConfig, addDownloadButton, addSources } from './graphs.js';

const graphContainer = document.getElementById("graph-container");
let nofPlots = 5;

function addCanvas() {
	const div = document.createElement("div");
	div.classList.add("graph");
	const canvas = document.createElement("canvas");
	canvas.classList.add("line-chart");
	div.append(canvas);
	graphContainer.appendChild(div);

	return canvas;
}

async function addPlot(datasetIndex) {
	const canvas = addCanvas();
	const dataset = await fetchData(datasetIndex);
	const config = getConfig(dataset);
	const chart = new Chart(canvas.getContext("2d"), config);
	return [canvas, chart, dataset];
}

async function fetchData(datasetIndex) {
	const response = await fetch("/data", {
		method: "POST",
		body: JSON.stringify({ index: datasetIndex }),
	});
	const data = await response.json();
	return data;
}

window.onscroll = async function (ev) {
	if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
		nofPlots++;
		const [canvas, chart] = await addPlot(nofPlots);
		addDownloadButton(canvas, chart);
	}
};

async function init(initialNofPlots) {
	for (let i = 0; i < initialNofPlots; i++) {
		const [canvas, chart, dataset] = await addPlot(i);
		addSources(canvas, dataset);
		addDownloadButton(canvas, chart);
	}
}

init(nofPlots);
