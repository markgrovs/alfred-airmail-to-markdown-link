""" Airmail to Markdown Link


"""
#!/usr/bin/python
# encoding: utf8

import sys
# import os
from workflow import Workflow3
from Foundation import *
from ScriptingBridge import *

LOG = None

def main(wf):
    """

    """

    airmail = SBApplication.applicationWithBundleIdentifier_("it.bloop.airmail.beta11")

    # Format note text from message subject
    markdown_link = "[{title}]({url})".format(title=airmail.selectedMessage().subject(), \
                                                url=airmail.selectedMessageUrl())
    print markdown_link

if __name__ == u"__main__":
    wf = Workflow3()
    LOG = wf.logger
    sys.exit(wf.run(main))
