# Agent_Sel
Agent selector
You are given the following data for agents 
agent
•	is_available
•	available_since (the time since the agent is available)
•	roles (a list of roles the user has, e.g. spanish speaker, sales, support etc.) 

When an issue comes in we need to present the issue to 1 or many agents based on an agent selection mode. An agent selection mode can be all available, least busy or random. In “all available mode” the issue is presented to all agents so they pick the issue if they want. In least busy the issue is presented to the agent that has been available for the longest. In random mode we randomly pick an agent. An issue also has one or many roles (sales/support e.g.). Issues are presented to agents only with matching roles.

The function takes an input the list of agents with their data, agent selection mode and returns a list of agents the issue should be presented to.

The function is implemented using Python and MySQL here. The database contains the data of all agents, their roles, availability, and the number of days since they are available.
The python code consists of all the functions and using the data from the database the agents which have the user input roles are filtered, and as per the given agent selection mode, the list of agents are returned to the user.

This project is useful to provide various services to the customers where users can provide their issues and the appropriate agent is allotted to them.
