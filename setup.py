from distutils.core import setup
import py2exe, sys, os

setup(
    windows=[{"script":"main.py"}],
    options={"py2exe":{"includes":["sip"]}},
    zipfile = None,
    )
