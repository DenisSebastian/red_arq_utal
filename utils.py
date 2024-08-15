import geopandas as gpd

# Cargar el archivo GeoJSON
gdf = gpd.read_file("originales/comunas_nac.geojson")

# Simplificar la geometría
gdf['geometry'] = gdf['geometry'].simplify(tolerance=0.00015, preserve_topology=True)

# Guardar el archivo simplificado
gdf.to_file("data/INE/comuna_nac.geojson", driver='GeoJSON')
