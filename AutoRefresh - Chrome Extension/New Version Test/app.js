function openNewTab () {
	chrome.tabs.query({active: true}, function(tabs) {		
		chrome.tabs.query({}, function(tabs) {						 
			chrome.tabs.reload(tabs[0].id)
		})
	});
}

var time = 60000;

function readdoc() {
   var time = document.getElementById('time').value;
}


setInterval(function() {openNewTab()}, time);

<script src="app.js"></script>


//var intervalo = setInterval(openNewTab(), time);
//setTimeout(function() {openNewTab()}, clearInterval(), document.onclick());
//document.onClick(clearInterval());

