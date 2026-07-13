.PHONY: install serve build publish clean

install:   ## Instala las dependencias
	pip install -r requirements.txt

serve:     ## Vista previa local (http://localhost:8000)
	pelican --autoreload --listen content -s pelicanconf.py -o output

build:     ## Construye el sitio (desarrollo)
	pelican content -s pelicanconf.py -o output

publish:   ## Construye para producción
	pelican content -s publishconf.py -o output

clean:     ## Limpia artefactos
	rm -rf output __pycache__
