[//]: # (title: Open an HTML report)

Due to JavaScript security restrictions, the generated report cannot be viewed via the `file://` protocol (that is, by double-clicking the `index.html` file). Instead, you can use the `--show-report` argument to serve the HTML report locally via the `http://` protocol.
If you have Docker, Python, or PHP installed, you can view the report in the already generated `report/` folder as follows:
- Docker

  ```shell
   docker run -it --rm -p 8000:80 -v $(pwd)/report:/usr/share/nginx/html nginx
   ```  
- Python  
  
  ```shell
   cd report/
   python2 -m SimpleHTTPServer
   # or
   python3 -m http.server
   ```
- PHP  
  
  ```shell
   cd report/
   php -S localhost:8000
   ```

The report is available at [http://localhost:8000](http://localhost:8000). You can stop the web server by pressing `Ctrl-C`.
