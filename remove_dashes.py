import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = re.split(r'(<script.*?>.*?</script>|<style.*?>.*?</style>)', html, flags=re.DOTALL | re.IGNORECASE)

for i in range(len(parts)):
    if i % 2 == 0:
        sub_parts = re.split(r'(<[^>]+>)', parts[i])
        for j in range(len(sub_parts)):
            if j % 2 == 0:
                # Replace em-dash, en-dash, and hyphen with a space
                sub_parts[j] = sub_parts[j].replace('—', ' ').replace('–', ' ').replace('-', ' ')
                # Optional: collapse multiple spaces if you want, but browsers do it anyway
        parts[i] = "".join(sub_parts)

new_html = "".join(parts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Dashes removed from text nodes.")
