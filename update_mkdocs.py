from pathlib import Path as pp
import shutil
import yaml
import os


DOCS = "docs"
NOTES = "notes"
YAML_FILE = "mkdocs.yml"
BASE_NAV = {'Home': 'index.md'}
BKP_FILE = "mkdocs.yml.bkp"

# creaiting a mkdocs.yml.bkp file
shutil.copy(YAML_FILE, BKP_FILE)
print("creaiting a mkdocs.yml.bkp ...")

try:
  # updating the mkdocs.yml file
  print("updating the mkdocs.yml ...")
  yaml_data: dict = yaml.safe_load(open(YAML_FILE, 'r'))
  yaml_data.get('nav').clear()
  yaml_data.get('nav').append(BASE_NAV)

  notes = {}

  for file in pp(DOCS, NOTES).glob('**/*'):
    if str(file).endswith('.md'):
      notes.update({file.name.split('.')[0].replace('_', '-')[1:]: str(file.relative_to(DOCS))})

  yaml_data.get('nav').append({'notes': notes})

  yaml_file = open(YAML_FILE, 'w')
  yaml.safe_dump(yaml_data, yaml_file)

  # cleanup
  os.remove(BKP_FILE)
except Exception:
  # something went wrong, your mkdocs.yml file is retained
  for file in os.listdir('.'):
    if file.endswith('.yml'):
      os.remove(file)
  os.rename(BKP_FILE, YAML_FILE)
  print("something went wrong, your mkdocs.yml file is retained")
    
