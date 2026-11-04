import re
import sys

def change_namespace_prefix_md(md_file, elements, new_prefix):
    # Read the Markdown file
    with open(md_file, 'r') as f:
        content = f.read()

    # Find XML snippets
    snippets = re.findall(r'```xml(.*?)```', content, re.DOTALL)

    for snippet in snippets:
        original_snippet = snippet
        print (f"Snippet: {snippet}")
        # Replace the namespace prefix in the XML snippet
        for element in elements:
            snippet = re.sub(rf'<{element} ', f'<{new_prefix}:{element} ', snippet, flags=re.IGNORECASE)
            snippet = re.sub(rf'</{element}>', f'</{new_prefix}:{element}>', snippet, flags=re.IGNORECASE)
            snippet = re.sub(rf'<{element}>', f'<{new_prefix}:{element}>', snippet, flags=re.IGNORECASE)
            snippet = re.sub(rf'</{element} ', f'</{new_prefix}:{element} ', snippet, flags=re.IGNORECASE)



        print (f"New snippet: {snippet}")
        print("-" * 80)
        # Replace the original XML snippet with the modified one
        content = content.replace(original_snippet, f'\n{snippet}\n')

    # Write the modified Markdown back to the file
    with open(md_file, 'w') as f:
        f.write(content)

    f.close()

def change_namespace_prefix_md_from_file(md_file, elements_file, new_prefix):
    # Read the elements file
    with open(elements_file, 'r') as f:
        elements = [line.strip() for line in f]
    
    change_namespace_prefix_md(md_file, elements, new_prefix)

def apply_implicit_prefix(md_file):
    prefix = "i"
    elements = [
        "implicitfunction",
        "scalar",
        "vector",
        "matrix",
        "resourceid",
        "in",
        "out",
        "scalarref",
        "vectorref",
        "matrixref",
        "resourceref",
        "addition",
        "subtraction",
        "multiplication",
        "division",
        "constant",
        "constvec",
        "constmat",
        "composevector",
        "vectorfromscalar",
        "decomposevector",
        "composematrix",
        "matrixfromcolumns",
        "matrixfromrows",
        "dot",
        "cross",
        "matvecmultiplication",
        "transpose",
        "inverse",
        "sin",
        "cos",
        "tan",
        "arcsin",
        "arccos",
        "arctan",
        "arctan2",
        "min",
        "max",
        "abs",
        "fmod",
        "pow",
        "sqrt",
        "exp",
        "log",
        "log2",
        "log10",
        "select",
        "clamp",
        "cosh",
        "sinh",
        "tanh",
        "round",
        "ceil",
        "floor",
        "sign",
        "fract",
        "functioncall",
        "unsignedmesh",
        "length",
        "constresourceid",
        "mod"
    ]

    change_namespace_prefix_md(md_file, elements, prefix)

def apply_volumetric_prefix(md_file):
    prefix = "v"
    elements = [
        "image3d",
        "imagestack",
        "imagesheet",
        "functionfromimage3d",
        "volumedata",
        "composite",
        "materialmapping",
        "color",
        "property",
        "levelset"
    ]

    change_namespace_prefix_md(md_file, elements, prefix)

def apply_prefixes(md_file):
    apply_implicit_prefix(md_file)
    #apply_volumetric_prefix(md_file)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python apply_prefixes.py md_file")
        # print number of arguments
        print(len(sys.argv))
        sys.exit(1)

    md_file = sys.argv[1]
    
    apply_prefixes(md_file)