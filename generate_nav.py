import os

NAV_TEMPLATE = '''<nav aria-label="Main navigation" role="navigation">
    <ul>
{links}
    </ul>
</nav>'''

LINK_TEMPLATE = '        <li><a href="{href}"{current}>{name}</a></li>'

# Exclude these files from navigation
default_excludes = {'404.html', 'error.html'}

# Preferred order for known pages; remaining files will follow alphabetically
PREFERRED_ORDER = [
    'index.html',
    'web-accessibility-tools.html',
    'about.html',
]

def get_html_files(exclude=None):
    if exclude is None:
        exclude = set()
    return [f for f in os.listdir('.') if f.endswith('.html') and f not in exclude]

def make_nav(current_page=None):
    html_files = get_html_files(default_excludes)
    # Sort files by preferred order first, then by name
    order_index = {name: i for i, name in enumerate(PREFERRED_ORDER)}
    html_files.sort(key=lambda name: (order_index.get(name, 9999), name))

    links = []
    for f in html_files:
        name = f.replace('.html', '').replace('-', ' ').title()
        current = ' aria-current="page"' if f == current_page else ''
        links.append(LINK_TEMPLATE.format(href=f, current=current, name=name))
    return NAV_TEMPLATE.format(links='\n'.join(links))

if __name__ == '__main__':
    import re
    html_files = get_html_files(default_excludes)
    for page in html_files:
        nav_html = make_nav(current_page=page)
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(r'<nav[\s\S]*?</nav>', nav_html, content, count=1)
        with open(page, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Navigation updated in {page}')
