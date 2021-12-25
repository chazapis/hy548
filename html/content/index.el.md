---
title: "Σελίδα Μαθήματος"
date: 2021-12-24T18:15:26+02:00
---

Διδάσκων
: [Αντώνης Χαζάπης](http://users.ics.forth.gr/~chazapis/)

Περιοχή ειδίκευσης μεταπτυχιακών φοιτητών
: (Γ) Παράλληλα και Κατανεμημένα Συστήματα

Κατηγορία επιλογής προπτυχιακών φοιτητών
: (Ε5) Συστήματα Λογισμικού και Εφαρμογές

Διδακτικές Μονάδες
: 6 ECTS

Προαπαιτούμενα
: HY-335 (Δίκτυα Υπολογιστών), HY-345 (Λειτουργικά Συστήματα) ή άδεια του διδάσκοντα

Πρόγραμμα
: _Θα οριστεί_

Επικοινωνία:
: _Θα οριστεί_

# Περιγραφή Αντικειμένου

Το Διαδίκτυο παρέχει υπηρεσίες σε δισεκατομμύρια χρήστες ανά τον κόσμο. Ιστοσελίδες ενημέρωσης, δίκτυα κοινωνικής δικτύωσης, ηλεκτρονικά καταστήματα, κρατικές υπηρεσίες κτλ. πρέπει να είναι διαθέσιμα ανά πάσα στιγμή, ανεξάρτητα από τον φόρτο που δέχονται. Για αυτόν τον λόγο, οι σύγχρονες εφαρμογές κλίμακας Διαδικτύου αναπτύσσονται στο Cloud (Υπολογιστικό Νέφος). Οι εσωτερικές τους αρχιτεκτονικές έχουν εξελιχθεί σε πολύπλοκους ιστούς από "microservices" (μικρο-υπηρεσίες), που σε φυσικό επίπεδο είναι διασκορπισμένες ανά τον κόσμο, χρησιμοποιώντας εικονικούς πόρους και στοιχεία λογισμικού που προσφέρονται από τους παρόχους Cloud. Σε αυτό το μάθημα εξερευνούμε την οργάνωση υπηρεσιών Διαδικτύου μεγάλης κλίμακας και εστιάζουμε στις τεχνικές και τα εργαλεία που χρησιμοποιούνται για την κατασκευή και εκτέλεση εφαρμογών σε πλατφόρμες Cloud, συμπεριλαμβανομένων των containers και των συναρτήσεων "serverless". Μέσα από μια σειρά διαλέξεων με πρακτικό χαρακτήρα και σχετικών ασκήσεων οι φοιτητές καθοδηγούνται στην προχωρημένη χρήση και κατανόηση των εσωτερικών διαδικασιών του Kubernetes, που αποτελεί σήμερα το κοινά αποδεκτό πρότυπο για την αφηρημένη σύνθεση υπηρεσιών ανεξαρτήτως παρόχου. Επιπρόσθετα, επεκτεινόμαστε στο πως το Kubernetes εφαρμόζεται στην πράξη από τους μεγάλους παρόχους Cloud, όπως η Amazon και η Google, και πως οι εκτελούμενες αρχιτεκτονικές microservices που βασίζονται σε containers μπορούν να χρησιμοποιούν σχετικές υποστηρικτικές υπηρεσίες και APIs για να πετυχαίνουν αδιάλειπτη λειτουργία σε παγκόσμια κλίμακα.

# Μαθησιακοί Στόχοι

Σκοπός του μαθήματος είναι να παρέχει ουσιαστική κατανόηση για το πως δομείται, συντάσσεται και εκτελείται μια σύνθετη εφαρμογή κλίμακας Διαδικτύου στο Cloud, το οποίο περιλαμβάνει:
* Τη γνωριμία με τις ιδιαίτερες προδιαγραφές τόσο των εφαρμογών μεγάλης κλίμακας, όσο και του περιβάλλοντος του Cloud.
* Τεχνικές και εργαλεία για τη συγγραφή των εφαρμογών, τη διαχείριση των προαπαιτούμενων βιβλιοθηκών και την ενσωμάτωσή τους σε containers.
* Τον σχεδιασμό και την υλοποίηση αρχιτεκτονικών micro-services και την αξιοποίηση των προσφερόμενων υπηρεσιών Cloud, όπως οι συναρτήσεις serverless.
* Την προχωρημένη χρήση μιας σύγχρονης πλατφόρμας ενορχήστρωσης εφαρμογών για το Cloud, όπως το Kubernetes, μέσα από την κατανόηση της εσωτερικής του λειτουργίας.

# Ύλη Διαλέξεων

| Εβδομάδα | Σύντομη περιγραφή ύλης διδακτικής εβδομάδας |
|---|---|
| 1 | Εισαγωγή στις αρχιτεκτονικές λογισμικού για το Cloud (παραδείγματα εφαρμογών, υποδομές Cloud) |
| 2 | Περιβάλλοντα εκτέλεσης containers I (σύνθεση containers, εκτέλεση εφαρμογών, βασική χρήση του Docker) |
| 3 | Περιβάλλοντα εκτέλεσης containers II (μεταβλητές, αρχεία, δικτύωση, προχωρημένη χρήση του Docker) |
| 4 | Πλατφόρμες ενορχήστρωσης I (εισαγωγή στο Kubernetes, βασικά στοιχεία, βασικές εντολές) |
| 5 | Πλατφόρμες ενορχήστρωσης II (αφηρημένες έννοιες του Kubernetes, προχωρημένη χρήση) |
| 6 | Αυτόματη κλιμάκωση και serverless (χρήση του auto-scaler, συναρτήσεις ως υπηρεσία) |
| 7 | Δομικά στοιχεία της πλατφόρμας I (εσωτερική οργάνωση του Kubernetes, διεπαφές χρήσης και επέκτασης) |
| 8 | Δομικά στοιχεία της πλατφόρμας II (χρονοπρογραμματιστής, τελεστές) |
| 9 | Δομικά στοιχεία της πλατφόρμας III (CNI, CSI, διαδικτύωση μεταξύ εγκαταστάσεων, ενσωμάτωση του Edge) |
| 10 | Πλατφόρμες στο Cloud I (προσφερόμενες υπηρεσίες, διεπαφές χρήσης) |
| 11 | Πλατφόρμες στο Cloud II (παραδείγματα εφαρμογών) |
| 12 | Επισκόπηση αρχιτεκτονικών λογισμικού για το Cloud (αναφορές σε τρέχουσες και μελλοντικές εξελίξεις) |
| 13 | Παρουσιάσεις εργασιών |

# Προτεινόμενα Συγγράμματα

Δεν υπάρχουν υποχρεωτικά συγγράμματα. Το παρακάτω υλικό είναι σχετικό με την ύλη του μαθήματος και θα καλυφθεί στις διαλέξεις και τις ασκήσεις.

Υπηρεσίας κλίμακας Διαδικτύου:
* Architecture and design of high volume web sites: (a brief history of IBM sport and event web sites). Paul Dantzig. Proceedings of the 14th international conference on Software engineering and knowledge engineering (SEKE '02), July 2002, pp. 17-24 [[διαθέσιμο online](https://doi.org/10.1145/568760.568765)]
* Architecture and Dependability of Large-Scale Internet Services. David Oppenheimer and David Patterson. IEEE Internet Computing, vol. 6, no. 5, pp. 41-49, Sept.-Oct. 2002, [[διαθέσιμο online](http://roc.cs.berkeley.edu/papers/inet-computing.pdf)]
* On Designing and Deploying Internet-Scale Services. James Hamilton. Proceedings of the 21st Large Installation System Administration Conference (LISA '07), pp. 231-242, Dallas, TX, USENIX Association, Nov. 2007 [[διαθέσιμο online](https://www.usenix.org/legacy/event/lisa07/tech/full_papers/hamilton/hamilton_html/index.html)]
* Microservices: The Journey So Far and Challenges Ahead. Pooyan Jamshidi, Claus Pahl, Nabor C. Mendonça, James Lewis, Stefan Tilkov. IEEE Software, vol. 35, no. 3, pp. 24-35, May/June 2018 [[διαθέσιμο online](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8354433)]

Containers και Kubernetes:
* Containers and Cloud: From LXC to Docker to Kubernetes. David Bernstein. IEEE Cloud Computing, vol. 1, no. 3, pp. 81-84, Sept. 2014 [[διαθέσιμο online](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7036275)]
* Large-scale cluster management at Google with Borg. Abhishek Verma, Luis Pedrosa, Madhukar R. Korupolu, David Oppenheimer, Eric Tune, John Wilkes. Proceedings of the European Conference on Computer Systems (EuroSys), ACM, Bordeaux, France, 2015 [[διαθέσιμο online](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43438.pdf)]
* Borg, Omega, and Kubernetes. Brendan Burns, Brian Grant, David Oppenheimer, Eric Brewer, John Wilkes. ACM Queue, vol. 14 (2016), pp. 70-93 [[διαθέσιμο online](https://queue.acm.org/detail.cfm?id=2898444)]
* Demystifying Kubernetes: Overcoming Misconceptions About Container Orchestration. VMware. Sept. 2017 [[διαθέσιμο online](https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/products/pivotal/vmware-demystifying-kubernetes-overcoming-misconceptions-whitepaper.pdf)]
* Kubernetes: Up and Running, 2nd Edition. Brendan Burns, Joe Beda, Kelsey Hightower. O'Reilly Media, Inc., Oct. 2019, ISBN: 9781492046530 [[διαθέσιμο online](https://tanzu.vmware.com/content/ebooks/kubernetes-up-running-dive-into-the-future-of-infrastructure)]

Επιλεγμένες Εργασίες σε Συναφή Ειδικά Αντικείμενα:
* Serverless Computing: Cloud Programming Simplified: A Berkeley View on Serverless Computing. Eric Jonas, Johann Schleier-Smith, Vikram Sreekanti, Chia-Che Tsai, Anurag Khandelwal, Qifan Pu, Vaishaal Shankar, Joao Carreira, Karl Krauth, Neeraja Yadwadkar, Joseph Gonzalez, Raluca Popa, Ion Stoica, David Patterson. Technical Report No. UCB/EECS-2019-3, Feb. 2019 [[διαθέσιμο online](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2019/EECS-2019-3.pdf)]
* Reproducibility: The Role of Container Technology in Reproducible Computer Systems Research. Ivo Jimenez, Carlos Maltzahn, Adam Moody, Kathryn Mohror, Jay Lofstead, Remzi Arpaci-Dusseau, Andrea Arpaci-Dusseau. Proceedings of the 2015 IEEE International Conference on Cloud Engineering (IC2E 2015), pp. 379-385, Tempe, AZ, 2015 [[διαθέσιμο online](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7092948)]
* Resource allocation: Quasar: resource-efficient and QoS-aware cluster management. Christina Delimitrou and Christos Kozyrakis. Proceedings of the 19th international conference on Architectural support for programming languages and operating systems (ASPLOS '14), pp. 127–144, Feb. 2014 [[διαθέσιμο online](https://www.csl.cornell.edu/~delimitrou/papers/2014.asplos.quasar.pdf)]
* Resource Sizing in the Cloud: Ernest: Efficient Performance Prediction for Large-Scale Advanced Analytics. Shivaram Venkataraman, Zongheng Yang, Michael Franklin, Benjamin Recht, Ion Stoica. Proceedings of the 13th USENIX Symposium on Networked Systems Design and Implementation (NSDI 16), pp. 363-378, Santa Clara, CA, Mar. 2016 [[διαθέσιμο online](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-venkataraman.pdf)]
* Chaos Engineering: Chaos Engineering. Ali Basiri, Niosha Behnam, Ruud de Rooij, Lorin Hochstein, Luke Kosewski, Justin Reynolds, Casey Rosenthal. IEEE Software, vol. 33, no. 3, pp. 35-41, May-June 2016 [[διαθέσιμο online](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7436642)]

# Ασκήσεις

| Εβδομάδα | Σύντομη περιγραφή |
|---|---|
| 1-2 | Άσκηση 1 (Βασικές λειτουργίες του Docker) |
| 3-4 | Άσκηση 2 (Βασικές λειτουργίες του Kubernetes) |
| 5-6 | Άσκηση 3 (Κλιμάκωση εφαρμογών στο Kubernetes) |
| 7-8 | Άσκηση 4 (Επεκτάσεις του Kubernetes) |
| 9-13 | Εργασία. Τα θέματα θα αποφασιστούν σε συνεννόηση με τον διδάσκοντα. Ενδεικτικά: Προσαρμοσμένες προσθήκες/επεκτάσεις του Kubernetes, υλοποίηση ολοκληρωμένης εφαρμογής στο Kubernetes με αυτόματη κλιμάκωση, χρήση APIs του Cloud για αυτόματη εκτέλεση εφαρμογών, κτλ. |

# Τρόπος Αξιολόγησης

|   |   |
|---|---|
| Συμμετοχή | 15% |
| Ασκήσεις | 60% (4 * 15%) |
| Εργασία | 25% |
