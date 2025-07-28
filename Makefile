
MDFILES =  intro.md pois/pueblo-del-chirimoyo.md\
    pois/terrazas-playa-granada.md pois/villa-astrida.md\
    pois/viviendas-varias.md pois/Oleaje.md\
    pois/iglesia-josefina-bakhita.md\
    pois/vertice-geodesico.md\
    pois/el-piruli.md\
    pois/arquitectura-tradicional.md\
    pois/tras-la-pandemia.md
ALLFILES = $(MDFILES)  $(wildcard *.txt) $(wildcard *.css)

doc: tour-playa-granada.docx

tour-playa-granada.docx: $(ALLFILES)
	pandoc  -o tour-playa-granada.docx \
        --metadata title="Playa Granada, arquitectura e historia" --metadata creator="JJ Merelo" --metadata rights="CC-BY-SA 3.0" \
        playa-granada.txt  $(MDFILES)

