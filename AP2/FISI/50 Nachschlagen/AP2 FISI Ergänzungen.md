---
tags: [ap2/nachschlagen, ap2/fisi]
---
# AP2 FISI – Ergänzungen aus dem Prüfungsabgleich

Kleine Themen, die in den FISI-Modulen bisher fehlten oder nur am Rand standen. Ausgangspunkt war ein Abgleich mit den FISI-AP2-Prüfungen 2021–2026 (GA1 „Konzeption und Administration“, GA2 „Analyse und Entwicklung von Netzwerken“). Der übrige Prüfungsstoff ist in den Modulen [[Übersicht FISI Konzeption und Administration]] und [[Übersicht FISI Netzwerke]] bereits abgedeckt.

> [!info] Hinweis zur Quelle
> Die Musterlösungen in der Community-Sammlung sind nicht offiziell von der IHK und enthalten vereinzelt Fehler. Nutze sie zum Üben, nicht als Wahrheit. Die Originalprüfungen sind urheberrechtlich geschützt und deshalb nicht im Vault.

## 1. Kupferkabel-Kategorien

| Kategorie | Frequenz | Typische Übertragung | Anmerkung |
|---|---|---|---|
| Cat 5e | 100 MHz | 1 Gbit/s | Mindeststandard im Büro |
| Cat 6 | 250 MHz | 1 Gbit/s, 10 Gbit/s nur auf kurzer Strecke (ca. 55 m) | |
| Cat 6a | 500 MHz | 10 Gbit/s bis 100 m | häufig für Neuverkabelung |
| Cat 7 | 600 MHz | 10 Gbit/s | durchgehend geschirmt (S/FTP) |
| Cat 8 | 2000 MHz | 25/40 Gbit/s, nur bis ca. 30 m | Rechenzentrum, kurze Verbindungen |

- Maximale Länge einer Kupferstrecke (Twisted Pair): **100 m** insgesamt, üblicherweise 90 m feste Verlegung (Permanent Link) plus 2 × 5 m Patchkabel.
- Kategorie = Eigenschaft des **Kabels und aller Komponenten** (Dosen, Patchfeld). Die schwächste Komponente bestimmt die Leistung.
- Schirmung (U/UTP, F/UTP, S/FTP) reduziert Störungen durch Nachbarkabel und Strom; Erdung des Schirms ist Pflicht.
- Vergleich mit Glasfaser (Reichweite, Störfestigkeit, Gebäudekopplung): [[FISI-11 Switching, VLAN und Verkabelung#Glasfaser oder Kupfer]].

## 2. Infrastructure as Code und Konfigurationsmanagement

**Idee:** Server und Netzwerkgeräte werden nicht von Hand konfiguriert, sondern über Textdateien (Code) beschrieben, versioniert und automatisch ausgerollt.

| Werkzeug | Zweck | Merkmale |
|---|---|---|
| **Ansible** | Konfiguration und Software-Rollout | **agentenlos** (SSH/WinRM), Playbooks in YAML, **idempotent** |
| **Puppet** | Konfigurationsmanagement | Agent auf jedem System, deklarativer Soll-Zustand |
| **Terraform** | Bereitstellung von Infrastruktur (VMs, Netze, Cloud) | deklarativ, beschreibt den Zielzustand |

- **Idempotent:** Wiederholtes Ausführen führt immer zum selben Ergebnis und ändert nichts, was schon passt.
- **Vorteile:** gleiche Konfiguration auf vielen Systemen, weniger Fehler, nachvollziehbare Änderungen (Versionsverwaltung), schneller Neuaufbau nach Ausfall, Dokumentation als Nebenprodukt.
- **Nachteile:** Einarbeitung, Fehler im Code wirken sich auf viele Systeme gleichzeitig aus, Zugangsdaten (Secrets) müssen geschützt werden.
- Passt zu: [[FISI-1 Server, Virtualisierung und Container]], [[FISI-7 Programmierung und Skripte für Admins]].

## 3. Monitoring-Werkzeuge

Aufgaben: Verfügbarkeit und Auslastung überwachen, bei Schwellenwerten alarmieren, Verläufe für Kapazitätsplanung sammeln.
- Bekannte Werkzeuge: **Zabbix**, **Nagios/Icinga**, **PRTG** (Windows), **Prometheus** mit Grafana (Metriken und Dashboards).
- Datenquellen: **SNMP** (Abfrage per Polling oder Meldung per **Trap**), Agenten auf den Systemen, **Syslog** für Logmeldungen, Ping/Port-Checks.
- Gute Konfiguration: sinnvolle Schwellenwerte (Warnung vor Kritisch), Benachrichtigung an die richtige Person, Abhängigkeiten (fällt der Switch aus, nicht jeden dahinterliegenden Server melden).
- Weiter: [[FISI-13 DNS, DHCP und Netzdienste]], [[FISI-16 Netzwerkanalyse, Fehlersuche und WAN]].

## 4. Honeypot

Ein **Honeypot** ist ein absichtlich ungeschütztes, aber isoliertes und stark überwachtes Lockvogel-System. Greift jemand darauf zu, ist das ein Hinweis auf einen Angriff oder ein bereits kompromittiertes Gerät, denn im normalen Betrieb hat dort niemand etwas zu suchen.
- **Zweck:** Angriffe früh erkennen, Vorgehen der Angreifer analysieren, Angreifer ablenken.
- **Abgrenzung:** IDS/IPS suchen Angriffe im echten Verkehr, ein Honeypot lockt sie an. Er schützt nicht selbst.
- **Risiko:** Wird der Honeypot übernommen und ist nicht sauber getrennt, dient er als Sprungbrett ins Netz (eigenes VLAN/DMZ, kein Zugriff aufs Produktivnetz).

## 5. SD-WAN

**Software-Defined WAN** verbindet Standorte über mehrere Leitungen (MPLS, DSL, Glasfaser, LTE/5G) und steuert den Verkehr zentral per Software.
- Ein **Controller** verteilt Richtlinien an die Router der Standorte.
- Anwendungsbezogene Wegewahl: kritischer Verkehr (VoIP, ERP) nimmt die beste Leitung, anderer Verkehr geht direkt ins Internet.
- Bei Ausfall oder schlechter Qualität eines Weges wird automatisch umgeschaltet.
- Verschlüsselte Tunnel (IPsec) zwischen den Standorten; günstigere Internetleitungen können MPLS teilweise ersetzen.
- Einordnung: [[FISI-16 Netzwerkanalyse, Fehlersuche und WAN]].

## 6. Typische Prüfungsrechnungen und -fragen (Kurzliste)

| Aufgabe | Weg |
|---|---|
| Netzteil dimensionieren | Leistungen aller Komponenten addieren, Reserve (z. B. 20 %) aufschlagen, durch Wirkungsgrad teilen, nächste marktübliche Größe wählen. Beispiel: 304 W · 1,2 ÷ 0,9 ≈ 405 W → 450 W |
| Verfügbarkeit in Ausfallstunden | 99,9 % von 8760 h/Jahr → 0,1 % = 8,76 h; mal Umsatz je Stunde = Schaden |
| Load-Balancing-Verfahren | Round Robin (reihum), Least Connections (wenigster aktive Verbindungen), IP-Hash (gleicher Client, gleicher Server) |
| FHRP (VRRP/HSRP) | virtuelle Gateway-IP/MAC; ein aktiver Router, Standby übernimmt. Clients tragen die **virtuelle** Adresse als Standard-Gateway ein |
| ARP-Poisoning im Mitschnitt | **Eine** IP-Adresse (meist das Gateway) gehört in ARP-Antworten zu **mehreren** MAC-Adressen |
| Port-Security | Configured MAC (fest eingetragen), Sticky MAC (gelernt und gemerkt), Violation Mode `shutdown` (Port aus), `restrict`, `protect` |
| DHCP-Mitschnitt auswerten | Option-Felder lesen: Router, DNS, Lease Time, Domain. Weicht `ipconfig /all` ab: statische Einstellung, alter Lease oder zweiter DHCP-Server prüfen, dann `ipconfig /release` und `/renew` |
| SPI vs. NGFW | SPI: Layer 3/4, Verbindungszustände. NGFW: zusätzlich Layer 7 (Anwendung, Benutzer, IPS, URL-/Malware-Filter) |

Die Grundlagen dazu stehen in den Modulen [[FISI-4 Datensicherung, Archivierung und Notfallvorsorge]], [[FISI-12 NAT, Firewall, DMZ und Proxy]] und [[FISI-14 WLAN und Netzzugangskontrolle]].

---
← [[AP2 FISI Start]]
