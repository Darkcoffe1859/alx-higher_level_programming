$(document).ready(function() {
	$.ajax({
	url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
	type: 'GET',
	success: function(response) {
	$('#character').text('Character name: ' + response.name);
	},
	error: function(error) {
	console.log('Error fetching character data:', error);
	}
	});
	});
