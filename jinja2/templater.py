import jinja2
import importlib.util
import pathlib


#KEEP THE STRINGS RAW (sushi grade, if you'd prefer) Just paste your desired path straight from the file manager below vv
TEMPLATE_DIRECTORY = r"C:\Users\theno\Documents\Uni Work\GitHub\nedinyourhead.github.io\jinja2\template_files"
INPUT_DIRECTORY = r"C:\Users\theno\Documents\Uni Work\GitHub\nedinyourhead.github.io\jinja2\input_files"
OUTPUT_DIRECTORY = r"C:\Users\theno\Documents\Uni Work\GitHub\nedinyourhead.github.io"

#Template file names
PROJECT_TEMPLATE_FILE = "project_template.jinja"


#Format directories as readable paths
python_template_directory = TEMPLATE_DIRECTORY.replace("\\", r"/")
uri_input_directory = 'file:' + INPUT_DIRECTORY.replace("\\", r"/")
uri_output_directory = 'file:' + OUTPUT_DIRECTORY.replace("\\", r"/")


#Use Jinja's built-in template loading system to load the template
templateLoader = jinja2.FileSystemLoader(searchpath=python_template_directory)
templateEnv = jinja2.Environment(loader=templateLoader, autoescape = False)
template = templateEnv.get_template(PROJECT_TEMPLATE_FILE)


#Render project site templates using project_data inputs
for source_file in pathlib.Path.from_uri(uri_input_directory).glob('*.py'):
    name = source_file.stem
    spec = importlib.util.spec_from_file_location(name, source_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    output_text = template.render(mod.project_data.data)  # this is where to put args to the template renderer
    

    print("Generated", mod.project_data)

    p = pathlib.Path.from_uri(uri_output_directory)
    folder = p / source_file.stem.replace("_", "-") / "index.html"
    with folder.open("w") as f:
        f.write(output_text)
