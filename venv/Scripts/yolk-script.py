#!C:\Users\ASUS\PycharmProjects\GiraNapoliFlask\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'yolk==0.4.3','console_scripts','yolk'
__requires__ = 'yolk==0.4.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('yolk==0.4.3', 'console_scripts', 'yolk')()
    )
