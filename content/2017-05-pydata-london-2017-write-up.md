Title: PyData London 2017, write up
Author: Marc
Date: 2017-05-09 11:06:00
Slug: pydata-london-2017-write-up
Tags: 

This is a post about my experience at [PyData London 2017](https://pydata.org/london2017/). About what I liked, what I learnt... Note that having 4 tracks, and so many people, my opinions are very biased. If you want to know how your experience would be, it'll be amazing, but different than mine. :)

On the organization side, I think it's been excellent. Everything worked as expected, and when I've got a problem with wifi, I got it fixed literally in couple of minutes by the organizers. It was great to have sushi and burritos instead of last year sandwiches too. The slack channels were quite useful and well organized. I think the organizers deserve a 10, and that's very challenging when organizing a conference.

More on the content side, I used to attend conferences mainly for talks. But this year I decided to try other things a conference can offer (networking, sprints, unconference sessions...). Some random notes:

**<span style="font-size: x-large;">Bayesian stuff</span>**
<b>
</b>I think probabilistic models is the are of data science with a higher entry barrier. This is a personal opinion, but shared by many others, including authors:

**<i style="font-style: italic;">The Bayesian method is the natural approach to inference, yet it is hidden from readers behind chapters of slow, mathematical analysis. The typical text on Bayesian inference involves two to three chapters on probability theory, then enters what Bayesian inference is. Unfortunately, due to mathematical intractability of most Bayesian models, the reader is only shown simple, artificial examples. This can leave the user with a so-what feeling about Bayesian inference. In fact, this was the author's own prior opinion.</i>**
**[Cameron Davidson-Pilon](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)**

It looks like there is even terminology to define whether the approach used is mathematical (formulae and proofs quite cryptic to me), or computational (more focused on the implementation).

It was luxury to have at PyData once more, [Vincent Warmerdam](https://www.linkedin.com/in/vincentwarmerdam/), from the PyData Amsterdam organization. He has been one step ahead of most of us, who are more focused on machine learning (I didn't meet any frequentist so far at PyData conferences). He already gave a talk last year about the topic,&nbsp;[The Duct Tape of Heroes: Bayes Rule](https://www.youtube.com/watch?v=BiYTLb-o1Dk&amp;list=PLGVZCDnMOq0rzDLHi5WxWmN5vueHU5Ar7&amp;index=2), which was quite inspiring and make probabilistic models easier, and this year we've got another amazing talk, [SaaaS: Sampling as an Algorithm Service](https://pydata.org/london2017/schedule/presentation/36/).

After that, we managed to have an unconference session with him, where we could see more in detail the examples presented in the talk. While Markov Chain Monte Carlo or Gibbs sampling aren't straight forward to learn, I think we all learnt a lot, so we can finish learning all the details easily by ourselves.

There were other sessions about Bayesian stuff too:

- <li>[Bayesian optimisation with scikit-learn](https://pydata.org/london2017/schedule/presentation/61/" style="box-sizing: border-box; color: #337ab7; text-decoration-line: none; transition: all 295ms ease;)&nbsp;- Thomas Huijskens</li><li>[Variational Inference and Python](https://pydata.org/london2017/schedule/presentation/15/" style="box-sizing: border-box; color: #337ab7; text-decoration-line: none; transition: all 295ms ease;)&nbsp;- Peadar Coyle</li><li>[Bayesian Deep Learning with Edward (and a trick using Dropout)](https://pydata.org/london2017/schedule/presentation/33/" style="box-sizing: border-box; color: #337ab7; text-decoration-line: none; transition: all 295ms ease;)&nbsp;- Andrew Rowan</li><li>[Segmenting Channel 4 Viewers using LDA Topic Modelling](https://pydata.org/london2017/schedule/presentation/45/" style="box-sizing: border-box; color: #337ab7; text-decoration-line: none; transition: all 295ms ease;)&nbsp;- Thomas Nuttall</li>
<div>And probably some others that I'm missing, so it looks like the interest on the area is growing, and [PyMC3](https://github.com/pymc-devs/pymc3) looks to be the preferred option of most people.</div>

I've got good recommendations of books related to probabilistic models and Bayesian stuff, which shouldn't use the tough approach:

- <li>[Bayesian methods for Hackers](https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers)</li><li>[Information theory, inference and learning algorithms](http://www.inference.eng.cam.ac.uk/mackay/itila/)</li><li>[Computer age statistical inference](https://www.amazon.co.uk/Computer-Age-Statistical-Inference-Mathematical/dp/1107149894/ref=sr_1_1?s=books&amp;ie=UTF8&amp;qid=1494246251&amp;sr=1-1&amp;keywords=computer+age+statistical+inference)</li><li>[Statistical Rethinking: A Bayesian course with examples in R and Stan](https://www.crcpress.com/Statistical-Rethinking-A-Bayesian-Course-with-Examples-in-R-and-Stan/McElreath/p/book/9781482253443)</li>

There is a Meetup in London, which is the place to be to meet other Bayesians:

- <li>[Bayesian Mixer London](https://www.meetup.com/Bayesian-Mixer-London/)</li>

<span style="font-size: x-large;">**Frequentist stuff**</span>
<div style="text-align: center;">
</div>**<This space is for sale, contact the administrator of the page>**
<div style="text-align: center;">
</div><div style="text-align: left;"><span style="font-size: x-large;">**Topic modeling and Gensim**</span></div><div style="text-align: left;">
</div><div style="text-align: left;">Another topic that it looks like it's trending is topic modelling, using vector spaces for NLP, and Gensim in particular. Including Latent Dirichlet allocation, one of the most amazing algorithms I've seen in action.</div><div style="text-align: left;">
</div><div style="text-align: left;">We also got a Gensim sprint during the conference, and we could not only learn about what Gensim does, but also why is a great open source project. In the past I could see how Gensim was able to answer the most similar documents immediately, in a dataset with more than one million samples. While the documentation gives many hints on how Gensim was designed with performance in mind, it was a pleasure to participate in a Gensim sprint, and see the code and the people who make this happen in action.</div><div style="text-align: left;">
</div>Amazing also to see&nbsp;how [Lev Konstantinovskiy](https://www.linkedin.com/in/levkonst/) managed to run a tutorial, a talk, a sprint and a lightning talk, during the conference.

<b style="font-size: x-large;">From theory to practice</b>

It may be just my impression, but I'd say there have been more talks on applications of data science, and more diverse. While I remember talks on common applications like recommender systems in previous editions, I think it's been an increase on the talks on applications of all these techniques, in different areas.

To name few:
- <li>[Data science used to see the popularity of users in a Muslim dating app](https://pydata.org/london2017/schedule/presentation/38/)</li><li>[Intelligent ventilators, that make newborns breath when they need it](https://pydata.org/london2017/schedule/presentation/16/)</li><li>[Electrocardiogram analysis with time series techniques](https://pydata.org/london2017/schedule/presentation/43/)</li>
<div>Also, the astronomy/aeroespace communities look to be quite active inside the PyData community</div><div>
</div><div><span style="font-size: x-large;">**Data activism**</span></div><div>
</div><div>Another area which I'd say it's growing is data activism. Or how to use data in a social or political way. We got a keynote on fact checking, and another about analyzing data for good, to prevent money laundry with government information.</div><div>
</div><div>[DataKind UK](http://www.datakind.org/chapters/datakind-uk) looks to be the place to be, to participate on this efforts.</div><div>
</div><div><b style="font-size: x-large;">Pub Quiz</b></div>
**_That awkward moment when you thought you knew Python, but James Powell is your interviewer..._**

Ok, it wasn't an interview, it was a pub quiz, but the feeling was somehow similar. 10 years working in Python, I passed challenging technical interviews for companies such as Bank of America or Google, and at some point you start to think you know what you're doing.

Then, when you're relaxed in a pub, after and amazing but exhausting day, [James Powell](https://twitter.com/dontusethiscode) starts running the pub quiz, and you feel that you don't know anything about Python. Some new Python 3 syntax, all time namespace tricks, and so many atypical cases...

Luckily, all the dots started to connect, and I realized that few hours before, I was discussing with [Steve Holden](https://twitter.com/holdenweb) about the new edition of his book [Python in a Nutshell](http://shop.oreilly.com/product/0636920012610.do). Which sounded like an introduction to me, but it looks like it provides all Python internals.

Going back to the pub quiz, I think it's one of the most memorable moments in a conference. Great people, loads of laughs, and an amazing set of questions perfectly executed.

<span style="font-size: x-large;">**Big Data becoming smaller**</span>

As I mentioned before, my experience at the conference is very biased, and very influenced by the talks I attended, the people I met... But my impression is that the boom on big data (large deep networks, spark...) is not a boom anymore.

Of course there is a lot of people working with Spark, and researching in deep neural networks, but instead of growing, I felt like these things are loosing momentum, and people is focusing on other technologies and topics.

<b style="font-size: x-large;">Meetup groups</b>

One of the things I was interested in, was on finding new interesting meetups. I think among the most popular ones in data science are:

- <li>[https://www.meetup.com/PyData-London-Meetup/](https://www.meetup.com/PyData-London-Meetup/)</li><li>[https://www.meetup.com/London-Machine-Learning-Meetup/](https://www.meetup.com/London-Machine-Learning-Meetup/)</li><li>[https://www.meetup.com/London-ODSC/](https://www.meetup.com/London-ODSC/)</li>
<div>But I met many organizers of other very interesting meetups at the conference:</div><div>- <li>[https://www.meetup.com/London-Data-Science-Journal-Club/](https://www.meetup.com/London-Data-Science-Journal-Club/)</li><li>[https://www.meetup.com/London-Kaggle-Meetup/](https://www.meetup.com/London-Kaggle-Meetup/)</li><li>[https://www.meetup.com/project_euler/](https://www.meetup.com/project_euler/)</li><li>[https://www.meetup.com/DataKind-UK/](https://www.meetup.com/DataKind-UK/)</li>
<div><b style="font-size: x-large;">Some obvious things</b></div></div><div>
</div><div>To conclude, there are couple of tools/packages I discovered, that seemed everybody else was aware of.</div><div>
</div><div>It looks like &nbsp;at some point, instant messaging of most free software projects moved from IRC to [gitter](https://gitter.im/). There you can find data science communities, like pandas, scikit-learn, as well as other non data science, like Django.&nbsp;</div><div>
</div><div>A package that many people seems to be using, is [tqdm](https://github.com/noamraph/tqdm). You can use it over an iterator (like enumerate), and it shows a progress bar while the iterations is running. Funny, that besides being an abbreviation of progress in Arabic, i's an abbreviation for "I want/love you too much" in Spanish.</div><div>
</div><div><span style="font-size: x-large;">**What's next?**</span></div><div>
</div><div>Good news. If you couldn't attend PyData London 2017, or you didn't have enough of it, there are some things you can do:</div><div>- <li>Attend PyData Barcelona 2017, which will be as amazing as PyData London, also in English, and with top speakers like [Travis Oliphant](https://twitter.com/teoliphant) (author of scipy and numpy) or [Francesc Alted](https://twitter.com/francescalted?lang=en) (author of PyTables, Blosc, bcolz and numexpr).</li><li>Wait until the videos are published in the [PyData channel](https://www.youtube.com/user/PyDataTV) (or watch the ones from other PyData conferences)</li><li>Join one of the 55 [PyData meetups](https://www.meetup.com/pro/pydata/) around the world, or start yours (check [this document](https://docs.google.com/document/d/1ozK-MXUEANuO-xN3tQSCQ7AaqOkubKBeivqC3s-gB8I/edit) to see how, [NumFOCUS](https://www.numfocus.org/) will support you).</li><li>Join one of the other conferences happening later this year in Paris, Berlin, EuroPython in Italy, Warsaw... You can find all them at&nbsp;[https://pydata.org/](https://pydata.org/)</li>
</div>