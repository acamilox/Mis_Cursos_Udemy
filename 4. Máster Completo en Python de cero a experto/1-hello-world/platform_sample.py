import platform

system = platform.system() # Nombre del sistema operativo
print(system)

version = platform.version() # Versión del sistema operativo
print(version)

print(platform.python_version())
print(platform.uname())
print(platform.machine())