import os
import re

DARK_CSS_INJECT = '\n   <!-- Dark Mode CSS -->\n   <link href="/static/web/css/darkmode.css" rel="stylesheet">\n   <!-- Dark Mode JS - loaded early to prevent flash -->\n   <script src="/static/web/js/darkmode.js"></script>'

DARK_STYLE_EXTRA = """
       /* Admin/Seller dark mode extras */
       html.dark-mode #main-wrapper,
       html.dark-mode .page-wrapper {
           background-color: #0f172a !important;
       }
       html.dark-mode .left-sidebar,
       html.dark-mode .scroll-sidebar {
           background-color: #1e293b !important;
       }
       html.dark-mode .sidebar-nav ul,
       html.dark-mode .sidebar-nav li a,
       html.dark-mode .sidebar-link {
           background-color: #1e293b !important;
           color: #94a3b8 !important;
       }
       html.dark-mode .sidebar-link:hover,
       html.dark-mode .sidebar-link.active {
           background-color: #263548 !important;
           color: #00B98E !important;
       }
       html.dark-mode .sidebar-link .hide-menu { color: inherit !important; }
       html.dark-mode .topbar { background-color: #1e293b !important; }
       html.dark-mode .page-breadcrumb.bg-white {
           background-color: #1e293b !important;
           border-bottom: 1px solid #334155 !important;
       }
       html.dark-mode .white-box {
           background-color: #1e293b !important;
           box-shadow: 0 4px 20px rgba(0,0,0,0.35) !important;
       }
       html.dark-mode footer.footer {
           background-color: #1e293b !important;
           color: #94a3b8 !important;
           border-top: 1px solid #334155 !important;
       }
       html.dark-mode .preloader { background-color: #0f172a !important; }"""

base = os.path.join('app', 'templates')
files = []
for folder in ['admin', 'seller']:
    fpath = os.path.join(base, folder)
    for f in os.listdir(fpath):
        if f.endswith('.html'):
            files.append(os.path.join(fpath, f))

changed = 0
skipped = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'darkmode.css' in content:
        print(f'Skipped (already updated): {fp}')
        skipped += 1
        continue

    # Insert dark CSS/JS after the admin or seller CSS link
    new_content = re.sub(
        r'(<link href="/static/(?:admin|seller)/css/style\.min\.css" rel="stylesheet">)',
        r'\1' + DARK_CSS_INJECT,
        content
    )

    # Insert dark style rules inside style block after logo-text closing brace
    new_content = re.sub(
        r'(\.logo-text \{[^}]+\})',
        r'\1' + DARK_STYLE_EXTRA,
        new_content,
        count=1
    )

    if new_content != content:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {fp}')
        changed += 1
    else:
        print(f'No change: {fp}')

print(f'\nDone. Changed: {changed}, Skipped (already done): {skipped}')
