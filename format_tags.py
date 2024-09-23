import re

# Read the content of the markdown file
with open('3MF Volumetric Extension Template.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Define a regular expression pattern to match any XML tag starting with a backslash, excluding those enclosed in ** **
pattern = r'(?<!\*\*)\\<([\w]+)>(?!\*\*)'

# Replace the matched XML tags with the desired format
modified_content = re.sub(pattern, r'`<\1>`', content)

# Write the modified content back to the file
with open('3MF Volumetric Extension Template.md', 'w', encoding='utf-8') as file:
    file.write(modified_content)

print("XML tags starting with a backslash have been replaced successfully, excluding those enclosed in ** **.")