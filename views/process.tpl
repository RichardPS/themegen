%themename = siteinfo['theme_name']
%themeslug = siteinfo['theme_slug']
%sitemap = siteinfo['site_map']
%pageScript = siteinfo['page_script']
{{themename}}
{{themeslug}}
<ul>
% for item in sitemap:
	<li>{{item}}</li>
% end
</ul>
<hr>
%for item in pageScript:
	{{item}}<br>
%end