Title: Jupyter environment setup
Author: Marc
Date: 2015-12-22 14:07:00
Slug: jupyter-environment-setup
Tags: Python,Data Mining

This is a short note about how I set up my "data scientist" environment. Different people have different tastes, but what I use, and what I set up is:

- <li>**conda** for environment and package management (equivalent to virtualenv and pip to say)</li><li>Latest **Python** (yes, Python 3)</li><li>**Jupyter**&nbsp;(aka IPython notebook)</li><li>Disable all the autocomplete quotes and brackets stuff, that comes by default with Jupyter</li><li>Set the IPython backend for matplotlib</li>
<div>So, we download Anaconda from:&nbsp;https://www.continuum.io/downloads (Linux 64 bits, Python 3, in my case). We install it by:</div><div>
</div><blockquote class="tr_bq">bash&nbsp;Anaconda3-2.4.1-Linux-x86_64.sh</blockquote><div>
</div><div>We can either restart the terminal, or type the next command, so we start using conda environment:</div><div>
</div><blockquote class="tr_bq">. ~/.bashrc</blockquote><div>
</div><div>We can update conda and all packages:</div><div>
</div><blockquote class="tr_bq">conda update conda &amp;&amp; conda update --all</blockquote><div>
</div><div>Then we create a new conda environment (this way we can change package versions without affecting the main conda packages). We name it myenv and specify the packages we want (numpy, pandas...).</div><div>
</div><blockquote class="tr_bq">conda create --name myenv jupyter numpy scipy pandas matplotlib scikit-learn bokeh</blockquote><div>
</div><div>We activate the new environment:</div><div>
</div><blockquote class="tr_bq">source activate myenv</blockquote><div>
</div><div>Now we have everything we wanted installed, let's change the configuration.</div><div>
</div><div>We start by creating a default ipython profile.</div><div>
</div><blockquote class="tr_bq">ipython profile create</blockquote><div>
</div><div>Then we edit the file ~/.ipython/profile_default/ipython_kernel_config.py and we add the next lines to make matplotlib display the images with the inline backend, and with a decent size:</div><div>
</div><blockquote class="tr_bq">c.InteractiveShellApp.matplotlib = 'inline' c.InlineBackend.rc = {'font.size': 10, 'figure.figsize': (18., 9.), 'figure.facecolor': 'white', 'savefig.dpi': 72, 'figure.subplot.bottom': 0.125, 'figure.edgecolor': 'white'} </blockquote>
<div>
</div><div>To disable autoclosing brackets, run in a notebook:</div><div>
</div><pre style="background-color: #f6f8fa; border-radius: 3px; box-sizing: border-box; color: #24292e; font-family: SFMono-Regular, Consolas, &quot;Liberation Mono&quot;, Menlo, Courier, monospace; font-size: 11.9px; font-stretch: normal; line-height: 1.45; overflow: auto; padding: 16px; word-break: normal; word-wrap: normal;"><span class="pl-k" style="box-sizing: border-box; color: #d73a49;">from</span> notebook.services.config <span class="pl-k" style="box-sizing: border-box; color: #d73a49;">import</span> ConfigManager
c <span class="pl-k" style="box-sizing: border-box; color: #d73a49;">=</span> ConfigManager()
c.update(<span class="pl-s" style="box-sizing: border-box; color: #032f62;"><span class="pl-pds" style="box-sizing: border-box;">'</span>notebook<span class="pl-pds" style="box-sizing: border-box;">'</span></span>, {<span class="pl-s" style="box-sizing: border-box; color: #032f62;"><span class="pl-pds" style="box-sizing: border-box;">"</span>CodeCell<span class="pl-pds" style="box-sizing: border-box;">"</span></span>: {<span class="pl-s" style="box-sizing: border-box; color: #032f62;"><span class="pl-pds" style="box-sizing: border-box;">"</span>cm_config<span class="pl-pds" style="box-sizing: border-box;">"</span></span>: {<span class="pl-s" style="box-sizing: border-box; color: #032f62;"><span class="pl-pds" style="box-sizing: border-box;">"</span>autoCloseBrackets<span class="pl-pds" style="box-sizing: border-box;">"</span></span>: <span class="pl-c1" style="box-sizing: border-box; color: #005cc5;">False</span>}}})</pre>
<div>
</div>