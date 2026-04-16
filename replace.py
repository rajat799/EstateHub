import os

files = [
    r'c:\Users\asus\OneDrive\Desktop\property_management\app\templates\web\index.html',
    r'c:\Users\asus\OneDrive\Desktop\property_management\app\templates\web\latest_properties.html',
    r'c:\Users\asus\OneDrive\Desktop\property_management\app\templates\web\property_types.html',
    r'c:\Users\asus\OneDrive\Desktop\property_management\app\templates\web\propertylist.html'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert what I did earlier for Properties
    bad_str1 = '''<a class=\"d-block h5 mb-2\">' + response[i].pr_name + '</a> <p class=\"text-primary mb-2\" style=\"font-size: 14px; font-weight: 600;\"><i class=\"fas fa-store me-2\"></i>Sold by: ' + response[i].pr_seller_name + '</p>'''
    good_str1 = '''<a class=\"d-block h5 mb-2\">' + response[i].pr_seller_name + '</a> <p class=\"text-primary mb-2\" style=\"font-size: 14px; font-weight: 600;\"><i class=\"fas fa-store me-2\"></i>Sold by: ' + response[i].pr_created_by + '</p>'''
    
    content = content.replace(bad_str1, good_str1)

    bad_str2 = '''<a class=\"d-block h5 mb-2\">'+response[i].pr_name+'</a> <p class=\"text-primary mb-2\" style=\"font-size: 14px; font-weight: 600;\"><i class=\"fas fa-store me-2\"></i>Sold by: '+response[i].pr_seller_name+'</p>'''
    good_str2 = '''<a class=\"d-block h5 mb-2\">'+response[i].pr_seller_name+'</a> <p class=\"text-primary mb-2\" style=\"font-size: 14px; font-weight: 600;\"><i class=\"fas fa-store me-2\"></i>Sold by: '+response[i].pr_created_by+'</p>'''
    
    content = content.replace(bad_str2, good_str2)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

with open(r'c:\Users\asus\OneDrive\Desktop\property_management\app\templates\web\single_property.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('$("#name").text(response[0].pr_name);', '$("#name").text(response[0].pr_seller_name);')
content = content.replace('$("#name1").text(response[0].pr_name);', '$("#name1").text(response[0].pr_seller_name);')
content = content.replace('$("#seller_info").text(response[0].pr_seller_name);', '$("#seller_info").text(response[0].pr_created_by);')

with open(r'c:\Users\asus\OneDrive\Desktop\property_management\app\templates\web\single_property.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
