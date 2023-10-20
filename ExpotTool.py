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
elif output_type == "EXCEL":
    output_EXCEL_file = "{}.xlsx".format(file_name)
    full_output_EXCEl_path = os.path.join(output_folder,output_EXCEL_file)
    arcpy.TableToExcel_conversion("Fclayer",full_output_EXCEl_path)
elif output_type == "SHP":
    output_SHP_file = "{}".format(file_name)
    full_output_SHP_path = os.path.join(output_folder,output_SHP_file)
    if not os.path.exists(full_output_SHP_path):
        os.makedirs(full_output_SHP_path)
    fc_gdp_path, fc_name = os.path.split(fc_input_path)
    arcpy.env.workspace = fc_gdp_path
    arcpy.conversion.FeatureClassToShapefile(fc_name,full_output_SHP_path)
elif output_type == "CAD":
    output_CAD_file = "{}.dwg".format(file_name)
    full_output_CAD_path = os.path.join(output_folder,output_CAD_file)
    # Process: Export to CAD
    arcpy.conversion.ExportCAD(fc_input_path, "DWG_R2018", full_output_CAD_path,"USE_FILENAMES_IN_TABLES","OVERWRITE_EXISTING_FILES")


