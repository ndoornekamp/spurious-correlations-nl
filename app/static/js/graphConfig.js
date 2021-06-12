export function getConfig(dataset) {
	const data = {
		datasets: [
			{
				data: dataset.series1.values,
				label: dataset.series1.localized_axis_label,
				yAxisID: "y",
				backgroundColor: "#CD5C5C",
				borderColor: "#CD5C5C",
			},
			{
				data: dataset.series2.values,
				label: dataset.series2.localized_axis_label,
				yAxisID: "y1",
				backgroundColor: "#ADD8E6",
				borderColor: "#ADD8E6",
			},
		],
		labels: [2014, 2015, 2016, 2017, 2018, 2019, 2020],
	};

	const title = [dataset.series1.localized_title, " vs. ", dataset.series2.localized_title, `ρ = ${dataset.correlation.toFixed(4)}`];

	const canvasBackgroundColorPlugin = {
		id: "custom_canvas_background_color",
		beforeDraw: (chart) => {
			const ctx = chart.canvas.getContext("2d");
			ctx.save();
			ctx.globalCompositeOperation = "destination-over";
			ctx.fillStyle = "white";
			ctx.fillRect(0, 0, chart.width, chart.height);
			ctx.restore();
		},
	};

	const config = {
		type: "line",
		data: data,
		plugins: [canvasBackgroundColorPlugin],
		options: {
			responsive: true,
			interaction: {
				mode: "index",
				intersect: false,
			},
			stacked: false,
			plugins: {
				title: {
					display: true,
					text: title,
				},
			},
			scales: {
				y: {
					type: "linear",
					display: true,
					position: "left",
					title: {
						display: true,
						text: dataset.series1.localized_axis_label,
					},
				},
				y1: {
					type: "linear",
					display: true,
					position: "right",
					title: {
						display: true,
						text: dataset.series2.localized_axis_label,
					},

					// grid line settings
					grid: {
						drawOnChartArea: false, // only want the grid lines for one axis to show up
					},
				},
			},
		},
	};
	return config;
}