#!/usr/bin/env python
"""
 Created by howie.hu at 2019-10-21.
"""

import plistlib
import os

import fire

PLIST_PATH_TEM = "/Applications/{0}.app/Contents/Info.plist"


def change_app_plist(app_name: str, status: bool = True):
    """
    Used for hiding/displaying the application's icon
    eg: leaf WeChat --status=1
    :param app_name:
    :param status:
    :return:
    """
    info_plist = PLIST_PATH_TEM.format(app_name)
    if os.path.exists(info_plist):

        with open(info_plist, "rb") as fp:
            pl = plistlib.load(fp)
            if status:
                pl["LSUIElement"] = "1"
            else:
                pl.pop("LSUIElement", '')

        with open(info_plist, "wb") as fp:
            plistlib.dump(pl, fp)
            print(f"{app_name} icon is {'hidden' if status else 'shows'} successfully, Please restart it.")
    else:
        output = f"Please make sure the app_name is correct, {app_name} is not in /Applications."
        print("\033[1;31;40m" + output + "\033[0m")


def execute():
    fire.Fire(change_app_plist)
