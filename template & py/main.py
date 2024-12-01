import os

def generate_html(output_file, Titre, image_background, h1, PEGI, DUREE, RESUME, GENRE1, GENRE2, GENRE3, GENRE4, URL):
    with open('template-film.html', 'r', encoding='utf-8') as template_file:
        template = template_file.read()
    
    html_content = template.replace('{{Titre}}', Titre)\
                           .replace('{{image-background}}', image_background)\
                           .replace('{{h1}}', h1)\
                           .replace('{{PEGI}}', PEGI)\
                           .replace('{{DURÉE}}', DUREE)\
                           .replace('{{RÉSUMÉ}}', RESUME)\
                           .replace('{{GENRE1}}', GENRE1)\
                           .replace('{{GENRE2}}', GENRE2)\
                           .replace('{{GENRE3}}', GENRE3)\
                           .replace('{{GENRE4}}', GENRE4)\
                           .replace('{{URL}}', URL)
    
    with open(output_file, 'w', encoding='utf-8') as output_html:
        output_html.write(html_content)

movie_data = {
    "Titre": "#",
    "image_background": "#",
    "h1": "CACA",
    "PEGI": "#",
    "DUREE": "#",
    "RESUME": "#",
    "GENRE1": "#",
    "GENRE2": "#",
    "GENRE3": "#",
    "GENRE4": "#",
    "URL": "#"
}

generate_html('#.html', **movie_data)