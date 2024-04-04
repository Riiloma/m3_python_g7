from string import Template
img_template = Template('<img src="$url">')
html_template = Template('''<!DOCTYPE html>
<html>
<head>
<title>Título de la Página</title>
</head>
<body>
<h1>Nuestra página Web</h1>
$body
</body>
</html>
''')
lista_url = [elemento['url'] for elemento in response]
texto_img = ''
for url in lista_url:
    texto_img += img_template.substitute(url = url)+'\n'
print(texto_img)