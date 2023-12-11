k8sFMS - k8s Flight Management System
===============================================

Flight Management System Buit on Kubernetes


What is this?
---

- A scalable platform built on top of kubernetes to manage airline flights between different airlines. 

### Airports are split out in to a heiarchy as follows: 
---
Each Airline has a main hub airport wich connects to several spoke airports

![Alt text](/readme_images/flight-diagram.jpg)
---

To improve efficiancy it is sugested that the below rules are followed regaurding flight operations

Operational Rules
1. Flights from 1 hub can not go to another hubs spoke

2. Common operation spokes have common flights to and from hubs daily and hubs have common flights to each other daily

  - in the future we may design the platform to enforce this behavior


Quick-Start - Helm Install
--------------


To install run the below in the repo directory after it is cloned


Install CRDs into K8s: 

```bash
kubectl apply -f /k8s_crds
```

Install helm chart in K8s:

```bash
cd k8s_examples/helm/chart/

helm install appname --namespace namespace --create-namespace --set appName=appname ./k8sfms
```

K8sFMS TUI Operation
--------------
Terminal User Interface Operation


After helm chart is installed you can take advantage of the TUI(Terminal User Interface)

To access the Tui you have to exec into the pod in the deployment you deployed the helmchart. :

```bash
kubectl -n namespace exec -it podname -- bash
```


Once you exec into the pod you can run: 

```bash
python BasicTui.py
```

This will give you the TUI interface below:

![Alt text](/readme_images/tui-home.jpg)

From here you have a few sub menus: 
- Flights
    - View all of the flights in k8sfms
- Hubs
    - View all of the hubs in k8sfms
- Spokes
    - View all of the spokes in k8sfms
- Airlines
    - View all of the airlines in k8sfms
- Create
    - Add new objects to k8sfms

#### Airline Screen: 

![Alt text](/readme_images/tui-airline-screen.jpg)

#### Create Screen: 

![Alt text](/readme_images/tui-create-screen.jpg)

#### Flights Screen: 

#### Hubs Screen: 

![Alt text](/readme_images/tui-hub-screen.jpg)

#### Spokes Screen: 

![Alt text](/readme_images/tui-spoke-screen.jpg)

##### Future to do list

```
I need to make tables for create screen + return button on create screen
I need to make it auto change names to lowercase when creating resources and add a dash between spaces
```