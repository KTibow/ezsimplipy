print("Going to install...")
from distutils.core import setup
print("Imported setup tool...")
setup(name="ezsimplipy",
      version='1.0',
      packages=['ezsimplipy'],
      author="Kendell R.",
      author_email="ejrejr@hotmail.com",
      license="MIT",
      description="A wrapper for the simplipy library.",
      download_url="https://github.com/KTibow/ezsimplipy",
      url="https://github.com/KTibow/ezsimplipy")
print("Package installed!")
