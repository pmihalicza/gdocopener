# gdocopener
A lightweight Python-based application for Linux to open Google Docs (gdoc, gsheet, gslides) files created on and by Dropbox from a file manager. It will only work if you have an internet connection. 

Dropbox introduced the possibility to create Google Docs files from within Dropbox. These files can be edited by the Google Docs editor, but save back to Dropbox. If you use the Dropbox website to navigate among your files, you are good to go. However, if you are on Linux and want to open these Docs files from a file manager (e.g. Nautilus, Double Commander), you cannot (on Windows, if you associate these files with the Dropbox app, it will do the job).
**gdocopener** will solve this problem. If you follow the steps below, you will be able to open these files from your file manager with one click.

## Follow these steps to make it work for you
1. Copy gdocopener.py to any folder you prefer.
2. Copy gdocopener.desktop to /usr/share/applications.
You will need superuser priviliges, so use 'sudo cp [SOURCE] [DEST]'.
3. Run 'sudo chmod a+x gdocopener.desktop' to make it executable.
4. Modify gdocopener.desktop to have your path to gdocopener.py
4. Select gdocopener as the default app for gdoc/gsheet/gslides files, following instructions in this post: .
https://help.ubuntu.com/stable/ubuntu-help/files-open.html
Please note, that this also changes the default app for all text documents. gdocopener handles this, and if you open a "normal" text file - i.e. not Google Docs - it will be passed to a text editor (currently hardcoded to 'gedit').

If you don't have python and unwilling to install it, download the compiled, executable file from /dist in this repo and change the executable in the gdocopener.desktop file to this:
Exec=[your_path_to_the_gdocopener_executable file]/gdocopener %f
