# Random Meal Generator
Following the QAC Practical Project Specification (DevOps) due 15th June 2020.

## Index
1. [Brief](#brief)
    - [Project Proposal](#pp)

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

<div align="center">![](documentation/images/proposalimage.PNG)</div>