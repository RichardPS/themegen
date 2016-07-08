% themename = siteinfo['theme_name']
% pageScript = siteinfo['page_script']
% zipName = siteinfo['zipName']
% page_title = page_title

{{page_title}}
<hr>
% for item in pageScript:
	{{item}}<br>
% end
<hr>

<a href="{{zipName}}">Download Theme</a>
<hr>
<a href="/">Return Home</a>