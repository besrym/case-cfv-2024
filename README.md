# case-cfv-2024
Praktische Arbeit (Sommersemester 2024) für das Modul Computer-Forensik und Vorfallsbehandlung


## Vorbereitende Schritte
Bevor Sie mit der Einrichtung eines eigenen Mailservers beginnen können, müssen Sie einige Voraussetzungen erfüllen:

1.) Sie müssen einen Host haben, den Sie verwalten können.
2.) Sie müssen eine Domäne besitzen, und Sie müssen in der Lage sein, DNS für diese Domäne zu verwalten.

##Einrichtung des Hosts
Es gibt einige Anforderungen an ein geeignetes Hostsystem:

1.) Der Host sollte eine statische IP-Adresse haben; andernfalls müssen Sie das DNS dynamisch aktualisieren (unerwünscht aufgrund des DNS-Cachings)
2.) Der Host sollte in der Lage sein, auf den notwendigen Ports für Mail zu senden/empfangen
3.) Sie sollten in der Lage sein, einen PTR-Eintrag für Ihren Host einzurichten; sicherheitsbewusste Mailserver könnten sonst Ihren Mailserver ablehnen, da die IP-Adresse Ihres Hosts nicht korrekt/überhaupt nicht in den DNS-Namen Ihres Servers aufgelöst werden kann.


## Overview of Email Ports

| Protocol | Explicit TLS | Implicit TLS | Purpose    | Enabled by Default |
|----------|--------------|--------------|------------|--------------------|
| ESMTP    | 25           | N/A          | Transfer   | Yes                |
| ESMTP    | 587          | 465          | Submission | Yes                |
| POP3     | 110          | 995          | Retrieval  | No                 |
| IMAP4    | 143          | 993          | Retrieval  | Yes                |

