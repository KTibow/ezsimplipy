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
		globals()[libname] = importlib.import_module(libname)
		return (0, -1, -1)
	except ModuleNotFoundError as e:
		try:
			pipit("install "+libname)
			globals()[libname] = importlib.import_module(libname)
			return (0, e, -1)
		except Exception as f:
			return (-1, e, f)
makeSure("asyncio")
makeSure("aiohttp")
ClientSession = aiohttp.ClientSession
