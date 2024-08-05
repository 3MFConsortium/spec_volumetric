import os


if __name__ == '__main__':
    # Get the current working directory
    cwd = os.getcwd()
    
    
    # check if the template file exists
    if not os.path.exists(f'{cwd}/3MF Volumetric Extension Template.md'):
        exit(1)

    # check if the implicit.xsd and the volumetric.xsd files exist
    if not os.path.exists(f'{cwd}/implicit.xsd') or not os.path.exists(f'{cwd}/volumetric.xsd'):
        exit(1)
    
    template = None
    with open(f'{cwd}/3MF Volumetric Extension Template.md', 'r') as file:
        template = file.read()
    
    implicit = None
    with open(f'{cwd}/implicit.xsd', 'r') as file:
        implicit = file.read()
    
    volumetric = None
    with open(f'{cwd}/volumetric.xsd', 'r') as file:
        volumetric = file.read()
    
    # Volumetric placeholder is VOLUMETRIC_SCHEMA_INSERT
    template = template.replace('VOLUMETRIC_SCHEMA_INSERT', "```xml\n" + volumetric + "```")

    # Implicit placeholder is IMPLICIT_SCHEMA_INSERT
    template = template.replace('IMPLICIT_SCHEMA_INSERT', "```xml\n" + implicit + "```")

    with open(f'{cwd}/3MF Volumetric Extension.md', 'w') as file:
        file.write(template)
    