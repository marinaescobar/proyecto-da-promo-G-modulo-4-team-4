


- Cambiar ISO por nombre país ✅
- Año llegada poner en formato fecha
- Lead_time tine que ser un int ✅ 
- hacer un concat de fecha con arrival_date (day,month, year) formato Año, mes, día
- Cortesía. Si/no ✅
- Ver por que en ADR hay valores negativos. ¿Son devoluciones? 14969 mirar esta linea, es la única con nulos
- Arrival date month tiene los valores en texto y valores con el Nº del mes ✅
- Arrival date day cambiar a integer
- Stay in weekend nights, están en en float, hay que cambiarlo
- Stay in week nights, están como float
- Adults revisar lo que está a cero
- Is_repited_guest cambiar a true & false
- Previos cancelation: tiene muchos nulos
- Para las categóricas con nulos, utilizar undefined
- Agente y company convertir a object 
- Reservation status date. Hay fechas con horas, quitarlas para hacer homogéneo el dato
- No existe identificador único de la habitación, recomendar su incluisión en el DataFrame. En gestión de duplicados, no los eliminamos porque pueden ser reservas diferentes con el mismo cliente.

- Children, babies, previous_cancellations: Nan = 0
- meal	country	market_segment	distribution_channel, agent, reserved_room_type, assigned_room_type, customer_type: Nan = Undefined



arrival_date_year                 4.59
arrival_date_month                7.85
arrival_date_week_number         14.88
arrival_date_day_of_month         0.00
stays_in_weekend_nights           0.00
stays_in_week_nights              0.00
adults                            0.00
children                         41.35
babies                            0.00
meal                              0.00
country                          44.89
market_segment                   49.23
distribution_channel             10.87
is_repeated_guest                 4.01
previous_cancellations           35.52
previous_bookings_not_canceled    0.00
reserved_room_type               32.92
assigned_room_type                0.00
booking_changes                   0.00
agent                            13.19
days_in_waiting_list              0.00
customer_type                    20.47
adr                               0.00
required_car_parking_spaces       0.00
total_of_special_requests         0.00
reservation_status                0.00
reservation_status_date          10.39
courtesy                          0.00