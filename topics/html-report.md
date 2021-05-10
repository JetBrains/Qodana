[//]: # (title: HTML report)

### Local run

Due to JavaScript security restrictions, the generated report cannot be viewed via the `file://` protocol (that is, by double-clicking the `index.html` file). Instead, you can use the `--show-report` argument to serve the HTML report locally via the `http://` protocol.
To view the report in the already generated `report/` folder:
- Docker

  ```shell
   docker run -it --rm -p 8000:80 -v $(pwd)/report:/usr/share/nginx/html nginx
   ```  
- Python  
  If you have python installed, you can serve current folder content via:

  ```shell
   cd report/
   python2 -m SimpleHTTPServer
   # or
   python3 -m http.server
   ```
- PHP  
  If you have PHP installed, you can serve current folder content via:

  ```shell
   cd report/
   php -S localhost:8000
   ```

The report is available at [http://localhost:8000](http://localhost:8000). You can stop the web server by pressing `Ctrl-C`.
