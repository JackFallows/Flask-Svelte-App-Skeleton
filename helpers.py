import pathlib
import functools
from os import listdir
from os.path import isfile, join

from flask import render_template

bundle_files_path = 'client/public/build'

def get_bundle_files():
    # https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    return [f for f in listdir(bundle_files_path) if isfile(join(bundle_files_path, f))]

def get_css():
    bundle_files = get_bundle_files()
    css_file = list(filter(lambda f: pathlib.Path(f).suffix == '.css', bundle_files))[0]
    return join('build', css_file)

def get_js():
    bundle_files = get_bundle_files()
    
    def map_file(file: str):
        last_index = file.rindex("-")
        file_dict = {
            file[0:last_index]: "/" + join('build', file)
        }
        return file_dict
    
    def reduce_files(file_a, file_b):
        file_dict = {
            **file_a,
            **file_b
        }
        return file_dict
    
    module_bundles = dict(
        functools.reduce(
            reduce_files,
            map(
                map_file, 
                filter(lambda f: pathlib.Path(f).suffix == '.js', bundle_files)
            )
        )
    )
    
    return module_bundles

def custom_render_template(template_name, **context):
    return render_template(
        template_name_or_list=template_name,
        module_js=get_js(),
        module_css=get_css(),
        **context
    )
