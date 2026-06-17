
import re
file_path = '/home/anton-samarin/Schreibtisch/documentation/Qodana/topics/qodana-yaml.md'
with open(file_path, 'r') as f:
    content = f.read()

# Let's see what's after 'linter: <linter>'
matches = re.findall(r'linter: <linter>.*', content)
print(f"Matches found: {len(matches)}")
for match in matches[:5]:
    print(f"Match: {repr(match)}")

# Let's try to match with a regex that is more permissive
# Maybe there are spaces or something?
# Let's search for just 'linter: <linter>'
