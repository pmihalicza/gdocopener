# gdocopen
Python-based application to open Google Docs (gdoc) files created on and by Dropbox. It will only work if you have an internet connection. 

Linux

Copy gdocopen.desktop to /usr/share/applications.
You will need superuser priviliges, so use 'sudo cp [SOURCE] [DEST]'.

run sudo chmod a+x gdcopen.desktop

select gdcopen as default app for gdoc files

According to this thread, Google do not plan to have a client on Linux any time soon:
https://support.google.com/drive/thread/2269747?hl=en

Windows

Google's Backup and sync solves the problem, so I highly recommend to install it.
If you do not want to install Backup and sync, you can still associate Google Docs files (gdoc, gdraw, etc) with the Dropbox app, which will open them in the browser. For some reason the latter solution does not work on Linux. Hence the need for gdocopen. :)
