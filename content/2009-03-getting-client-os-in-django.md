Title: Getting client OS in Django
Author: Marc
Date: 2009-03-11 13:30:00
Slug: getting-client-os-in-django
Tags: Django

Some times it can be useful to serve our site content with little differences depending on the visitor operating system. I really think it's a bad idea changing the content or doing some big changes, depending on it, but this post can be useful for it as well.

So, while most time just some Javascript is used to customize user experience based on its operating system, few times it'll also be useful to do it in the server side.

For those cases, here you've a simple context processor that will make available a template variable named "platform" which content can be "Linux", "Mac" or "Windows".


    ::::
    
    import re
    
    def user_agent(request):
        ''' 
        Context processor for Django that provides operating system
        information base on HTTP user agent.
        A user agent looks like (line break added):
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.6) \
        Gecko/2009020409 Iceweasel/3.0.6 (Debian-3.0.6-1)"
        '''
        print 'user_agent'
        # Mozilla/5.0
        regex = '(?P<application_name>\w+)/(?P<application_version>[\d\.]+)'
        regex += ' \('
        # X11
        regex += '(?P<compatibility_flag>\w+)'
        regex += '; '
        # U 
        regex += '(?P<version_token>[\w .]+)'
        regex += '; '
        # Linux i686
        regex += '(?P<platform_token>[\w .]+)'
        # anything else
        regex += '; .*'
    
        user_agent = request.META['HTTP_USER_AGENT']
        result = re.match(regex, user_agent)
        if result:
            result_dict = result.groupdict()
            full_platform = result_dict['platform_token']
            platform_values = full_platform.split(' ')
            if platform_values[0] in ('Windows', 'Linux', 'Mac'):
                platform = platform_values[0]
            elif platform_values[1] in ('Mac',):
                # Mac is given as "PPC Mac" or "Intel Mac"
                platform = platform_values[1]
            else:
                platform = None
        else:
            full_platform = None
            platform = None
    
        return {
            'user-agent': user_agent,
            'full_platform': full_platform,
            'platform': platform,
        }   
    


To make it work just copy the code in a file


    ::::
    myproject/myapp/context_processors.py

add it to context processors in settings


    ::::
    TEMPLATE_CONTEXT_PROCESSORS = ('myproject.myapp.context_processors.user_agent', [...])

and don't forget to add the RequestContext parameter if you are processing your template with render_to_response and want the variable available 


    ::::
    from django.template import RequestContext
    [...]
    render_to_response('mytemplate.html', mycontext, <span style="font-weight:bold;">RequestContext(request)</span>)


Then you'll be able to do something like that in your templates:

    ::::
    
        <p>You are a {{ platform }} user.</p>
