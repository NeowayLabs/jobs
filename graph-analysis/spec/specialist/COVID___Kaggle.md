
# <a id='_modelTop'></a>COVID - Kaggle

**Date:** Thu Sep 05 2024  
**Cypher Workbench Version:** 1.5.0  
**Description:** Graph Test  
**Stats:**  6 node labels, 8 relationship types,
19 node label properties, 0 relationship type properties  

### Table of Contents

#### Node Labels
* [Country](#Node0)
* [CovidStats](#Node9)
* [Date](#Node2)
* [Region](#Node1)
* [VaccinationStats](#Node3)
* [Vaccine](#Node10)

#### Relationship Types
* [AUTHORIZATION_ON](#Rel15)
* [BELONGS](#Rel1)
* [ON_DATE](#Rel18)
* [ON_DATE](#Rel13)
* [REPORTED_ON](#Rel12)
* [STARTED_ON](#Rel16)
* [USES](#Rel14)
* [VACCINATED_ON](#Rel17)
        
## Node Labels
--------------

### <a id='Node0'></a>Country <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---  

#### Country Outbound Relationships

Country - [BELONGS](#Rel1) -> [Region](#Node1)  
Country - [REPORTED_ON](#Rel12) -> [CovidStats](#Node9)  
Country - [USES](#Rel14) -> [Vaccine](#Node10)  
Country - [VACCINATED_ON](#Rel17) -> [VaccinationStats](#Node3)  

#### Country Properties

Node Key: code  
Unique Constraint Properties: code  
Indexed Properties: code  
Must Exist Properties: code, name  

**code**  
Datatype: String  
Node Key, Unique Constraint, Indexed, Must Exist    

**name**  
Datatype: String  
Must Exist        

### <a id='Node9'></a>CovidStats <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---  

#### CovidStats Outbound Relationships

CovidStats - [ON_DATE](#Rel13) -> [Date](#Node2)  

#### CovidStats Inbound Relationships

[Country](#Node0) - [REPORTED_ON](#Rel12) -> CovidStats  

#### CovidStats Properties

**cumulativeCases**  
Datatype: Integer    

**cumulativeDeaths**  
Datatype: Integer    

**newCases**  
Datatype: Integer    

**newDeaths**  
Datatype: Integer        

### <a id='Node2'></a>Date <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---  

#### Date Inbound Relationships

[Vaccine](#Node10) - [AUTHORIZATION_ON](#Rel15) -> Date  
[VaccinationStats](#Node3) - [ON_DATE](#Rel18) -> Date  
[CovidStats](#Node9) - [ON_DATE](#Rel13) -> Date  
[Vaccine](#Node10) - [STARTED_ON](#Rel16) -> Date  

#### Date Properties

Node Key: date  
Unique Constraint Properties: date  
Indexed Properties: date  
Must Exist Properties: date  

**date**  
Datatype: Date  
Node Key, Unique Constraint, Indexed, Must Exist        

### <a id='Node1'></a>Region <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---  

#### Region Inbound Relationships

[Country](#Node0) - [BELONGS](#Rel1) -> Region  

#### Region Properties

Node Key: name  
Unique Constraint Properties: name  
Indexed Properties: name  
Must Exist Properties: name  

**name**  
Datatype: String  
Node Key, Unique Constraint, Indexed, Must Exist        

### <a id='Node3'></a>VaccinationStats <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---  

#### VaccinationStats Outbound Relationships

VaccinationStats - [ON_DATE](#Rel18) -> [Date](#Node2)  

#### VaccinationStats Inbound Relationships

[Country](#Node0) - [VACCINATED_ON](#Rel17) -> VaccinationStats  

#### VaccinationStats Properties

**personsBoosterAddDose**  
Datatype: Integer    

**personsBoosterAddDosePer100**  
Datatype: Integer    

**personsLastDose**  
Datatype: Integer    

**personsLastDosePer100**  
Datatype: Integer    

**personsVaccinated1PlusDose**  
Datatype: Integer    

**personsVaccinated1PlusDosePer100**  
Datatype: Integer    

**totalVaccinations**  
Datatype: Integer    

**totalVaccinationsPer100**  
Datatype: Integer        

### <a id='Node10'></a>Vaccine <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---  

#### Vaccine Outbound Relationships

Vaccine - [AUTHORIZATION_ON](#Rel15) -> [Date](#Node2)  
Vaccine - [STARTED_ON](#Rel16) -> [Date](#Node2)  

#### Vaccine Inbound Relationships

[Country](#Node0) - [USES](#Rel14) -> Vaccine  

#### Vaccine Properties

Node Key: product  
Unique Constraint Properties: product  
Indexed Properties: product  
Must Exist Properties: company, product, vaccine  

**company**  
Datatype: String  
Must Exist    

**product**  
Datatype: String  
Node Key, Unique Constraint, Indexed, Must Exist    

**vaccine**  
Datatype: String  
Must Exist        

## Relationship Types
--------------

### <a id='Rel15'></a>AUTHORIZATION_ON <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---
[Vaccine](#Node10) - AUTHORIZATION_ON -> [Date](#Node2)    

### <a id='Rel1'></a>BELONGS <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---
[Country](#Node0) - BELONGS -> [Region](#Node1)    

### <a id='Rel18'></a>ON_DATE <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---
[VaccinationStats](#Node3) - ON_DATE -> [Date](#Node2)    

### <a id='Rel13'></a>ON_DATE <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---
[CovidStats](#Node9) - ON_DATE -> [Date](#Node2)    

### <a id='Rel12'></a>REPORTED_ON <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---
[Country](#Node0) - REPORTED_ON -> [CovidStats](#Node9)    

### <a id='Rel16'></a>STARTED_ON <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---
[Vaccine](#Node10) - STARTED_ON -> [Date](#Node2)    

### <a id='Rel14'></a>USES <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---
[Country](#Node0) - USES -> [Vaccine](#Node10)    

### <a id='Rel17'></a>VACCINATED_ON <span style="font-size:0.7em;">[[top]](#_modelTop)</span>
---
[Country](#Node0) - VACCINATED_ON -> [VaccinationStats](#Node3)    