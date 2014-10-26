# Overview

This is a plugin that renders diagrams from your selection in Sublime Text 2
or 3.

By default, it binds the (Command / Alt)-M key and registers a command on the
Command Palette.  Simple select the text for your diagram and trigger the
command.  Multiselections are allowed.  Each diagram will be generated in a
uniquely named file.

If a diagram handler recognizes a diagram in the selection, it will render it
and pop it up in a detected viewer.  All files are created in such a way that
they will be cleaned up unless Sublime Text dies a particularly horrible death.

If you wish to override the viewer used, create a user version of
Diagram.sublime-settings file in the usual way.


# Requirements

To install from scratch, it's necessary to have:

* Java (download from java.sun.com)
* Graphviz (I recommend "homebrew" on the Mac)
* Sublime Text 2 or 3

To install, just put a checkout of this project into your Packages directory in
Sublime Text.


# Support

Operating Systems:  MacOS X, Linux  
Diagram Types: PlantUML  
Viewers (in order of preference):

* Sublime Text3(**not 2**)
* MacOS X Preview
* MacOS X QuickLook
* Eye of Gnome

Patches to support additional viewers or diagrams are welcome.

# Install Instructions

1. Git clone this repository or download and uncompress zipped one.(in Packages directory for your platform)  
Sublime Text should detect the plugin and automatically load it.

  * On Linux, it's sometimes "~/.config/sublime-text-2/Packages/".
  * On MacOS X, it's r"~/Library/Application Support/Sublime Text( 2)?/Packages/".

2. Export PATH of subl(Sublime Text3)  
For example,  
```zsh
ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
```
**If you don't want to preview in Sublime Text or use *Sublime Text2*, select other viewer instead.**  
For example,  
```json
{
  "viewer" : "Preview" //Sublime, Preview, QuickLook or EyeOfGnome
}
```


The source is available via git at:

https://github.com/amaya-382/sublime_diagram_plugin.git

# Thanks

Special thanks to all of those who have contributed code and feedback,
including:

* Tobias Bielohlawek (Syntax Highlighting Support)
* Julian Godesa (UX feedback)
* Seán Labastille (Preview support, multi-diagram support)
* Kirk Strauser (Python 3 / SublimeText 3 Support)
* Stanislav Vitko (PlantUML updates)
