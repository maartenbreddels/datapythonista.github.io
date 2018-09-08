Title: Parsing unescaped urls in django
Author: Marc
Date: 2009-02-19 15:40:00
Slug: parsing-unescaped-urls-in-django
Tags: Django

Modern browsers escape urls automatically before sending them to the server, but what happens if your application serves http requests to clients that doesn't escape urls?

The answer is that can get unexpected results if you server works in Django (and probably in any python framework/application). That's because python's BaseHTTPServer.BaseHTTPRequestHandler handles urls according to standards, not from a human point of view.

Let's see with an example, consider the next request:

<code>http://vaig.be/identify_myself?name=Marc Garcia&amp;country=Catalonia</code>

if you request it with a browser, it will escape the space in the url, so the server will get:

<code>http://vaig.be/identify_myself?name=Marc%20Garcia&amp;country=Catalonia</code>

but what if the client uses, for example, python's urllib2.urlopen without escaping (using urllib.quote)? Of course it is a mistake, but you, as server side developer can't control your clients.

In that case the whole request that server receives is:

<code>GET http://vaig.be/identify_myself?name=Marc Garcia&amp;country=Catalonia HTTP/1.1</code>

and after being processed (splitted) by python's BaseHTTPServer.BaseHTTPRequestHandler, what we'll get from django is:

<code>
request.method == 'GET'
request.META['QUERY_STRING'] == 'name=Marc'
request.META['SERVER_PROTOCOL'] == 'Garcia&amp;country=Catalonia HTTP/1.1'
</code>

so our request.GET dictionary will look like:

<code>request.GET == {'name': 'Marc'}</code>

what is not the expected value (from a human point of view).

So, what we can do for avoiding this result is quite easy (and of course tricky), and is getting the GET values not from django request.GET dictionary but from the one returned by this function:

<code>
def _manual_GET(request):
&nbsp;&nbsp;&nbsp;&nbsp;if ' ' in request.META['SERVER_PROTOCOL']:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;query_string = ' '.join(
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[request.META['QUERY_STRING']] +
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;request.META['SERVER_PROTOCOL'].split(' ')[:-1]
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;args = query_string.split('&amp;')
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = {}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for arg in args:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key, value = arg.split('=', 1)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result[key] = value
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return result
&nbsp;&nbsp;&nbsp;&nbsp;else:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return request.GET
</code>