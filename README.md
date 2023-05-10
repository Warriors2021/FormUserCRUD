<h1>API REST en FASTAPI para realizar un CRUD en un formulario de usuarios</h1>
<p>Este proyecto está elaborado en FastAPI y permite crear una API REST que implementa un CRUD y se puede utilizar como un microservicio. Además, utiliza una base de datos MySQL, la cual debe ser configurada previamente antes de ejecutar este proyecto.</p>

<h2>Clonar este proyecto</h2>

<pre><code>git clone https://github.com/Warriors2021/FormUserCRUD.git
</code></pre>

<h2>Variables de entorno</h2>
<p>Para configurar la aplicación, es necesario establecer las siguientes variables de entorno:</p>
<ul>
  <li><code>DATABASE_NAME</code>: El nombre de la base de datos que ya se ha creado.</li>
  <li><code>DATABASE_USER</code>: El nombre de usuario, por defecto es <strong>"root"</strong>, o el que se ha creado para la base de datos.</li>
  <li><code>DATABASE_PASSWORD</code>: La contraseña del usuario de la base de datos.</li>
  <li><code>DATABASE_HOST</code>: La dirección IP donde se encuentra ejecutándose la base de datos MySQL.</li>
  
</ul>

<h2>Creación de entorno virtual</h2>

<p>De esta forma creamos un entorno virtual:</p>

<pre><code>virtualenv venv
</code></pre>

<h2>Requerimientos</h2>
<ul>
  <li>Python 3.10</li>
  <li>Base de datos MySQL</code></li>
  <li>Instalacion del documento requirements.txt</li>
  <lo><pre><code>fastapi==0.95.0
uvicorn==0.21.1
python-dotenv==1.0.0
mysqlclient==2.1.1
pydantic[email]
</code></pre></lo>
</ul>





<h2>Instalación de requerimientos en el entorno virtual</h2>

<p>De esta forma instalamos el archivo requirements.txt:</p>

<pre><code>pip install -r requirements.txt
</code></pre>


<h2>Ejecución de la API REST</h2>
<p>Para ejecutar nuestra API REST y permitir que escuche en <code>http://localhost:8000</code>, podemos utilizar el siguiente comando:</p>
<pre><code>python main.py
</code></pre>
<p>Al ejecutar este comando por primera vez, si no existe una tabla llamada "users" en la base de datos MySQL, se creará automáticamente para que podamos trabajar con ella.</p>
<h2>Endpoints disponibles para peticiones GET</h2>
<ul>
  <li><code>http://localhost:8000/docs</code></li>
  <li><code>http://localhost:8000/users</code></li>
  <li><code>http://localhost:8000/cities</code></li>
</ul>
<h2>Endpoints disponibles para peticiones POST</h2>
<ul>
  <li><code>http://localhost:8000/user</code></li>
  <li><code>http://localhost:8000/user/delete</code></li>
  <li><code>http://localhost:8000/user/update</code></li>
  <li><code>http://localhost:8000/city</code></li>
  <li><code>http://localhost:8000/register</code></li>
</ul>


<h2>Ejemplo completo de registro de usuario</h2>
<p>Para registrar usuarios, debemos utilizar el método de endpoint <code>http://localhost:8000/register</code>, el cual tiene ciertas condiciones que deben cumplirse para poder registrar un usuario:</p>
<ul>
  <li>El usuario debe ingresar una fecha de nacimiento, la cual se valida para asegurar que el usuario sea mayor de 18 años.</li>
  <li>Solo se permite un máximo de 3 ciudades en la base de datos, y esta condición se verifica antes de registrar o actualizar al usuario.</li>
</ul>
<h2>Json para consumo de la api</h2>

<pre><code>{
  "sexo": "Masculino",
  "fecha_de_nacimiento": "1996-05-10",
  "nombre": "Alexander",
  "apellido": "Pabon",
  "email": "hapabonm@gmail.com",
  "direccion": "CR 18 20 25",
  "casa_apartamento": "Casa",
  "pais": "Colombia",
  "departamento": "Meta",
  "ciudad": "Villavicencio"
}
</code></pre>
<h2>Curl para registro de usuario</h2>
<pre><code>curl -X 'POST' \
  'http://localhost:8000/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sexo": "Masculino",
  "fecha_de_nacimiento": "1996-05-10",
  "nombre": "Alexander",
  "apellido": "Pabon",
  "email": "hapabonm@gmail.com",
  "direccion": "CR 18 20 25",
  "casa_apartamento": "Casa",
  "pais": "Colombia",
  "departamento": "Meta",
  "ciudad": "Villavicencio"
}'
</code></pre>


<h2>Descripción de cada endpoint</h2>
<ul>
  <li><code>http://localhost:8000/docs</code>: Este endpoint nos proporciona una interfaz interactiva generada por FastAPI que muestra y permite interactuar con los demás endpoints creados.</li>
  <li><code>http://localhost:8000/register</code>: Este endpoint utiliza el método POST y nos permite enviar información para registrar usuarios. Se aplican validaciones de edad y ciudad, y devuelve información sobre el estado del registro.</li>
  <li><code>http://localhost:8000/users</code>: Este endpoint utiliza el método GET y nos devuelve todos los usuarios existentes en la base de datos en formato JSON.</li>
  <li><code>http://localhost:8000/cities</code>: Este endpoint utiliza el método GET y nos devuelve todas las ciudades existentes en la base de datos, junto con la cantidad de usuarios asociados a cada ciudad, en formato JSON.</li>
  <li><code>http://localhost:8000/user</code>: Este endpoint utiliza el método POST y nos permite consultar información de un usuario mediante su ID.</li>
  <li><code>http://localhost:8000/user/delete</code>: Este endpoint utiliza el método POST y nos permite eliminar un usuario enviando su ID.</li>
  <li><code>http://localhost:8000/user/update</code>: Este endpoint utiliza el método POST y nos permite actualizar un usuario enviando su ID junto con la información completa del usuario. También realiza validaciones de edad y ciudad (no más de 3 ciudades). </li>
  <li><code>http://localhost:8000/city</code>: Este endpoint utiliza el método POST y nos permite consultar información sobre una ciudad enviando el nombre de la ciudad. Retorna la ciudad y la cantidad de usuarios asociados a ella en la base de datos.</li>  
</ul>