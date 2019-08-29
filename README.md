# Auto-Paste-Text
The program is written in Python 3, It create document and paste the copied text.

This program allow to continuiously  copy text without shifting back and forth from  source to document.

## Usage
Requirements: 

> [Pyhon 3](https://www.python.org/downloads/)

> [PyQt5](https://pypi.org/project/PyQt5)


You can run the program by:(GNU/Linux)

Make it executable

> ```$chmod +x Autopaste.pyw```

then:

> ```$nohup /path/Autopaste.pyw > output.log &```

Use the run.py

Open the run.py in text edtitor and edit the path:

> ```path = '/path/Autopaste.pyw```

then save

> ```$python3 run.py```

Shortcut keys:
 
 'Ctrl + alt + u'. Open the UI.
 
 'shift + s'. Paste the text. 
 
I use nohup for running my program in background
you can check the tutorial: [here](https://janakiev.com/blog/python-background/)
