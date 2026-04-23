import os
import re

DARK_INJECT = '\n    <!-- Dark Mode CSS -->\n    <link href="/static/web/css/darkmode.css" rel="stylesheet">\n    <!-- Dark Mode JS - loaded early to prevent flash -->\n    <script src="/static/web/js/darkmode.js"></script>'

base = os.path.join('app', 'templates', 'web')
files = [os.path.join(base, f) for f in os.listdir(base) if f.endswith('.html')]

changed = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip files that already have darkmode OR files that use navbar include (they get it from navbar)
    if 'darkmode.css' in content:
        print(f'Skipped (already has darkmode): {fp}')
        continue

    # Inject after style.css link
    new_content = re.sub(
        r'(<link href="/static/web/css/style\.css" rel="stylesheet">)',
        r'\1' + DARK_INJECT,
        content,
        count=1
    )

    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {fp}')
        changed += 1
    else:
        print(f'No change: {fp}')

print(f'\nDone. Changed: {changed}')
