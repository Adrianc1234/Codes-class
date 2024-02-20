## Database design and normalization
## Introduction
In this class, we will delve into the principles of database design and learn about normalization, its importance and how to apply it.

## Objectives:

By the end of the class, students will be able to:
- Identify the different components of a relational database.
- Describe the fundamental principles of database design.
- Understand the different normal forms and their importance for data integrity.
- Apply the principles of normalization to a case study.

## 1. Database design
## Components:

- Entity: A real-world object or concept that is represented in the database.

[Click to the topic](https://github.com/Adrianc1234/Topics-Repository/blob/f0f1529ee51b427b2188320a2134fc32cd9082c8/Database%20Management/Components/Entity.md)

- Attribute: A property or characteristic of an entity.

[Click to the topic](https://github.com/Adrianc1234/Topics-Repository/blob/f0f1529ee51b427b2188320a2134fc32cd9082c8/Database%20Management/Components/Attributes.md)

- Relationship: The connection between two entities.
- 
[Click to the topic](https://github.com/Adrianc1234/Topics-Repository/blob/f0f1529ee51b427b2188320a2134fc32cd9082c8/Database%20Management/Components/Relation.md)

## Fundamental principles:

- Atomicity: data should not be divided into smaller units.

[Click to the topic](https://github.com/Adrianc1234/Topics-Repository/blob/f0f1529ee51b427b2188320a2134fc32cd9082c8/Database%20Management/Principles/Atomicity.md)

- Consistency: Data must be accurate and consistent throughout the database.

[Click to the topic](https://github.com/Adrianc1234/Topics-Repository/blob/f0f1529ee51b427b2188320a2134fc32cd9082c8/Database%20Management/Principles/Consistency.md)

- Integrity: Data must be complete and protected from unauthorized access.

[Click to the topic](https://github.com/Adrianc1234/Topics-Repository/blob/f0f1529ee51b427b2188320a2134fc32cd9082c8/Database%20Management/Principles/Integrity.md)

- Normalization: Redundancy and anomalies in the data must be avoided.

[Click to the topic](https://github.com/Adrianc1234/Topics-Repository/blob/f0f1529ee51b427b2188320a2134fc32cd9082c8/Database%20Management/Principles/Normalization.md)

[Diagram for these principles](https://www.google.com/url?sa=i&url=https%3A%2F%2Fgravitar.biz%2Fbi%2Fmodelo-acid-base-datos%2F&psig=AOvVaw1BJL330z6-G80rwERfohMW&ust=1708542275400000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMjI74zOuoQDFQAAAAAdAAAAABAE)

## Entity-relationship model (MER):

A tool for conceptual database design that uses entities, relationships and attributes to represent information.
[Click to the topic]()

Example:

- Entity: Student

- Attributes: Name, Enrollment, Career

- Relationship: Cursa (Student, Subject)

## 2. Standardization
## Definition:

Process of organizing data in a database to minimize redundancy and anomalies.

## Normal forms:

- First normal form (1NF): Each cell contains only one value and there are no duplicate rows.
- Second normal form (2NF): It is in 1NF and each non-key attribute is completely dependent on the primary key.
- Third normal form (3NF): It is in 2NF and there are no transitive attributes that depend on the primary key.

## Importance:

- Reduces data redundancy.
- Improves data integrity.
- Facilitates database update and maintenance.
- Optimizes query performance.


## Examples
### Unnormalized table:

| Estudiante | Materia    | Calificación |
|------------|------------|--------------|
| Juan Pérez | Matemáticas | 10           |
| Juan Pérez | Física      | 8            |
| María López| Matemáticas | 9            |

### Normalized Table:

- Estudiantes

| Estudiante | Matrícula | Carrera   |
|------------|-----------|-----------|
| Juan Pérez | 123456    | Ingeniería|
| María López| 654321    | Derecho   |

- Materias:

| Materia    | Código |
|------------|--------|
| Matemáticas| MAT101 |
| Física     | FIS202 |

- Calificaciones:

| Estudiante | Materia | Calificación |
|------------|---------|--------------|
| 123456     | MAT101  | 10           |
| 123456     | FIS202  | 8            |
| 654321     | MAT101  | 9            |


## 3. Application of standardization
## Steps:

- Identify the entities and their attributes.
- Define the relationships between entities.
-Convert the entity-relationship model into a set of tables.
- Apply the normalization rules to the tables.
## Tools:

- Database design software.
- Data flow diagrams.
- Data dictionary.

## 4. Summary
In this class, we have learned about the principles of database design and the importance of normalization. We have also seen how to apply normalization to a practical case.
