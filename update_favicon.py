import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The old favicon link starts with <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'
# We can use a regex to match the whole line.
pattern = re.compile(r"^\s*<link rel=\"icon\" type=\"image/svg\+xml\" href=\"data:image/svg\+xml.*?\">\s*", re.MULTILINE)

new_favicon_html = """  <link rel="icon" type="image/png" href="/favicon-96x96.png" sizes="96x96" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="shortcut icon" href="/favicon.ico" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="manifest" href="/site.webmanifest" />\n"""

# Perform replacement
new_content, count = pattern.subn(new_favicon_html, content)

if count > 0:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Replaced favicon markup. {count} occurrence(s) updated.")
else:
    print("Could not find the old favicon markup to replace.")
