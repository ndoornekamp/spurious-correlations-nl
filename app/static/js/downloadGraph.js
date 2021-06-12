export function addDownloadButton(canvas, chart) {
	const downloadButton = document.createElement("button");
	downloadButton.textContent = "Download";
	downloadButton.onclick = function () {
		const a = document.createElement("a");
		a.href = chart.toBase64Image();
		a.download = "correlation.png";
		a.click();
	};
	canvas.parentElement.append(downloadButton);
}