import shutil
from pathlib import Path

carpeta_origen = Path(Path.home(), 'Documents', 'AI', 'bibliografia', 'Attention is All you Need.pdf' )
print(carpeta_origen)

archivo_destino = 'Libros_AI_comprimidos'
#shutil.make_archive(archivo_destino, zip, carpeta_origen)