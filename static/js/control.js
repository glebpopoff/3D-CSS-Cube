$(function(){
	
	$('a.simupkey').live('click', function(evt) {
		sendControlCmd('up');
	});
	
	$('a.simdownkey').live('click', function(evt) {
		sendControlCmd('down');
	});
	
	$('a.simrightkey').live('click', function(evt) {
		sendControlCmd('right');
	});
	
	$('a.simleftkey').live('click', function(evt) {
		sendControlCmd('left');
	});
});

function sendControlCmd(cmd)
{
	var ts = new Date().getTime();
	$.ajax({
		  url: "/control/id/" + sessionId + "/dir/" + cmd + "?time=" + ts,
		  context: document.body,
		  success: function(){
		  }
		});
}