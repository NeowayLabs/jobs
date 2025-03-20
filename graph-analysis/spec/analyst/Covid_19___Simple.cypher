// Criar países com código ISO3
CREATE (:Country {name: "Brazil", iso3: "BRA"})
CREATE (:Country {name: "United States", iso3: "USA"})
CREATE (:Country {name: "Germany", iso3: "DEU"});

// Criar vacinas
CREATE (:Vaccine {name: "Pfizer-BioNTech"})
CREATE (:Vaccine {name: "Moderna"})
CREATE (:Vaccine {name: "AstraZeneca"});

// Criar casos de Covid-19
CREATE (:CovidCase {date: "2021-01-01", total_cases: 5000000, total_deaths: 200000})
CREATE (:CovidCase {date: "2021-02-01", total_cases: 5500000, total_deaths: 220000});

// Criar relação entre países e casos de Covid-19
MATCH (c:Country {iso3: "BRA"}), (case:CovidCase {date: "2021-01-01"})
CREATE (c)-[:HAS_COVID_CASE]->(case);

MATCH (c:Country {iso3: "BRA"}), (case:CovidCase {date: "2021-02-01"})
CREATE (c)-[:HAS_COVID_CASE]->(case);

// Criar registros de vacinação
CREATE (:VaccinationStats {date: "2021-01-10", total_vaccinated: 1000000})
CREATE (:VaccinationStats {date: "2021-02-10", total_vaccinated: 5000000});

// Associar vacinação ao país
MATCH (c:Country {iso3: "BRA"}), (v:VaccinationStats {date: "2021-01-10"})
CREATE (c)-[:VACCINATED_ON]->(v);

MATCH (c:Country {iso3: "BRA"}), (v:VaccinationStats {date: "2021-02-10"})
CREATE (c)-[:VACCINATED_ON]->(v);

// Criar relação entre países e vacinas usadas
MATCH (c:Country {iso3: "BRA"}), (v:Vaccine {name: "Pfizer-BioNTech"})
CREATE (c)-[:USES]->(v);

MATCH (c:Country {iso3: "BRA"}), (v:Vaccine {name: "AstraZeneca"})
CREATE (c)-[:USES]->(v);

// Criar relação entre vacinas e datas de autorização
CREATE (:VaccineApproval {vaccine: "Pfizer-BioNTech", date: "2020-12-10"});
CREATE (:VaccineApproval {vaccine: "Moderna", date: "2020-12-20"});
CREATE (:VaccineApproval {vaccine: "AstraZeneca", date: "2021-01-05"});

// Relacionar vacinas às autorizações
MATCH (v:Vaccine {name: "Pfizer-BioNTech"}), (a:VaccineApproval {vaccine: "Pfizer-BioNTech"})
CREATE (v)-[:APPROVED_ON]->(a);

MATCH (v:Vaccine {name: "Moderna"}), (a:VaccineApproval {vaccine: "Moderna"})
CREATE (v)-[:APPROVED_ON]->(a);

MATCH (v:Vaccine {name: "AstraZeneca"}), (a:VaccineApproval {vaccine: "AstraZeneca"})
CREATE (v)-[:APPROVED_ON]->(a);
