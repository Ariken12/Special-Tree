import cx_Freeze

cx_Freeze.setup(
    name = "NewYearTree",
    version = "0.1",
    description = "That programm count coords and lenght for NewYearTree",
    executables = [cx_Freeze.Executable("main.py")]
)
