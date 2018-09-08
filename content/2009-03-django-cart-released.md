Title: django-cart released!
Author: Marc
Date: 2009-03-25 18:50:00
Slug: django-cart-released
Tags: Django

Until now, if you had to develop an online store in django, you had two options, use [satchmo](http://www.satchmoproject.com/), or write your own code. Satchmo is a huge application that tries to provide everything for all the cases, so for a simple shop you've to deal with hundreds of features that you're not going to use, and in some case it won't be enough flexible.

So what I've not any complain for satchmo, the fact is that is not the ideal solution for some cases as some small shops with few options.

With that said, this post is to announce the release of a new project that could help some people to do simple web shops in a very simple way. This project is [django-cart](http://code.google.com/p/django-cart/).

While django-cart already existed, it was an unfinished (and unmaintained) project by Eric Woundenberg, to whom I'm very thankful for letting reuse it's project, and avoid confusion.

So, what's django-cart. Django Cart is basically a django application that provides a Cart class, with add/remove/update and get methods to be used for storing products. The products model isn't included in the application, so you can define your products with the fields you need. Then you just need something like...

    ::::
    
    product_to_add = MyProductModel.objects.get(id=whatever)
    cart = Cart(request)
    cart.add(product_to_add, product_to_add.price)
    

and your product will be saved on the database, on a session based cart. Getting the content of the cart is as easy as itering the cart instance.

And basically that's it. More information is available on the project page. Just note that the current version of the application is unstable, and hasn't been tested enough, so feel free to use it, but consider that you'll have to test it by yourself and report/fix some bugs.

I hope all you like it!