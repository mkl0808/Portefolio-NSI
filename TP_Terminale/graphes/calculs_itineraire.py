from math import *
import osmnx as ox
import networkx as nx
import folium
from IPython.display import IFrame
from geopy.geocoders import Nominatim
ox.config(log_console=True, log_file=True, use_cache=True)
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

#fonction déterminant les coordonnées GPS à partir d'une adresse postale
def coord_GPS_addresse(adresse, ville):
    geo = Nominatim()
    coord = geo.geocode(adresse + ' ' + ville, timeout = 10)
    coord_GPS=(coord.latitude,coord.longitude)
    return(coord_GPS)

#fonction calcul de la distance entre deux points GPS en mètres
def distance_2pGPS(coord1,coord2):
    la1=radians(coord1[0])
    la2=radians(coord2[0])
    lon1=radians(coord1[1])
    lon2=radians(coord2[1])
    dis=6371009*acos((sin(la1)*sin(la2)+cos(la1)*cos(la2)*cos(lon1-lon2)))
    return dis

#fonction de calculs d'orientation d'une droite passant par 2 points GPS par rapport à la direction Nord
def orientation(coord1,coord2):
    la1=radians(coord1[0])
    la2=radians(coord2[0])
    lon1=radians(coord1[1])
    lon2=radians(coord2[1])
    longDelta = lon2-lon1
    y= sin(longDelta)*cos(la1)
    x=cos(la1)*sin(la2)-sin(la1)*cos(la2)*cos(longDelta)
    angle = atan2(y,x)*360/(2*pi)
    while angle < 0:
        angle += 360
    direction=360-(float(angle) % 360)
    return direction

# fonction calcul du temps de parcours du chemin le plus court en tenant compte des vitesses maximums renseignées sur openstreetmap
def calcul_temps_parcours(G,route):
    t=0
    distance=0
    d=0
    edges_proj = ox.graph_to_gdfs(G, nodes=False, edges=True)
    for i in range (0 ,len(route)-1):
        d=distance_2pGPS((G.node[route[i]]['y'],G.node[route[i]]['x']),(G.node[route[i+1]]['y'],G.node[route[i+1]]['x']))
        for j in range(0,len(edges_proj.osmid)):
            if (edges_proj.u[j]==route[i]) and (edges_proj.v[j]==route[i+1]):
                v= float(edges_proj.maxspeed[j])
                if isnan(v) :
                    road=edges_proj.highway[j]
                    if road=='unclassified' or road[0]=='unclassified' :
                        v=30
                        break;
                    if road== 'residential'  or road[1]=='residential':
                        v=30
                        break;
                    if road== 'tertiary'  or road[1]=='tertiary':
                        v=80
                        break;
        t+= (d*3.6)/v
        distance = distance + d
    return(t)


# génération d'une carte interactive itineraire.html avec tous les détails
def graphique_html(G,route):
    graph_map = ox.plot_graph_folium(G, popup_attribute='name',  edge_width=2)
    route_graph_map= ox.plot_route_folium(G, route, route_map=graph_map, popup_attribute='length')
    folium.Marker(location=(G.node[route[0]]['y'],G.node[route[0]]['x']), icon=folium.Icon(color='red')).add_to(route_graph_map)
    folium.Marker(location=(G.node[route[len(route)-1]]['y'],G.node[route[len(route)-1]]['x']), icon=folium.Icon(color='blue')).add_to(route_graph_map)
    filepath = 'itinéraire.html'
    route_graph_map.save(filepath)
    IFrame(filepath, width=600, height=500)

#génération du graphe de la zone géographique incluant l'itinéraire en fonction du type de moyen de locomotion
def graphe(adresse_depart,Ville_D,adresse_arrivee,Ville_A,type_graph):
    origine_GPS=coord_GPS_addresse(adresse_depart,Ville_D)
    destination_GPS=coord_GPS_addresse(adresse_arrivee,Ville_A)
    point = ((origine_GPS[0]+destination_GPS[0])/2,(origine_GPS[1]+destination_GPS[1])/2)
    dist=distance_2pGPS(origine_GPS,destination_GPS)/1.5
    G = ox.graph_from_point(point, distance=dist, network_type=type_graph)
    origine=ox.get_nearest_node(G, origine_GPS)
    destination=ox.get_nearest_node(G, destination_GPS)
    route = nx.shortest_path(G, origine, destination)
    ox.plot_graph_route(G,route,fig_height=10, fig_width=10, show=True, use_geom=True, close=False, route_color='green' ,orig_dest_node_size=100)
    return G, route


# Algorithme de calcul de distance à rechercher par les élèves en TP
def distance_totale(G, route):
    distance = 0
    for sommet in range(len(route) - 1):
        sommet_suivant = sommet + 1
        lat1 = G.node[route[sommet]]['y']
        lon1 = G.node[route[sommet]]['x']
        lat2 = G.node[route[sommet_suivant]]['y']
        lon2 = G.node[route[sommet_suivant]]['x']
        d = distance_2pGPS((lat1, lon1), (lat2, lon2))
        distance += d
    return distance

def distance_totale_adj(G, route):
    distance = 0
    for i in range(len(route) - 1):
        sommet_actuel = route[i]
        sommet_suivant = route[i + 1]
        arrete = list(G.adj[sommet_actuel][sommet_suivant].values())[0]
        longueur_arrete = arrete["length"]
        distance += longueur_arrete
    return distance

def temps_parcours(distance_m, vitesse_kmh):
    vitesse_ms = vitesse_kmh * 1000 / 3600
    temps_s = distance_m / vitesse_ms
    minutes = int(temps_s // 60)
    secondes = int(temps_s % 60)
    return minutes, secondes

# Programme principal
if __name__ == "__main__":
    #coord_domicile = coord_GPS_addresse("14 rue de la biche", "Chelles")
    #print("Coordonnées GPS du domicile :", coord_domicile)
    #coord_lycee = coord_GPS_addresse("32 avenue de l'Europe", "Chelles")
    #print("Coordonnées GPS du lycée :", coord_lycee)

    #G = graphe("14 rue de la biche", "Chelles", "32 avenue de l'Europe", "Chelles", "all")

    #G_drive_service, route_drive_service = graphe("14 rue de la biche", "Chelles", "32 avenue de l'Europe", "Chelles", "drive_service")
    #print("Contenu de la variable route_drive_service pour le trajet en transports :", route_drive_service)

    #distance_gps = distance_totale(G_drive_service, route_drive_service)
    #print("Distance totale (méthode GPS) :", distance_gps, "mètres")

    #distance_adj = distance_totale_adj(G_drive_service, route_drive_service)
    #print("Distance totale (via G.adj) :", distance_adj, "mètres")

    #G_walk, route_walk = graphe("14 rue de la biche", "Chelles", "32 avenue de l'Europe", "Chelles", "walk")
    #print("Contenu de la variable route_walk pour le trajet à pied :", route_walk)

    G_drive, route_drive = graphe("14 rue de la biche", "Chelles", "32 avenue de l'Europe", "Chelles", "drive")
    distance = distance_totale_adj(G_drive, route_drive)
    print("Distance totale (via G.adj) :", distance, "mètres")
    min_voiture, sec_voiture = temps_parcours(distance, 50)

    min_velo, sec_velo = temps_parcours(distance, 20)

    print("Voiture :", min_voiture, "minutes et", sec_voiture, "secondes")
    print("Vélo :", min_velo, "minutes et", sec_velo, "secondes")

    #graphique_html(G_drive, route_drive)

    #coord_domicile = coord_GPS_addresse("14 rue de la biche", "Chelles")
    #coord_lycee = coord_GPS_addresse("32 avenue de l'Europe", "Chelles")
    #orientation = orientation(coord_domicile, coord_lycee)
    #print("Orientation par rapport au Nord :", orientation, "degrés")




