window.onload=getCSS();
function getCSS(){
	var display = "bg-0.png"
	var datetoday = new Date();
	var timenow=datetoday.getTime();
	datetoday.setTime(timenow);
	var thehour = datetoday.getHours();
	if (thehour>8 && thehour<18)
	    display = "bg-0.png";
	else if (thehour>18 && thehour<24 || thehour>0 && thehour<8)
	    display = "bg-1.png";
	
	var css ='<style type="text/css">body{background-image: url("../static/img/'+display+'");background-size: cover;}</style>';
    document.write(css);
}
