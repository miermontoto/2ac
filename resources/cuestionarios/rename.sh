# Renombar todos los archivos para que tengan el formato:
# Sesión x-y. <nombre_sesión>.png
cd /home/JuanMier/uo/y2t1/Arquitectura/resources/cuestionarios/
for i in "./"*; do 
    j=$(echo $i | tr -s ' ' | cut -d ' ' -f 5-);
    if [ "Screenshot" = $(echo $i | tr -s ' ' | cut -d ' ' -f1 | cut -d/ -f9) ]; then
        j=$(echo $j | cut -d ' ' -f1-);
        j=${j::-25};
        mv "$(echo $i | cut -d/ -f9)" "$j.png";
    fi
done