This is a simple-to-use CLI YouTube video downloader I made in Python.

# Examples
<!-- **Note:** YouTube URLs contain a question mark, which confuses some shells. If this is the case with your shell, wrap the URL in single quotes or double quotes to tell your shell to ignore it. -->
**Note:** If your shell gets unhappy when you use a full URL, try wrapping the URL in single or double quotes; example: `ytd https://www.youtube.com/watch?v=thOifuHs6eY` -> `ytd 'https://www.youtube.com/watch?v=thOifuHs6eY'` or `ytd "https://www.youtube.com/watch?v=thOifuHs6eY"`

Download from a URL `ytd https://www.youtube.com/watch?v=thOifuHs6eY`

Download from a very short URL (aka just the video id) `ytd thOifuHs6eY`

This also works `ytd tch?v=thOifuHs6eY`, any portion of the URL works :)

Download from the URL in your clipboard `ytd -c`

Get some help `ytd -h` (...with the parameters, the help page cannot offer life advice)

# Installation
### Linux/MacOS
1. Download the executable binary for your system (downloads are at the bottom)
2. Drag that into `/usr/bin`, `/usr/local/bin`, or whatever bin directory you want (make sure the terminal recognizes the custom bin directory if that's what you're doing)
3. Use the `ytd` command like the examples above demonstrate :)

### Windows
I'll be honest, I'm not sure where to place stuff on Windows; people on the internet suggest Program Files, so maybe you could create a folder in `C:\Program Files`, name it "ytd", then place the .exe inside of it. Then, I'd add that `ytd` folder to the PATH. So, start typing in "Environment variables" into the Start Menu search, open the application, head to Advanced, click on Environment Variables, select "Path", click on "Edit...", press "New", paste in the path to that ytd folder, press "OK" on everything, and you should be good to go :).

# Downloads
**Linux**: <a href='resources/files/ytd' download>Click here to download</a>

**MacOS**: WIP

**Windows**: WIP