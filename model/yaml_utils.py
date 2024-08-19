import yaml
from pydantic import BaseModel
import sys

class ComparisonYaml(BaseModel):
    '''Class that defines the ymal format expected.'''
    image_a: str
    image_b: str
    threshold: float
    output_location: str


def load_yaml(input_path: str) -> dict:
    '''Loads an yaml file and returns a dict with the file content.'''
    ## Try to open YAML file
    try:
        with open(input_path, 'r') as yaml_file:
            yaml_dict = yaml.safe_load(yaml_file)
    except Exception as e:
        print("An Error occured during YAML file load:", e)
        sys.exit(0)
        
    return yaml_dict


def check_yaml_format(yaml_dict: dict, desired_format: ComparisonYaml=ComparisonYaml) -> ComparisonYaml:
    '''
        Checks if the 'yaml_dict' is in the 'desired_format' as defined by a pydantic BaseModel class.
        And returns an object in the 'desired_format', 'ComparisonYaml' by default.
    '''
    ## Try to parse YAML dict to desired_format
    try:
        comp_obj = desired_format(**yaml_dict)
    except Exception as e:
        print("Unexpected YAML format:", e)
        sys.exit(0)

    return comp_obj


def read_yaml(yaml_path):
    yaml_dict = load_yaml(yaml_path)
    comp_param = check_yaml_format(yaml_dict)

    return comp_param