# Random Meal Generator
Following the QAC Practical Project Specification (DevOps) due 15th June 2020.

## Index
1. [Brief](#brief)
    - [Project Proposal](#pp)
2. [Trello Board](#tb)
    - [Initial Board](#ib)
    - [On-going Changes](#ogc)

## Brief
Create an application that randomly generates 'Objects' upon a set of predefined rules. 

The requirements are, however not limited too:
- A micro-service orientated structure involving at least 4 services working together.
- Persisting data in a MySQL database.
- A functioning application implementing the Feature-Branch model 
- Kanban Board: Trello
- Version Control: Git
- Continuous Integration Server: Jenkins 
- Configuration Management: Ansible Playbook
- Multiple GCP Virtual Machines
- Containerisation: Docker
- Orchestration Tool: Docker Swarm 

### Project Proposal <a name="pp"></a>
An application that generates a random meal, more specifically 'food' and 'drink', shown through a front-end website. This will be split across 4 services:
- Service 1: The website. This service is accountable for the display of persistent data. Essentially, a flask application with a single HTML template that communicates with all other services.
- Service 2: Generates 'food' for the user.
- Service 3: Generates 'drink' for the user.
- Service 4: Collects and formats the data from Services 2 & 3, returning it to Service 1 to be displayed. 

#<p align="center">![](documentation/images/proposalimage.PNG)</p>

The above diagram demonstrates how I imagined the user-interface would look like. The 'Generate' button refreshes the page, which re-runs the functions in all services to produce a new outcome. Then, previously generated objects are stored in an external MySQL database, fulfilling the persistent data deliverable in the project brief.

## Trello Board <a name="tb"></a>
A kanban-style Trello Board was used for project tracking. Agile methodology was implemented where possible, in line with the project brief (i.e. Product and Sprint backlogs). However, due to the individual nature of the project, no scrum activities were carried out. Therefore, the work conducted can be described as a single sprint.

The Trello Board can be accessed <a href="https://trello.com/b/RpOSyLLh/sfia2-project">here</a>.

### Initial Board <a name="ib"></a>
![](documentation/images/initial_board.PNG)

I started by adding the required lists, then populating the 'Product Backlog' field with user stories and the 'Sprint Backlog' field with tasks that when completed, would satisfy the user stories. Moreover, MoSCoW prioritisation was utilised by labelling tasks with 'MH' for must have, 'SH' for should have, and 'CH' for could have. This helped me to order the tasks that should be completed first, and which tasks could be completed towards the end of the project within the given timescale.

### On-going Changes <a name="ogc"></a>
![](documentation/images/updated_board.PNG)