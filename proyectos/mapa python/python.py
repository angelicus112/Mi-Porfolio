#generar un mapa

import folium

def generar_mapa():
    latitud = -34.4575
    longitud = -58.7061

    mapa = folium.Map(location=[latitud, longitud], zoom_start=13)

    folium.Marker(

        location = [latitud, longitud],
        popup="Benavidez",
        toolyip="Click para mas info",

    ).add_to(mapa)

    mapa.save("mapa.html")

generar_mapa()