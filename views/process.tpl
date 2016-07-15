% themename = siteinfo['theme_name']
% pageScript = siteinfo['page_script']
% zipname = siteinfo['zipname']+'.zip'
% page_title = page_title

{{page_title}}
<hr>
% for item in pageScript:
	{{item}}<br>
% end
<hr>

<a href="{{zipname}}">Download Theme</a>
<hr>
<a href="/">Return Home</a>