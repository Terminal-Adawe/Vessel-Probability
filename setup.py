from cx_Freeze import setup, Executable

setup(name = "Vessel Probability" ,
      version = "1.0.0" ,
      description = "DESCRIPTION" ,
      executables = [Executable("PYTHON FILE", base = "Win32GUI")]
      )