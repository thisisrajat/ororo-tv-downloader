# ororo-tv-downloader
Creates an HTML file containing download links to all the episodes by parsing Ororo's TV Show URL 

Usage:

```
    python ororo.py URL
```

### By Using HTML File:
Make a HTML file in the same directory where ororo.py script exists. Now visit http://ororo.tv and find the TV show you want to download. After you're on that TV shows page whose url is structured like this: http://ororo.tv/en/shows/[tv-show-name], you need to copy the source code of that page in the html file we previously created. In most modern browsers you can view source of a page by hitting CTRL + U simultaneously or alternatively you can always find an option to view source in settings. After you've copied the html of the TV Show to the html file that resides in the same directory as the ororo.py script, you can run the script like this ```python ororo.py HTML_FILE_NAME```