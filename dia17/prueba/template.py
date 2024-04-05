from string import Template
"""genera un template que basico con "html_template" y un template que genera un card con "html_informacion"
"""

#Creando el template principal
html_template = Template('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de chile</title>
    <meta name="author" content="Livio Gutierrez">
    <meta name="description" content="informacion de aves de chile">
    <meta name="keywords" content="aves,chile, aves chilenas">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/css/style.css">
</head>

<body>
    <div class="container">
            <h1 class="text-center">Aves de chile</h1>
            <div class="row d-flex justify-content-center">
    $body
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>
''')

#Creando el template del card
html_informacion = Template('''
                <div class="col-12 col-xl-3 mt-3">
                    <div class="card mt-4 mx-4">
                        <img src="$url" class="card-img-top" alt="pajarito">
                        <div class="card-body">
                            <h5 class="text-center card-title">$nombre_espanol</h5>
                            <hr>
                            <br>
                            <h6 class="card-title titulo_ingles">$nombre_ingles</h6>
                        </div>
                    </div>
                </div>
''')