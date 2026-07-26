


SELECT person.first_name, person.last_name, address.city, address.state 
FROM person
left join address 
ON address.person_id = person.person_id;