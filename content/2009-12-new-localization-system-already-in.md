Title: New localization system already in trunk
Author: Marc
Date: 2009-12-22 22:52:00
Slug: new-localization-system-already-in
Tags: Django,Django-i18n

Just few hours ago, Django's new localization system has been commited to trunk.<div>
</div><div>As some of you know, I did most of the work as my Google Summer of Code project, this year. Of course, together with [Jannis Leidel](http://jannisleidel.com/), who also did the final steps, including the commit.</div><div>
</div><div>Summarizing, with this change Django will format all displayed data, according to user's current locale. For example, the calendar will display Sunday as the first day for users in the States, but Monday for users from most European countries. Also it'll format numbers and dates.</div><div>
</div><div>You can check the slides I presented at DjangoCon.</div><div>[http://docs.google.com/present/view?id=dfbzs3ks_16d26xjbd9](http://docs.google.com/present/view?id=dfbzs3ks_16d26xjbd9)</div><div>
</div><div>Note that the setting is no longer USE_FORMAT_I18N (as in the slides), but USE_L10N.</div><div>
</div><div>You can also check the commit at:</div><div>[http://code.djangoproject.com/changeset/11964](http://code.djangoproject.com/changeset/11964)</div><div>
</div><div>
</div>