---
title: "Course Page"
date: 2021-12-24T18:15:26+02:00
---

Instructor
: [Antony Chazapis](http://users.ics.forth.gr/~chazapis/)

Graduate studies area
: (C) Parallel and Distributed Systems

Undergraduate studies elective category
: (E5) Software Systems and Applications

Credits
: 6 ECTS

Prerequisites
: CS-335 (Computer Networks), CS-345 (Operating Systems) or permission from the instructor

Lecture schedule
: Monday and Wednesday 14:00-16:00, in room H.206 (spring semester 2025)

Contact:
: hy548_at_csd.uoc.gr (instructor), hy548-list_at_csd.uoc.gr

# Course Description

The Internet provides services to billions of users worldwide. News sites, social media networks, e-shops, government agencies, and so on, must be online around the clock, no matter the load. As such, contemporary Internet-scale applications are deployed in the Cloud. Their internal architectures have evolved into complex webs of "microservices", physically dispersed around the globe, using virtualized resources and software components supplied by the cloud providers. In this course we explore the structure of large-scale Internet services and focus on the techniques and tools used to build and deploy modern-day applications in cloud platforms, including containers and "serverless" functions. Through a series of hands-on sessions and assignments students are guided into mastering the advanced usage and understanding the working internals of Kubernetes, which has become the de facto standard for abstract, cross-cloud service composition. Additionally, we expand on how Kubernetes is actually used by big cloud providers, such as Amazon and Google, and how deployed container-based microservice architectures can utilize respective supporting services and APIs to achieve uninterrupted operation at a global-scale.

# Goals

The aim of the course is to provide a substantial understanding of how to build, compile and execute a complex Internet-scale application in the Cloud, which includes:
* Familiarity with the distinctive specifications of both large-scale applications and the Cloud environment.
* Techniques and tools for writing applications, managing library requirements, and integrating them into containers.
* The design and implementation of micro-service architectures and the utilization of Cloud service offerings, such as serverless functions.
* The advanced use of a modern cloud orchestration application platform, such as Kubernetes, through the understanding of its internal structure.

# Syllabus

| Week | Short description |
|---|---|
| 1 | Introduction to cloud-native software architectures (application examples, the need for DevOps, Cloud infrastructure) [[slides](https://docs.google.com/presentation/d/1RZzmujB8rtA_11wjZfNnVb4hVxzWKhxghzOYBgE9b8g/edit?usp=sharing)] |
| 2-3 | Container execution environments (Docker usage: container synthesis, application execution, variables, files, networking) [[slides](https://docs.google.com/presentation/d/1-8-d5m99KuEPr03yP4fWL7kJe4DpTcufIOls5J-u7Gw/edit?usp=sharing)] |
| 4-5 | Orchestration platforms (Kubernetes usage: commands, abstract concepts, service composition) [[slides](https://docs.google.com/presentation/d/1rbOD4FsIkqvJ5eTlu4NZgc6HNYts7JWPiuV7dhiaeRY/edit?usp=sharing)] [[examples](https://github.com/chazapis/hy548/tree/master/examples)] |
| 6 | Auto-scaling and serverless (use of the autoscaler, functions as a service) [[scaling example](https://github.com/chazapis/hy548/tree/master/scaling)] [[serverless example](https://github.com/chazapis/hy548/tree/master/serverless)] |
| 7-9 | Platform components (Kubernetes internal structure, usage and extension APIs, scheduler, operators, CNI, CSI, intra-platform networking, Edge integration) [[CRI, CNI, CSI slides](https://docs.google.com/presentation/d/143pYlJpSSmAO3VMlkR0xCIz4Ik5WEBgUoH-T9BS_-YE/edit?usp=sharing)] [[scheduler slides](https://docs.google.com/presentation/d/17Mu-VYD1N0n8Dlz8XRBcxar32GPPp3YP/edit?usp=sharing&ouid=113659041026588075056&rtpof=true&sd=true)] [[CRD example](https://github.com/chazapis/hy548/tree/master/crds)] [[webhook example](https://github.com/chazapis/hy548/tree/master/webhooks)] |
| 10-12 | Project presentations |
| 13 | Cloud platforms (services offered, APIs), course overview [[slides](https://docs.google.com/presentation/d/15nMhkmO5X5QNrJ4_NXVXm-cIcIs9pyYK5hppM1bCpvA/edit?usp=sharing)] |

Other presentations: [[Helm](https://docs.google.com/presentation/d/1sX4Na8tyYyiXskRGMW19F0cNjkmdqwDfc2IJqzosNB4/edit?usp=sharing)] [[Operator Framework](https://docs.google.com/presentation/d/1KhInA-3lga7bjPX6BeZo0I1SoOXNZLvQEgsYa-8JGIA/edit?usp=sharing)]

# Suggested Reading

There is no required textbook. The following material is relevant to the syllabus and will be covered in lectures.

Internet-Scale Services:
* Architecture and design of high volume web sites: (a brief history of IBM sport and event web sites). Paul Dantzig. Proceedings of the 14th international conference on Software engineering and knowledge engineering (SEKE '02), July 2002, pp. 17-24 [[available online](https://doi.org/10.1145/568760.568765)]
* Architecture and Dependability of Large-Scale Internet Services. David Oppenheimer and David Patterson. IEEE Internet Computing, vol. 6, no. 5, pp. 41-49, Sept.-Oct. 2002, [[available online](http://roc.cs.berkeley.edu/papers/inet-computing.pdf)]
* On Designing and Deploying Internet-Scale Services. James Hamilton. Proceedings of the 21st Large Installation System Administration Conference (LISA '07), pp. 231-242, Dallas, TX, USENIX Association, Nov. 2007 [[available online](https://www.usenix.org/legacy/event/lisa07/tech/full_papers/hamilton/hamilton_html/index.html)]
* Microservices: The Journey So Far and Challenges Ahead. Pooyan Jamshidi, Claus Pahl, Nabor C. Mendonça, James Lewis, Stefan Tilkov. IEEE Software, vol. 35, no. 3, pp. 24-35, May/June 2018 [[available online](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8354433)]

Containers and Kubernetes:
* Containers and Cloud: From LXC to Docker to Kubernetes. David Bernstein. IEEE Cloud Computing, vol. 1, no. 3, pp. 81-84, Sept. 2014 [[available online](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7036275)]
* Large-scale cluster management at Google with Borg. Abhishek Verma, Luis Pedrosa, Madhukar R. Korupolu, David Oppenheimer, Eric Tune, John Wilkes. Proceedings of the European Conference on Computer Systems (EuroSys), ACM, Bordeaux, France, 2015 [[available online](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43438.pdf)]
* Borg, Omega, and Kubernetes. Brendan Burns, Brian Grant, David Oppenheimer, Eric Brewer, John Wilkes. ACM Queue, vol. 14 (2016), pp. 70-93 [[available online](https://queue.acm.org/detail.cfm?id=2898444)]
* Demystifying Kubernetes: Overcoming Misconceptions About Container Orchestration. VMware. Sept. 2017 [[available online](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/products/pivotal/vmware-demystifying-kubernetes-overcoming-misconceptions-whitepaper.pdf)]
* Kubernetes: Up and Running, 2nd Edition. Brendan Burns, Joe Beda, Kelsey Hightower. O'Reilly Media, Inc., Oct. 2019, ISBN: 9781492046530 [[available online](https://tanzu.vmware.com/content/ebooks/kubernetes-up-running-dive-into-the-future-of-infrastructure)]

Selected Publications on Specific Relevant Topics:
* Serverless Computing: Cloud Programming Simplified: A Berkeley View on Serverless Computing. Eric Jonas, Johann Schleier-Smith, Vikram Sreekanti, Chia-Che Tsai, Anurag Khandelwal, Qifan Pu, Vaishaal Shankar, Joao Carreira, Karl Krauth, Neeraja Yadwadkar, Joseph Gonzalez, Raluca Popa, Ion Stoica, David Patterson. Technical Report No. UCB/EECS-2019-3, Feb. 2019 [[available online](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.pdf)]
* Reproducibility: The Role of Container Technology in Reproducible Computer Systems Research. Ivo Jimenez, Carlos Maltzahn, Adam Moody, Kathryn Mohror, Jay Lofstead, Remzi Arpaci-Dusseau, Andrea Arpaci-Dusseau. Proceedings of the 2015 IEEE International Conference on Cloud Engineering (IC2E 2015), pp. 379-385, Tempe, AZ, 2015 [[available online](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7092948)]
* Resource allocation: Quasar: resource-efficient and QoS-aware cluster management. Christina Delimitrou and Christos Kozyrakis. Proceedings of the 19th international conference on Architectural support for programming languages and operating systems (ASPLOS '14), pp. 127–144, Feb. 2014 [[available online](https://www.csl.cornell.edu/~delimitrou/papers/2014.asplos.quasar.pdf)]
* Resource allocation: Skynet: Performance-driven Resource Management for Dynamic Workloads. Yannis Sfakianakis, Manolis Marazakis, Angelos Bilas. Proceedings of the IEEE 14th International Conference on Cloud Computing (CLOUD 2021), pp. 527-539, 2021 [[available online](https://ieeexplore.ieee.org/document/9582274)]
* Resource Sizing in the Cloud: Ernest: Efficient Performance Prediction for Large-Scale Advanced Analytics. Shivaram Venkataraman, Zongheng Yang, Michael Franklin, Benjamin Recht, Ion Stoica. Proceedings of the 13th USENIX Symposium on Networked Systems Design and Implementation (NSDI 16), pp. 363-378, Santa Clara, CA, Mar. 2016 [[available online](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-venkataraman.pdf)]
* Chaos Engineering: Chaos Engineering. Ali Basiri, Niosha Behnam, Ruud de Rooij, Lorin Hochstein, Luke Kosewski, Justin Reynolds, Casey Rosenthal. IEEE Software, vol. 33, no. 3, pp. 35-41, May-June 2016 [[available online](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7436642)]

# Assignments

| Week | Short description |
|---|---|
| 1-2 | Assignment 1 (Basic Docker operations) [[available οnline](https://docs.google.com/document/d/1CYbA4eMDjy7WWEh5E5PY5DCMaEoVsfChLhlhG7RBE4o/edit?tab=t.0)] |
| 3-4 | Assignment 2 (Basic Kubernetes operations) [[available οnline](https://docs.google.com/document/d/1pZR0EYSEoTedwCQeQ2SEzHpBks7ZeYmZyI0DKHV-t68/edit?tab=t.0)] |
| 5-6 | Assignment 3 (Scaling applications in Kubernetes) |
| 7-8 | Assignment 4 (Kubernetes extensions) |
| 9-13 | Project. Titles will be decided in agreement with the instructor. Indicative subjects: Presentation and demo of some CNCF project, custom additions/extensions to Kubernetes, complete application implementation on Kubernetes with auto-scaling, use of Cloud APIs for automated application deployment, etc. |

# Marking scheme

|   |   |
|---|---|
| Participation | 15% |
| Assignments | 60% (4 * 15%) |
| Project | 25% |

A grade is required in all three categories (participation, assignments, and project).
