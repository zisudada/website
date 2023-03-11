function getCSS(){
	var display = "bg-0.png"
	var datetoday = new Date();
	var timenow=datetoday.getTime();
	datetoday.setTime(timenow);
	var thehour = datetoday.getHours();
	if (thehour<12)
		display = "bg-0.png";
	else if (thehour>12)
	//样式表的名称，或者你可以加上路径
		display = "bg-1.png";
	else
		display = "bg-2.png";
	//(...想要更多再加即可...)
	
	var css ='<style type="text/css">body{background-image: url("../static/img/'+display+'");background-size: cover;}</style>';
	document.write(css);
}
