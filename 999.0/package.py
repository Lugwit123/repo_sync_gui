# -*- coding: utf-8 -*-

name = "repo_sync_gui"
version = "999.0"
description = "GUI tool to upload/download each rez-package-source package repo"
authors = ["Lugwit Team"]

requires = [
    "python-3.12+<3.13",
    "pyside6",
]


def commands():
    env.PYTHONPATH.prepend("{root}/src")
    alias("repo_sync_gui", "python {root}/src/repo_sync_gui/main.py")


build_command = False
cachable = True
relocatable = True
