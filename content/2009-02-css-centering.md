Title: CSS Centering
Author: Marc
Date: 2009-02-04 13:27:00
Slug: css-centering
Tags: 

Today I find a solution for one of the most common problems I had with CSS, vertical centering. I really don't like CSS, and one of my examples to explain why, it was the lack of a elegant way to vertical align an element inside a div.

First page I found was [http://www.jakpsatweb.cz/css/css-vertical-center-solution.html](http://www.jakpsatweb.cz/css/css-vertical-center-solution.html) that is a great post, that gets a solution but very very tricky.

Luckily while implementing that solution, I found a very is solution, described here: [http://www.w3.org/Style/Examples/007/center.html](http://www.w3.org/Style/Examples/007/center.html)

As easy as:
<code>
div.container {
  display: table-cell;
  vertical-align: middle;
}
</code>
I don't think that is very intuitive (at least for me), but it's simple.