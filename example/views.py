from datetime import datetime

from django.http import HttpResponse


def index(request):
    now = datetime.now()
    html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  
</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">GeoStat Espacial</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="#">Inicio</a></li>
      <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">Pagina 1<span class="caret"></span></a>
        <ul class="dropdown-menu">
          <li><a href="#">Page 1-1</a></li>
          <li><a href="#">Page 1-2</a></li>
          <li><a href="#">Page 1-3</a></li>
        </ul>
      </li>
      <li><a href="#">Pagina 2</a></li>
    </ul>
    <ul class="nav navbar-nav navbar-right">
      <li><a href="#"><span class="glyphicon glyphicon-user"></span> Inscrever-se</a></li>
      <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> Entrar</a></li>
    </ul>
  </div>
</nav>
  
<div class="container">
  <h3>Right Aligned Navbar</h3>
  <p>The .navbar-right class is used to right-align navigation bar buttons.</p>
</div>

<div class="container">
  <h2>Justified Button Groups</h2>
  <p>To span the entire width of the screen, use the .btn-group-justified class:</p>
  <div class="btn-group btn-group-justified">
    <a href="#" class="btn btn-primary">Apple</a>
    <a href="#" class="btn btn-primary">Samsung</a>
    <a href="#" class="btn btn-primary">Sony</a>
  </div>
</div>

</body>
</html>


    '''
    return HttpResponse(html)
