import arcpy
import os
# defining script input
fc_input_path = arcpy.GetParameterAsText(0)
output_type = arcpy.GetParameterAsText(1)
output_folder = arcpy.GetParameterAsText(2)
file_name = arcpy.GetParameterAsText(3)
arcpy.MakeFeatureLayer_management(fc_input_path,"FcLayer")
if output_type == "KMZ":
    output_kml_file = "{}.KMZ".format(file_name)
    full_output_kmz_path = os.path.join(output_folder,output_kml_file)
    arcpy.conversion.LayerToKML("FcLayer",full_output_kmz_path)
    print('exported')
elif output_type == "CAD":
    output_CAD_file = "{}.dwg".format(file_name)
    full_output_CAD_path = os.path.join(output_folder,output_CAD_file)
    # Process: Export to CAD
    arcpy.conversion.ExportCAD(fc_input_path, "DWG_R2018", full_output_CAD_path,"USE_FILENAMES_IN_TABLES","OVERWRITE_EXISTING_FILES")


