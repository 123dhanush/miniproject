function mysession(){
	var x=parseInt(document.getElementById('nsessions').value);
	for(var i=1;i<=x;i++)
	{
		document.getElementById('paraid').innerHTML="Students for Session "+i+": <input type='text' id='no"+i+"'><br>";
	}
}
