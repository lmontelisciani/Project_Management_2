# 1. Project goal

Develop a project management system with time tracking of individual tasks of each project. Each project can have any number of tasks. Each task can have a status of "Stop", "Pending", "In progress". The system has several types of visual representation of tasks: kanban board, summary view with cards for each employee, view with metrics.

# 2. System description

The system consists of the following main functional blocks:
1. Registration, authentication and authorization.
2. Functionality for the employee.
3. Functionality for the project manager.
4. Notification system.

## 2.1 User types

The system provides for two types of users: employee and project manager. An employee can add himself as a task performer, manage tasks in which he is the performer. The project manager can manage any tasks.

## 2.2 Registration and authentication

The System is not designed as a SaaS for different teams. One particular installation of the System is attached to one particular team.

The process of subscriber registration and authentication should be designed into the interfaces of the System. The System provides a single sign-on (SSO) using Google Workspace.

## 2.3 Functionality for the employee
### 2.3.1 Profile editing
### 2.3.2 Editing and creating projects
### 2.3.3 Editing and creating project tasks
## 2.4 Functionality for the project manager
## 2.5 Notification functionality
## 2.6 Integration with other services
# 3. Technology Stack

To implement the system, the following technology stack is proposed:

- Backend:
  - Python language
  - FastAPI framework
  - PostgreSQL database
  - SQLAlchemy ORM
  - Alembic for migrations
- Frontend:
  - React
  - TypeScript

# 4. Design requirements
