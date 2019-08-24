from pip._internal import main as pipmain
pipit = lambda theargs: pipmain(theargs.split(" "))
class VersionError(Exception):
  pass
def makeSure(libname):
  try:
    import importlib
  except ImportError:
    raise VersionError("Please upgrade your Python interpreter.")
  try:
    importlib.import_module(libname)
  except ModuleNotFoundError:
    pipit("install "+libname)
    importlib.import_module(libname)
