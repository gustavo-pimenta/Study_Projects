function openNewTab() {
	chrome.tabs.query({active: true}, function(tabs) {		
		chrome.tabs.query({}, function(tabs) {						 
			chrome.tabs.reload(tabs[0].id)
		})
	});
}

//var count=new Number();
var count = 10;

function start(){

    if((count - 1) >= 0){
        count = count-1;
    }

    if(count < 1){
            openNewTab();
            count = 10;
    }

    setTimeout('start()',1000);
    
}

