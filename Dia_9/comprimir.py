import zipfile

mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

mi_zip.write('Attention is All you Need.pdf')
mi_zip.write('Clinical Versus Statistical Prediction A Theoretical Analysis and a Review of the Evidence.pdf')

mi_zip.close()