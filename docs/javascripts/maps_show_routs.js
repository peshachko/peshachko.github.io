// coordinates are in lat-lng (required by leaflet)
function createMap(id) {
	fetch(`/events/routes/${id}.json`)
		.then(response => response.json())
		.then(data => {
			const center = data.center;
			const zoom = data.zoom;
			const coordinates = data.coordinates;
			const start = coordinates.at(0);
			const end = coordinates.at(-1);
			const loop = start[0] === end[0] && start[1] === end[1];

			const map = L.map(id).setView(center, zoom);
			L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
				maxZoom: 21,
			}).addTo(map);

			L.polyline(coordinates, {
				color: 'blue',
				weight: 3,
			}).addTo(map);

			if (loop) {
				L.circleMarker(start, {
					radius: 10,
					color: 'red',
					fillColor: 'green',
					fillOpacity: 1
				})
					.addTo(map)
					.bindPopup(`<div style="text-align:center"> Начало/Край<br>${start.toString()}</div>`)
					.openPopup();
			} else {
				L.circleMarker(end, {
					radius: 8,
					color: 'red'
				})
					.addTo(map)
					.bindPopup(`<div style="text-align:center"> Край<br>${end.toString()}</div>`)
					.openPopup();

				L.circleMarker(start, {
					radius: 8,
					color: 'green'
				})
					.addTo(map)
					.bindPopup(`<div style="text-align:center"> Начало<br>${start.toString()}</div>`)
					.openPopup();
			}
		})
}

document$.subscribe(() => {
	document.querySelectorAll("div.leaflet-map").forEach(el => {
		createMap(el.id);
	});
});
