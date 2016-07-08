<!DOCTYPE html>
<html>
<head>
<title>{{page_title}}</title>
<link rel="stylesheet" href="style.css" type="text/css">
<script src="common.js" type="text/javascript"></script>
</head>
<body>

<form action="/process" method="post">
	<textarea name="sitemap" rows="25" cols="100"></textarea><br>
	<input name="themename" type="text"><br>
	<input type="checkbox" name="nursery" value="true">Check if a nursery site<br>
	<input value="Submit" type="submit">
</form>
<h3>Special Page Keys</h3>
<ul style="list-style-type: none;">
	<li>**tour <span style="padding-left: 25px;">360 Tour (/special/virtual-tour)</span></li>
	<li>**news <span style="padding-left: 25px;">News (/stream/news/full/1/-//)</span></li>
	<li>**diary <span style="padding-left: 25px;">List View (/diary/list/)</span></li>
	<li>**calendar <span style="padding-left: 25px;">Grid View (diary_grid)</span></li>
	<li>**letter <span style="padding-left: 25px;">Newsletters (/stream/newsletters/full/1/-//)</span></li>
	<li>**kids <span style="padding-left: 25px;">Kid's Zone (/special/kidszone)</span></li>
</ul>
<br>
<a href="/generic">Get Build Template</a>
</body>
</html>