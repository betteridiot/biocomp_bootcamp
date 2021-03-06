import os
import shutil
import html


try:
    shutil.move(os.path.join(os.getcwd(), 'utils', 'init.py'),
                os.path.join(os.getcwd(), '.ipython', 'profile_default', 'startup', 'init.py'))
    print(html.unescape("Kernel environment variables reset.\nPlease press the '&#8635;' button above or '0' twice on your keyboard"))
except FileNotFoundError:
    if os.path.isfile(os.path.join(os.getcwd(), '.ipython', 'profile_default', 'startup', 'init.py')):
        if os.getenv('CULL_TIMEOUT') == '28800':
            print('Kernel environmental variables already set.\nPlease continue.')
        else:
            print(html.unescape("Kernel environment variables already reset.\nPlease press '&#8635;' above or '0' twice on your keyboard"))

