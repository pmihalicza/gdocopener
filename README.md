# gdocopener
Python-based application to open Google Docs (gdoc, gsheet, gslides) files created on and by Dropbox. It will only work if you have an internet connection. 

Linux

Copy gdocopener.desktop to /usr/share/applications.
You will need superuser priviliges, so use 'sudo cp [SOURCE] [DEST]'.

run sudo chmod a+x gdcopener.desktop

Select gdcopener as default app for gdoc files. 
If you don't have python and unwilling to install it, download the compiled, executable file from /dist and change the executable in the desktop file to this file. It will work on its own, without the python interpreter.
The problem with this approach, that it also changes the default app for all text documents, as Linux works based on MIME types and not extensions.

According to this thread, Google do not plan to have a client on Linux any time soon:
https://support.google.com/drive/thread/2269747?hl=en

Windows

Google's Backup and sync solves the problem, so I highly recommend to install it.
If you do not want to install Backup and sync, you can still associate Google Docs files (gdoc, gdraw, etc) with the Dropbox app, which will open them in the browser. For some reason the latter solution does not work on Linux. Hence the need for gdocopen. :)
