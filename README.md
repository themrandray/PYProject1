# pyproject1

# Jauno Vieglo Auto Sludinājumu Pārskatītājs  un Informētājs (Uz e-pastu)

Šī programma periodiski pārskata [SS.com](https://www.ss.com/lv/transport/cars/today/) vietni, lai atrastu jaunus vieglo auto sludinājumus. Ja tiek atrasts kāds jauns sludinājums, programma parāda informāciju par to ekrānā un nosūta paziņojumu uz norādīto e-pasta adresi.

## Galvenie Elementi

1. **`get_car_data` funkcija:** Iegūst informāciju par jauniem auto sludinājumiem no [SS.com](https://www.ss.com/lv/transport/cars/today/) vietnes, izmantojot `requests` un `BeautifulSoup` bibliotēkas. Atgriež sludinājumu sarakstu.

2. **`print_car_info` funkcija:** Izdrukā jauno auto sludinājumu informāciju uz ekrāna. Šī funkcija iterēs cauri katram elementam car_data (objektiem ar text atribūtu) un izdrukās to text atribūtu.

3. **`save_to_html` funkcija:** Saglabā pašreizējos auto sludinājumus HTML formātā failā ar nosaukumu "website.html". Jā tāda faila nav, programma to izveido.

4. **`find_new_ads` funkcija:** Salīdzina pašreizējos auto sludinājumus ar iepriekšējiem (current_ads ar previous_ads), lai atrastu jaunus sludinājumus, kas nav bijuši iepriekšējā sarakstā. Atgriež sarakstu ar jauniem sludinājumiem.

5. **`send_email` funkcija:** Sūta e-pasta paziņojumu ar jauno auto sludinājumu informāciju uz norādīto e-pasta adresi, izmantojot SMTP serveri un pievienojot HTML daļu. Uz e-pastu atnāk jauno sludinājumu auto dati (marka, dzinējs, gads, cena) jā tos satur jauns sludinājums.

6. **`main` funkcija:** Galvenā programma, kas periodiski pārbauda jaunos vieglo auto sludinājumus. Ja tiek atrasts jauns(i) sludinājums(i), to(s) izdrukā uz ekrāna un nosūta uz e-pastu. Pašreizējie sludinājumi tiek saglabāti HTML failā. Programma gaida 30 sekundes starp pārbaudēm.

## Bibliotēkas un Moduļi

- `requests`: Izveido HTTP pieprasījumu, lai iegūtu informāciju no web lapas.
- `bs4` (BeautifulSoup): Parsē HTML un izvēlas nepieciešamos elementus.
- `time`: Nodrošina laika aizture starp auto sludinājumu pārbaudēm.
- `smtplib`: Nodrošina funkcijas e-pasta sūtīšanai.
- `email.mime.multipart` un `email.mime.text`: Nodrošina iespēju veidot MIME tipa e-pasta ziņojumus ar alternatīvām versijām.

## Konfigurācija

Konfigurācijas informācija, piemēram, e-pasta adrešu, servera, un paroles dati, tiek iegūti no `config` faila.

[Email]
- `HOST` = "smtp.example.com" vai "smtp.gmail.com"
- `PORT` = 587
- `USERNAME` = "jusu_epasta_adrese@example.com" vai "jusu_epasta_adrese@gmail.com"
- `PASSWORD` = "jusu_epasta_parole" vai "lietojumprogrammas_parole" (ja ieslēgta divfaktoru autentifikācija)

[Recipient]
- `SENDTO` = "nosutitajam@example.com" vai "nosutitajam@gmail.com"

## Lietošana

Lai sāktu programmu, jāizpilda `main` funkcija, kas regulāri pārbauda jaunos auto sludinājumus un informē par tiem gan uz ekrāna, gan arī nosūta e-pasta paziņojumus. Jā, piemēram, uz viedā telefona uzinstalēt e-pasta klientu un tajā ieslēgt pazīņojumus, tad var sēkot līdzi jauniem vieglo auto sludinājumiem.

Pirms lietošanas, lūdzu, pārliecinieties, ka visi nepieciešamie moduļi ir instalēti, un konfigurācijas fails `config.py` ir pareizi konfigurēts ar jūsu e-pasta servera informāciju.

Šī ir projekta sākotnēja versija, kura ar laiku pilnveidosies.

Video ar programmatūras darbību un rezultātu: <https://www.loom.com/share/522fcb8a412c40b3b12c0657ee295047?sid=32a36216-0ced-4781-a98e-db80c2a3132c>
