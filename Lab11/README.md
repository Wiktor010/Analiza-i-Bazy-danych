## 1 . Ile rekordów znajduje się w tabeli nyc_streets?
* SQL:
* SELECT COUNT(* ) as number_of_streets" <br/>
FROM "nyc_streets" <br/>
* Answer : 19091
* ![1](https://user-images.githubusercontent.com/82833906/209726120-2f00c5fc-3814-43a0-812d-db2ce0cbf287.png)
## 2 . Ile ulic w Nowym Jorku ma nazwy zaczynające się na "B", "Q", "M" ?
* SQL:
* select count (name) as "number_of_selected_streets" <br/>
FROM "nyc_streets" <br/>
where name like 'B%' or name like 'Q%' or name 'M%'
* Answer (suma) : 2102
* ![2](https://user-images.githubusercontent.com/82833906/209726945-7eae007d-7af1-4757-b203-972a74cddbe7.png) <br/>
* Na literę B <br/>
* Answer : 1282 <br/> 
![2_1](https://user-images.githubusercontent.com/82833906/209727402-0cfdb903-ae89-4112-9dc6-f6da91811ad2.png)
* Na literę Q <br/>
* Answer : 68 <br/> 
![2_2](https://user-images.githubusercontent.com/82833906/209727525-40ec16d6-24d0-4917-a191-4130c5979c74.png)
* Na literę M <br/>
* Answer : 752 <br/> 
![2_3](https://user-images.githubusercontent.com/82833906/209727600-8d8a07aa-0806-4307-90d9-9d9162dca20b.png)
## 3 . Jaka jest populacja miasta Nowy Jork?
* SQL:
* select sum(popn_total) as "city_population" <br/>
from "nyc_census_blocks" <br/>
* Answer : 8175032
* ![3](https://user-images.githubusercontent.com/82833906/209727903-39ceded1-e173-4bd0-a90d-22d42698bc9e.png)
## 4 . Jaka jest populacja Bronxu, Manhattanu i Queens?
* SQL:
* select sum(popn_total) as "city_population" <br/>
from "nyc_census_blocks" <br/>
where boroname in ('The Bronx', 'Manhattan', 'Queens') <br/>
* Answer : Queens(2230621), The Bronx(1385108), Manhattan(1585873)
* ![4](https://user-images.githubusercontent.com/82833906/209728271-827522ef-22e7-4c7b-9b5f-786a66123ce7.png)

## 5. Ile dzielnic ("neighborhoods") znajduje się w każdej gminie (borough)?
* SQL:
* SELECT boroname, COUNT(name) as number_of_neighbours <br/>
from nyc_neighborhoods <br/>
group by boroname <br/>

* Answer: 
Queens(30), Brooklyn(23), Staten Island(24), The Bronx(24), Manhattan(28) <br/>
![5](https://user-images.githubusercontent.com/82833906/209729635-d7a46caa-8ea3-4920-b24e-f6721ddef9f6.png)
