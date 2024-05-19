Estoy creando una aplicación de productividad (tipo notion o google calendar) en archivos de texto plano como .txt o .md
Inspirado en https://youtu.be/EUCneUnGjv8?si=OK-mjSVM2Gelj66z
Pero amoldado a mis necesidades, creado con mis conocimientos y en base a mis gustos.

18/05/24 empecé con el proyecto e hice pruebas con la librería de python datetime y algunos de sus modulos (calendar, timedelta). Avancé hasta conseguir la fecha del dia de hoy y las siguientes para poder usarlo en el calendario. Por ejemplo:
for i in range(20):
        file.write(f"{hoy+timedelta(days=i)} {weekday((hoy+timedelta(days=i)).day)}\n")
        print((hoy+timedelta(days=i)).day)
este código me permite ver las siguientes 20 fechas y que dia de la semana es.
