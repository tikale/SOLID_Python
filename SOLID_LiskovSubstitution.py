# 3. Liskov Substitution Principle   - Liskov
#		Jeśli S jest podtypem T, to obiekty T mogą być zastępowane obiektami typu S bez modyfikowania funkcjonalności programu. 
#		np. klasa ptak ma funkcje lataj, pingwin dziedziczy po klasie ptak, ale ponieważ jest nielotem funkcja lataj dla pingwina nie ma sensu.
#		Dlatego wramach zgodności z zasadą Liskov. Pingwin nie może dziedziczyć po klasie ptak.