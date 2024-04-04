from string import Template

html_template = Template('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body>

$body

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
        crossorigin="anonymous"></script>
</body>

</html>
''')

html_informacion = Template('''
<div class="container">
        <div class="row">
            <div class="col-3">
                <div class="card mt-4 mx-4">
                    <img src="$url" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">$nombre_espanol</h5>
                        <h3 class="card-title">$nombre_ingles</h3>
                    </div>
                </div>
            </div>    
        </div>
    </div>
''')
