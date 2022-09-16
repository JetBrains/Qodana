[//]: # (title: Open an HTML report)

When you run %product% with the `--show-report` option, it starts a web server for immediate browsing the results.

When you run %product% with the `--save-report` option, it stores an HTML version of the report in `/data/results/report`.
This directory is typically mounted via Docker to let you view the HTML report later, independently of running %product%.
Due to JavaScript security restrictions, you cannot browse the HTML report by double-clicking the `index.html` file.
Instead, the HTML report needs to be served via a web server, and you can run the Dockerized version of nginx, or 
invoke the Python or PHP built-in web servers as shown below.

<procedure>
<step>After running %product%, navigate to the <code>report</code> folder and make sure that the 
<code>index.html</code> file is present there.</step>
<step>
    <p>Serve the report using the web server of your choice:</p>
    <tabs>
        <tab title="Dockerized version of nginx">
            <code style="block" prompt="$">
                docker run -it --rm -p 8000:80 \
                  -v $(pwd):/usr/share/nginx/html nginx
            </code>
        </tab>
        <tab title="Python 2">
            <code style="block" prompt="$">
                python2 -m SimpleHTTPServer
            </code>
        </tab>
        <tab title="Python 3">
            <code style="block" prompt="$">
                python3 -m http.server
            </code>
        </tab>
        <tab title="PHP">
            <code style="block" prompt="$">
                php -S localhost:8000
            </code> 
        </tab>
    </tabs>    
</step>
<step>
    In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.
</step>
</procedure>