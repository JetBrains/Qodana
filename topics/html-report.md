[//]: # (title: Open an HTML report)

You can open HTML-formatted %product% reports using JetBrains IDEs and shell commands.

<tabs>
<tab title="JetBrains IDEs" id="open-report-ide">
<p>Starting from version 2023.2 of %product%, you can open HTML reports using IntelliJ IDEA, PhpStorm, WebStorm, Rider, 
GoLand, PyCharm, and Rider as explained in the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports"/> section.</p> 
<p>In this case, your IDE needs to be installed via <a href="https://www.jetbrains.com/toolbox-app/">JetBrains Toolbox App</a>.</p>

</tab>
<tab title="Shell commands" id="open-report-shell">
<p>When you run %product% with the <code>--save-report</code> option, it stores an HTML version of the report in 
<code>/data/results/report</code>. This directory is typically mounted via Docker to let you view the HTML report later, 
independently of running %product%. Due to JavaScript security restrictions, you cannot browse the HTML report by 
double-clicking the <code>index.html</code> file. Instead, the HTML report needs to be served via a web server, and you 
can run the Dockerized version of nginx, or invoke the Python or PHP built-in web servers as shown below.</p>

<procedure>
<step>After running %product%, navigate to the <code>report</code> folder and make sure that the 
<code>index.html</code> file is present there.</step>
<step>
    <p>Serve the report using the web server of your choice:</p>
    <tabs>
        <tab title="Dockerized version of nginx">
            <code-block prompt="$">
                docker run -it --rm -p 8000:80 \
                  -v $(pwd):/usr/share/nginx/html nginx
            </code-block>
            <p>In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.</p>
        </tab>
        <tab title="Python 2">
            <code-block prompt="$">
                python2 -m SimpleHTTPServer
            </code-block>
            <p>In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.</p>
        </tab>
        <tab title="Python 3">
            <code-block prompt="$">
                python3 -m http.server
            </code-block>
            <p>In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.</p>
        </tab>
        <tab title="PHP">
            <code-block prompt="$">
                php -S localhost:8000
            </code-block> 
            <p>In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.</p>
        </tab>
    </tabs>    
</step>
</procedure>
</tab>
</tabs>
