# datapythonista.github.io

https://datapythonista.github.io

This is the personal page of Marc Garcia
[@datapythonista](https://datapythonista.github.io).

It has two main components:
- Home page (index.html) using the
  [Freelancer](http://startbootstrap.com/template-overviews/freelancer/)
  template
- Blog using [Pelican](https://blog.getpelican.com/)

To add a new entry to the blog:
- Create a new markdown file/notebook in `content/`
- Run `pelican content` (requires that dependencies in `environment.yml` are
  installed
- `git push`

If the `attila` submodule is not initialized locally, it can be fetched with
`git submodule update --init attila/`

The whole website is hosted in GitHub pages. To check it locally, a server can
be started with `python -m http.server`

To subscribe to the blog, the feed is available at https://datapythonista.github.io/blog/atom.xml
