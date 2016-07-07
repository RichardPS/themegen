% themename = siteinfo['theme_name']
% pageScript = siteinfo['page_script']
% zipName = siteinfo['zipName']
% page_title = page_title

{{page_title}}

% for item in pageScript:
	{{item}}<br>
% end
<hr>

<a href="{{zipName}}">Click Here</a>
<hr>
<a href="/">Return Home</a>