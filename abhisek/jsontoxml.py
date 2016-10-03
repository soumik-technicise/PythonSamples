import json     # For handling JSON data from given JSON file
import sys      # For handling command line arguments
import jinja2   # To create Controller for our template (template/jsontoxml_template.xml) to impart changes
import datetime # To estimate time duration
import time

def create_Dynamic_xml_dict(Object_dict, Output_XML_file, XML_template):
   
    print XML_template			     # Location of our XML template
    Location_list = XML_template.split("/")  # Location_list holds sub-directory and xml template as elements 
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(["./" + Location_list[0]])) #  # Create environmental variable in the sub-directory of xml teplete  
    Our_template = env.get_template(Location_list[1]) # Get our template with name as Location_list[1] using environment variable env at sub-directory as Location_list[0]  

    template_XML_dict = dict()
    for element in Object_dict: # Object_dict is a dictionary created from json data 
	if element == '__modelname__':
		model_name = Object_dict[element]   # model_name is a variable used in our template (jsontoxml_template.xml)
	else:
		template_XML_dict[element] = Object_dict[element] # template_XML_dict is a dictionary used in our template (jsontoxml_template.xml) 

    result = Our_template.render(template_XML_dict=template_XML_dict, model_name =model_name) # Update template (jsontoxml_template.xml)with present 
    # values of template_XML_dict and model_name w.r.t present json file

    # Timestamp information to show when the output xml file is modified 
    ts = time.time() 
    current_time = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y %H:%M:%S')
    print "Current Time:", current_time
    Modified_Output_XML_file = Output_XML_file + "_" + str(current_time)

    fp_out = open(Modified_Output_XML_file, 'w')  # Open Output XML file
    fp_out.write(result) # Output XML file is created with name given by user
    fp_out.close()
    

								# MAIN NAMESPACE
# Handling list of files using command line arguments
print 'Number of arguments:', len(sys.argv), 'arguments.'
argv_list = sys.argv
print 'Argument List:', argv_list
print"Our XML templete:",			# XML template with location
print argv_list[1]
print"Name of Input JSON file:",		# Please enter Input JSON file with .json extension
print argv_list[2]
print"Name of Output XML file:",		# Please enter Output XML file with .xml extension
print argv_list[3]
json1_file = open(str(argv_list[2]), "r")	# Open input json file
json1_str = json1_file.read()			# Read the content of json file as String
print"Given JSON object(s):"
print json1_str
json1_object = json.loads(json1_str)   # Given a JSON Object from String in form a dictionary 
create_Dynamic_xml_dict(json1_object, str(argv_list[3]), str(argv_list[1]))  # Calling controller function to impart changes over our default template and produce a XML file with name given by user.  
