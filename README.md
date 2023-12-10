k8sFMS - k8s Flight Management System
===============================================

Flight Management System Buit on Kubernetes


What is this?
---

- A scalable platform built on top of kubernetes to manage airline flights between different airlines. 

### Airports are split out in to a heiarchy as follows: 
---
Each Airline has a main hub airport wich connects to several spoke airports

(image here)

hub
   -  spoke  

(image here)

To improve efficiancy it is sugested that the below rules are followed regaurding flight operations
  - in the future we may design the platform to enforce this behavior


Operational Rules
1. Flights from 1 hub can not go to another hubs spoke

2. Common operation spokes have common flights to and from hubs daily and hubs have common flights to each other daily


Quick-Start - Helm Install
--------------


To install run the below in the repo directory after it is cloned

```bash
cd k8s_examples/helm/chart/

helm install --namespace namespace --create-namepsace --set appName=appname ./k8sfms
```

##### Future to do list

```
I need to make tables for create screen + return button on create screen
I need to make it auto change names to lowercase when creating resources and add a dash between spaces
```