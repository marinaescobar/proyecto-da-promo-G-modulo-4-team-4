Para facilitar el análisis de datos, hemos creado una ETL con funciones dedicadas a la exploración, limpieza y transformación de datos. Durante este proceso, identificamos lo siguiente y decidimos realizar las siguientes acciones:

## CAMBIOS DE TIPOS DE DATO:

**Convertir a entero las columnas**
-Primera fase: lead_time, arrival_date_year, arrival_date_week_number, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, is_repeated_guest, previous_bookings_not_canceled, previous_cancellations, booking_changes, days_in_waiting_list, required_car_parking_spaces, total_of_special.
-Segunda fase : arrival_date_year, arrival_date_month, arrival_date_week_number, arrival_date_day_of_month, children, previous_cancellations.
**is_repeated_guest** convertir a booleano True/False.

## VALORES:
**arrival_date_month** convertir los nombres de los meses en números.
**country**convertir los códigos de país en nombres de país.
**adr** algunos valores son negativos.
**reservation_status_date** quitar las horas de los datos.
**"arrival_date_day_of_month"** Cambiar el número de semana a su correspondiente mes.
**arrival_date_year**. Actualizar la columna utilizando la información de la columna reservation_status_date si arrival_date_year es nula y reservation_status_date no lo es.

## COLUMNAS ELIMINADAS:
**0 y company**
**arrival_date_year, arrival_date_month y arrival_date_day_of_month** al finalizar todas las acciones de limpieza y transformación.

## COLUMNAS AÑADIDAS:

**courtesy**. Crear nueva columna, que es True si el número de noches de fin de semana y el número de noches de semana son ambos cero, o si el Average Daily Rate (ADR) es cero; de lo contrario, es False.
**arrival_date**. Crear nueva columna que combina las columnas arrival_date_year, arrival_date_month y arrival_date_day_of_month en formato de fecha YYYY-MM-DD.

## Eliminar nulos
- Eliminar las filas que tienen todos los valores nulos.
- Elimina las filas que tienen más del 80% de valores nulos.

## Imputación de nulos :
- Con la mediana en las columnas : arrival_date_day_of, arrival_date_week_number, arrival_date_year.
- Con cero en las columnas: arrival_date_month, children, previous_cancellations,   is_repeated_guest, reservation_status_date.
- Con undefined en las columnas : meal,country, market_segment, distribution_channel, agent, reserved_room_type, assigned_room_type, customer_type.
- Actualizar reservation_status_date, utilizando arrival_date_year, arrival_date_month y arrival_date_day_of_month cuando reservation_status_date'es 0.


A continuación detallamos las funciones que  hemos creado para realizar las transformaciones y  obtener una base de datos limpia:

## def open_csv(rute):
Apertura del dataframe, Si el DataFrame tiene una columna llamada Unnamed: 0, la elimina.

## def explore_df(df):
Esta función imprime información básica sobre el DataFrame, como el tipo de datos y la cantidad de valores no nulos, y muestra las primeras 5 filas del DataFrame.

## def df_information(df):
Esta función proporciona una visión general rápida de los datos en el DataFrame, incluida la forma del DataFrame, los nombres de las columnas, el número de valores nulos y duplicados, y estadísticas descriptivas para cada columna.

## def explore_columns(df):
Proporciona una descripción básica de cada columna en un DataFrame, incluyendo el número total de valores, valores únicos, tipo de datos, valores nulos, valores duplicados y la cuenta de cada valor único en la columna.

## def limpieza (df):
- Homogeneiza la columna arrival_date_month convirtiendo los nombres de los meses en números.
- Homogeneiza la columna country convirtiendo los códigos de país en nombres de país.
- Crea una lista con las columnas lead_time, arrival_date_year, arrival_date_week_number, arrival_date_day_of_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, is_repeated_guest, previous_bookings_not_canceled, previous_cancellations, booking_changes, days_in_waiting_list, required_car_parking_spaces, total_of_special_requests y las convierte a tipo entero.
- Elimina la parte de la hora de la columna reservation_status_date si está presente.
- Actualiza la columna arrival_date_year utilizando la información de la columna reservation_status_date si arrival_date_year es nula y reservation_status_date no lo es.

## def eliminacion_nulos (df):
- Elimina las columnas 0 y company del DataFrame.
- Elimina las filas que tienen todos los valores nulos.
- Elimina las filas que tienen más del 80% de valores nulos.
- Crea una nueva columna llamada courtesy, que es True si el número de noches de fin de semana y el número de noches de semana son ambos cero, o si el Average Daily Rate (ADR) es cero; de lo contrario, es False.

## def imputacion_nulos (df):
- Calcula la mediana de arrival_date_day_of_month y lo utiliza para rellenar los valores nulos en esa columna.
- Mapea el número de semana a su correspondiente mes y utiliza este mapeo para rellenar los valores nulos en arrival_date_month cuando arrival_date_week_number no es 0 y arrival_date_month es 0.
- Rellena los valores nulos en las columnas (columns_to_0 ), arrival_date_month, children, previous_cancellations, is_repeated_guest, reservation_status_date con 0.
- Rellena los valores nulos en las columnas seleccionadas  (columns_to_undefined), meal,country, market_segment, distribution_channel, agent, reserved_room_type, assigned_room_type, customer_type con undefined.
- Rellena los valores nulos en arrival_date_week_number con su mediana
- Rellena los valores nulos en arrival_date_year con su mediana.
- Actualiza reservation_status_date utilizando arrival_date_year, arrival_date_month y arrival_date_day_of_month cuando reservation_status_date es 0.

## def limpieza_fase2 (df):
- Convierte la columna is_repeated_guest en tipo booleano, asignando False si el valor es 0 y True en caso contrario.
- Convierte las columnas (columns_to_int), arrival_date_year, arrival_date_month, arrival_date_week_number, arrival_date_day_of_month, children, previous_cancellations a tipo de datos entero.
- Crea una nueva columna llamada arrival_date, que combina las columnas arrival_date_year, arrival_date_month y arrival_date_day_of_month en formato de fecha YYYY-MM-DD.
-Elimina las columnas arrival_date_year, arrival_date_month y arrival_date_day_of_month del DataFrame.


