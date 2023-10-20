import arcpy
import os

gdp_path = arcpy.GetParameterAsText(0)

if not arcpy.Exists("gdp_path"):
    folder_path, gdp_name = os.path.split(gdp_path)
    arcpy.management.CreateFileGDB(folder_path, gdp_name)
    gdp_path = os.path.join(folder_path,gdp_name)
x_coord = arcpy.GetParameterAsText(1)
y_coord = arcpy.GetParameterAsText(2)
output_fc_name = arcpy.GetParameterAsText(3)
fc_path = os.path.join(gdp_path,output_fc_name)
point_obj = arcpy.Point(x_coord,y_coord)
spatial_ref = arcpy.SpatialReference("WGS 1984")
point_geom = arcpy.PointGeometry(point_obj,spatial_ref)
arcpy.CopyFeatures_management(point_geom,fc_path)

print("complete")


