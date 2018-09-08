Title: Compare two XML strings in Python
Author: Marc
Date: 2008-08-28 19:05:00
Slug: compare-two-xml-strings-in-python
Tags: Development,IT

I had to compare two XML strings for some unit tests, and if you want to do it without considering the indentation, or the newlines, it is a little bit tricky.<br/><br/>I thought that parsing the original xml and returning it again (using minidom), I'd got a raw string without any meaningless space, or any newline, but actually it returned the original string. Using toprettyxml() method also returns a trivial result, based on the original string (even when you specify the indent and the newline characters).<br/><br/>So the best way I've found by now is to write a custom function that returns what I want, an XML string without any trivial character between tag and tag. Here you have the code:<br/><br/><code>def raw_xml(xml_str):<br/>&nbsp;&nbsp;&nbsp;&nbsp;from xml.dom import minidom<br/>&nbsp;&nbsp;&nbsp;&nbsp;xml = minidom.parseString(xml_str)<br/>&nbsp;&nbsp;&nbsp;&nbsp;return u''.join([unicode(line).strip() for line in xml.toprettyxml().splitlines()])<br/></code>