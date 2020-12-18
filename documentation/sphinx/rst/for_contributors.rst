For Contributors
================


Testowanie
~~~~~~~~~~~
Testy oprócz swojej natury zapewniajacej stabilizację kodu i łatwiejsze rozbudowywaniie aplikacja zmiejszajace ryzoku wystąpienia błędów są także swoistą dokuemntacją projektu.
Pokrycie kodu testami czy to jednsotkowymi (Unit Test - UT)


Rodzaje testów
----------------

UT (Unit Tests) Testy jednostkowe

- jak nazwa wskazuje są to testy sprawdzajace pojedyncza unckjonalnosć często na najniżym poziomie aplikacji
- procentowo najwięcej testów to testy UT
- bardzo szybkie w działaniu
- nie wykorzystują danych z bazy - częste mockowanie obiektów


IT (Integration Test)

- testy zwiazane z fukncjonalnościami korzystającymi z bazy danych
- na potrzeby testów tworzona jest tymczasowa baza danych (odpowiadają za to użyte w testach frameworki)
- w klasach testujących tworzy się tymczasowe dane wykorzystywane do testów
- testy z reguły wykonują się zdecydowanie dłuzej niż testy jednostkowe


Testy funkcjonale

- testy funkcjonalności/feature np rejestracji użytkownika
- najwolniejsze z testów
- wykorzystywane do testowania dla wszystkich rodzajów danych - prawidłowych, nieprawidłowych, inne rodzaju np.: niebezpiecznych testójących możliwość SQL injection

Smoke Test

- https://www.altkomakademia.pl/baza-wiedzy/qna/discussion/1020/smoke-testy-czym-sa/p1
- test mający sprawdzić powierzchownie większą częśc apliakcjai - np jedną ścieżkę którą podąża użytkownik (np. od rejestracji konta do opublikowania posta)
- rzadziej spotykane w praktyce
- można myslec o nich jak o bardzo rozbudowanych/ połaczonych kilku testach funkcjonalnych
- często sprawdzają tylko happy path (dla prawidłowych danych)
- test pobieżny
- test zajmujący niewiele czasu
- test poszukujący bardzo wyraźnych problemów
- test dopuszczający do kolejnego etapu prac




Three L - Trzy poziomy testowania
------------------------------------
Easy/ Happy path:

- test upewnienia się że program działa prawidłowo dla prawisłowych danych (input)


Medium:

- Test upewnia się, że program działa prawidłowo dla podanych (input) nieprawdiłowych danych


Hard:

- Upenwieni się, że [program działa prawidłowo dla jakiegokolwie typu dancyh wejściowych (input)
- Można do tego zaliczyć testy


Uruchomienie testów w backend aplikacji sarenka
-------------------------------------------------





Dobre praktyki dla developerów (Code Contribution Guidelines)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- typing
- pisanie testów jednostowych
- tworzenie pydoc zgodnie z PEP 257 https://www.python.org/dev/peps/pep-0257/
- dokuemntacja kodu w formacie restructured text https://www.python.org/dev/peps/pep-0287/

