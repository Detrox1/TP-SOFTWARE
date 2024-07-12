<h1 align="center">¡Bienvenidos al juego Simsmejo!</h1>
<h2 align="center">Grupo conformado por Franco Lamas, Diego Mercado y Ezequiel de la Torre Lasala</h2>

<h3 align="center">Este es un fantástico juego para pasar el rato creando una hermosa ciudad. En esta ciudad, tú eres el alcalde y tendrás que construir diferentes edificios que te proporcionarán dinero o población. Con el dinero, podrás seguir construyendo o mejorando los diferentes edificios, mientras que la población te permitirá desbloquear más edificios para que tu ciudad se convierta en la mejor de todas. ¡Esperamos que pases un buen rato jugando a nuestro juego! 😄😄😄</h3>

### Pasos para instalar el juego

1. Descarga el código desde GitHub.
2. Posiciónate en la terminal en la carpeta `TP-SOFTWARE`.
3. Instala python3 con el comando `apt install python3.10-venv` si no lo tienes instalado.
4. Crea un entorno virtual con el siguiente comando: `python3 -m venv myenv`.
5. Activa el entorno virtual con el siguiente comando: `source myenv/bin/activate`.
6. Instala Flask en tu entorno con el siguiente comando: `pip install Flask`.
7. Instala Flask-CORS en tu entorno con el siguiente comando: `pip install flask-cors`.
8. Instala SQLAlchemy y psycopg2-binary en tu entorno con el siguiente comando: `pip install SQLAlchemy psycopg2-binary`.
9. Instala Flask SQLAlchemy en tu entorno con el siguiente comando: `pip install flask_sqlalchemy`.
10. Instala PostgreSQL con el siguiente comando `sudo apt install postgresql postgresql-contrib` si es que no lo tienes instalado. Verifica que PostgreSQL esté activo con este comando `sudo systemctl status postgresql`.
11. Accede al usuario PostgreSQL de la aplicación usando este comando `sudo -i -u postgres`. Abre la terminal de PostgreSQL con el comando `psql` y crea un nuevo usuario con `CREATE USER mi_usuario WITH PASSWORD 'mi_contraseña';` y dale el superusuario con `ALTER USER mi_usuario WITH SUPERUSER;`.
12. Luego de salir de la shell de PostgreSQL, ejecuta este comando `sudo -i -u postgres createdb -O mi_usuario nombre_bd`.
13. Para verificar la conexión puedes usar el siguiente comando `psql -U mi_usuario -d nombre_bd -W` para loguearte y este otro para verificar que la base de datos esté creada `\l`.
14. Ejecuta el backend para poder hacer solicitudes: `python3 app.py`.
15. Ejecuta este insert para tener la plantilla de datos:

    ```sql
    INSERT INTO tiposedificios (id, nombre, imagen, clase, poblacion, precio, descripcion, tiemporecaudacion, platarecaudacion) VALUES
    (1, 'Casa Humilde', 'https://www.aciprensa.com/imagespp/casahumildescolombia-240923.jpg?w=672&h=448', 'C', 4, 10, 'La Casa Humilde es el tipo de vivienda más básica y accesible dentro del juego. Construida con materiales sencillos y económicos, esta casa ofrece un refugio modesto pero acogedor para sus habitantes. Con una estructura simple y funcional, la Casa Humilde es ideal para los jugadores que recién comienzan su aventura o aquellos que prefieren un estilo de vida más sencillo.', '00:00:00', 0),
    (2, 'Casa de Ciudad', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv59Zj9g4BpisT7_8jDVvd9NrEcvaSu2_snA&s', 'C', 10, 20, 'La Casa de Ciudad es una vivienda diseñada para ofrecer comodidad y funcionalidad en el bullicio urbano. Construida con materiales duraderos y modernos, esta casa es ideal para aquellos que buscan una vida más conectada con el dinamismo de la ciudad. Con una estructura de varios pisos y un diseño contemporáneo, la Casa de Ciudad ofrece más espacio y comodidades avanzadas para sus habitantes.', '00:00:00', 0),
    (3, 'Conventillo', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9l7FFuzlHHGF1WUlzjMAoc1vogLeEEA6Npw&s', 'C', 30, 30, 'El Conventillo es una vivienda comunitaria típica de las áreas urbanas más antiguas, caracterizada por su estructura de múltiples habitaciones que alojan a varias familias. Construido con materiales básicos, este tipo de vivienda es una solución económica para quienes buscan un lugar donde vivir en la ciudad. Aunque las comodidades son limitadas, el sentido de comunidad y la vida compartida son características distintivas de este hogar.', '00:00:00', 0),
    (4, 'Edificio', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFwEiwhtG2BtZDM2ZNE72akP8RZUWa-vuVSw&s', 'C', 300, 350, 'El Edificio es una estructura urbana moderna, diseñada para albergar a varias familias o individuos en unidades separadas. Con múltiples pisos y un diseño eficiente, ofrece comodidades modernas y espacio para una vida confortable en la ciudad. Ideal para quienes buscan un estilo de vida más sofisticado y accesible a diversas facilidades urbanas.', '00:00:00', 0),
    (5, 'Mansion', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1PCj3qruCDQtgotx_Mdh-_ZwQhNBl_d1cvw&s', 'C', 20, 500, 'La Mansión es una lujosa residencia de gran tamaño, diseñada para proporcionar un nivel excepcional de comodidad y opulencia. Situada en un entorno exclusivo, esta vivienda es ideal para quienes buscan un estilo de vida de alta clase, con amplios espacios interiores y exteriores, acabados de primera calidad y todas las comodidades modernas imaginables.', '00:00:00', 0),
    (6, 'Chino', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFChsZ_WKfwPmhnGkNYmmAFNJqkA6I-xPAdQ&s', 'S', 0, 15, 'Supermercado chino que ofrece una amplia variedad de productos asiáticos, desde ingredientes frescos hasta artículos de cocina especializados.', '00:00:15', 1),
    (7, 'Tienda de ropa', 'https://phantom-telva.unidadeditorial.es/834cbdecd7feb5e11997245bea86ac92/crop/0x137/1998x1258/resize/828/f/jpg/assets/multimedia/imagenes/2020/11/11/16050829163655.jpg', 'S', 0, 20, 'La tienda de ropa es un establecimiento comercial que se dedica a la venta de prendas de vestir y accesorios relacionados.', '00:00:20', 5),
    (8, 'Cafeteria', 'https://dosg.net/wp-content/uploads/2018/03/cafeteria.jpg', 'S', 0, 20, 'La cafetería es un local comercial donde se sirven bebidas, principalmente café y té, así como una variedad de alimentos rapidos como pasteles, sándwiches, y snacks.', '00:00:25', 10),
    (9, 'Restaurante', 'https://media-cdn.tripadvisor.com/media/photo-s/17/59/9f/7f/salon-principal.jpg', 'S', 0, 30, 'El restaurante es un lugar donde se preparan y sirven platillos de buena elaboracion y bebidas a los clientes.', '00:00:30', 20),
    (10, 'Tienda de electrodomesticos', 'https://previews.123rf.com/images/starush/starush2005/starush200500029/147687319-interior-de-la-tienda-de-electrodom%C3%A9sticos-premium.jpg', 'S', 0, 35, 'La tienda de electrodomésticos es un lugar comercial que se especializa en la venta de aparatos eléctricos y electrónicos diseñados para el hogar.', '00:00:35', 40);

    ```

16. Entra al archivo `app.py` y en la línea 11 donde dice:
    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario_bd:contraseña_bd@localhost/nombre_bd'
    ```
    Modifica `'postgresql://usuario_bd:contraseña_bd@localhost/nombre_bd'` con usario_bd el usario con el que hayas creado la base de datos, contraseña_bd con la contraseña del usario y nombre_bd con el nombre de la base de datos.
