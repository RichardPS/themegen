% themename = siteinfo['theme_name']
% themeslug = siteinfo['theme_slug']
% sitemap = siteinfo['site_map']
% pageScript = siteinfo['page_script']
% specialPages = siteinfo['specialPages']
% topicNames = siteinfo['topicNames']
% topicSlugs = siteinfo['topicSlugs']
% nursery = siteinfo['nursery']

{{themename}}
{{themeslug}}
<ul>
% for item in sitemap:
	<li>{{item}}</li>
% end
</ul>
<hr>
% for item in pageScript:
	{{item}}<br>
% end
<hr>
% for key, value in specialPages.iteritems():
	{{key}} - {{value}}<br>
% end
<hr>
% for item in topicNames:
	{{item}}<br>
% end
<hr>
% for item in topicSlugs:
	{{item}}<br>
% end
<hr>
{{nursery}}