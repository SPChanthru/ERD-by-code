from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='Law Enforcement ERD')

# Configure graph attributes
dot.attr(rankdir='LR')  # Left to Right direction
dot.attr('node', shape='record')

# Define nodes (tables) with vertical attributes
dot.node('Officers', '''
Officers\l
--------------------\l
+ OfficerID (PK)\l
FirstName\l
LastName\l
BadgeNumber\l
Rank\l
Precinct\l''')

dot.node('Incidents', '''
Incidents\l
--------------------\l
+ IncidentID (PK)\l
IncidentDate\l
IncidentLocation\l
IncidentType\l
OfficerID (FK)\l
ReportNumber\l''')

dot.node('Arrests', '''
Arrests\l
--------------------\l
+ ArrestID (PK)\l
ArrestDate\l
ArrestLocation\l
PersonID (FK)\l
OfficerID (FK)\l
IncidentID (FK)\l''')

dot.node('People', '''
People\l
--------------------\l
+ PersonID (PK)\l
FirstName\l
LastName\l
DOB\l
Address\l''')

dot.node('Vehicles', '''
Vehicles\l
--------------------\l
+ VehicleID (PK)\l
LicensePlate\l
Make\l
Model\l
Color\l
PersonID (FK)\l''')

# Define relationships
dot.edge('Officers', 'Incidents', '1:N')
dot.edge('Officers', 'Arrests', '1:N')
dot.edge('Incidents', 'Arrests', '1:N')
dot.edge('People', 'Arrests', '1:N')
dot.edge('People', 'Vehicles', '1:N')

# Save and render the diagram
dot.render('law_enforcement_erd', view=True, format='png')