---
tags: [ap2/nachschlagen, ap2/fisi]
---
# AP2 FISI – Ergänzungen aus dem Prüfungsabgleich

Kleine Themen, die in den FISI-Modulen bisher fehlten oder nur am Rand standen. Ausgangspunkt war ein Abgleich mit den FISI-AP2-Prüfungen (Prüfungsbereiche „Konzeption und Administration von IT-Systemen“ und „Analyse und Entwicklung von Netzwerken“). Der übrige Prüfungsstoff ist in den Modulen [[Übersicht FISI Konzeption und Administration]] und [[Übersicht FISI Netzwerke]] bereits abgedeckt.

> [!info] Hinweis zur Quelle
> Die Musterlösungen in der Community-Sammlung sind nicht offiziell von der IHK und enthalten vereinzelt Fehler. Nutze sie zum Üben, nicht als Wahrheit. Die Originalprüfungen sind urheberrechtlich geschützt und deshalb nicht im Vault.

## 1. Kupferkabel-Kategorien

| Kategorie | Frequenz | Typische Übertragung | Anmerkung |
|---|---|---|---|
| Cat 5e | 100 MHz | 1 Gbit/s | Mindeststandard im Büro |
| Cat 6 | 250 MHz | 1 Gbit/s, 10 Gbit/s nur auf kurzer Strecke (ca. 55 m) | |
| Cat 6A | 500 MHz | 10 Gbit/s bis 100 m | häufig für Neuverkabelung |
| Cat 7 | 600 MHz | 10 Gbit/s | durchgehend geschirmt (S/FTP) |
| Cat 8 | 2 000 MHz | 25/40 Gbit/s, nur bis ca. 30 m | Rechenzentrum, kurze Verbindungen |

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
| Netzteil dimensionieren & Netzaufnahme | **Nennleistung (Ausgang):** Leistungen aller Komponenten addieren, Reserve (z. B. 20 %) aufschlagen, nächste marktübliche Größe wählen (z. B. 304 W · 1,2 = 364,8 W → **400 W**). **Netzaufnahme (Eingang für Stromkosten/USV):** Last durch Wirkungsgrad teilen ($P_{\text{zu}} = P_{\text{ab}} \div \eta$, z. B. 304 W ÷ 0,9 ≈ **337,8 W**) |
| Verfügbarkeit in Ausfallstunden | 99,9 % von 8 760 h/Jahr → 0,1 % = 8,76 h; mal Umsatz je Stunde = Schaden |
| Load-Balancing-Verfahren | Round Robin (reihum), Least Connections (wenigste aktive Verbindungen), IP-Hash (gleicher Client, gleicher Server) |
| FHRP (VRRP/HSRP) | virtuelle Gateway-IP/MAC; ein aktiver Router, Standby übernimmt. Clients tragen die **virtuelle** Adresse als Standard-Gateway ein |
| ARP-Poisoning im Mitschnitt | **Eine** IP-Adresse (meist das Gateway) gehört in ARP-Antworten zu **mehreren** MAC-Adressen |
| Port-Security | Configured MAC (fest eingetragen), Sticky MAC (gelernt und gemerkt), Violation Mode `shutdown` (Port aus), `restrict`, `protect` |
| DHCP-Mitschnitt auswerten | Option-Felder lesen: Router, DNS, Lease Time, Domain. Weicht `ipconfig /all` ab: statische Einstellung, alter Lease oder zweiter DHCP-Server prüfen, dann `ipconfig /release` und `/renew` |
| SPI vs. NGFW | SPI: Layer 3/4, Verbindungszustände. NGFW: zusätzlich Layer 7 (Anwendung, Benutzer, IPS, URL-/Malware-Filter) |

Die Grundlagen dazu stehen in den Modulen [[FISI-4 Datensicherung, Archivierung und Notfallvorsorge]], [[FISI-12 NAT, Firewall, DMZ und Proxy]] und [[FISI-14 WLAN und Netzzugangskontrolle]].

## 7. Frame- und Header-Aufbau (Ethernet, 802.1Q, IPv4/IPv6)

In Netzwerkteilen wird regelmäßig ein **Ethernet-Frame** oder **IP-Header** mit Lücken gezeigt:

| Ethernet-II-Feld | Größe | Inhalt / Prüfungsdetail |
|---|---|---|
| Präambel + SFD | 7 + 1 Byte | Synchronisation (`10101010…`, SFD `10101011`), zählt **nicht** zur Framegröße |
| **Ziel-MAC** | 6 Byte | Empfänger (`FF:FF:FF:FF:FF:FF` = Broadcast) |
| **Quell-MAC** | 6 Byte | Absender (Schnittstelle des sendenden Geräts bzw. letzten Routers) |
| **802.1Q-VLAN-Tag** *(optional)* | **4 Byte** | **TPID** `0x8100` (2 Byte) + **TCI** (2 Byte: **PCP** 3 Bit für QoS, **DEI** 1 Bit, **VLAN-ID** **12 Bit** → 0–4095, nutzbar **1–4094**) |
| **EtherType** | 2 Byte | Protokoll der Schicht 3, z. B. `0x0800` IPv4, `0x86DD` IPv6, `0x0806` ARP |
| **Nutzdaten (Payload)** | 46–1 500 Byte | IP-Paket (MTU 1 500 Byte; bei Jumbo Frames bis ca. 9 000 Byte) |
| **FCS (CRC)** | 4 Byte | Prüfsumme zur Fehlererkennung auf Schicht 2 (fehlerhafte Frames werden verworfen) |

- **Framegröße:** 64 bis 1 518 Byte ohne VLAN-Tag, mit 802.1Q-Tag bis **1 522 Byte**.
- **IPv4- vs. IPv6-Header im Vergleich:**
  - **IPv4-Header:** **20–60 Byte** (variabel durch Optionen), 12+ Felder, enthält u. a. **TTL** (Time to Live), **Protocol** (z. B. 6 = TCP, 17 = UDP, 1 = ICMP), **Header-Checksumme**, Fragmentierungsfelder (`DF`, `MF`, Offset) sowie Quell- und Ziel-IP (je 32 Bit).
  - **IPv6-Header:** **fest 40 Byte** (schlanker, schnelleres Routing), nur 8 Felder: Version (4 Bit = 6), Traffic Class (8 Bit, QoS), Flow Label (20 Bit), Payload Length (16 Bit), **Next Header** (ersetzt *Protocol* und verweist auf Erweiterungsheader oder TCP/UDP/ICMPv6), **Hop Limit** (ersetzt *TTL*), Quell- und Zieladresse (je 128 Bit). **Keine Header-Checksumme** (macht Schicht 2/4) und **keine Fragmentierung durch Router** (nur durch den Sender per Path MTU Discovery).

## 8. Ereignisgesteuerte Prozesskette (EPK)

Neben BPMN und UML-Aktivitätsdiagrammen taucht in Prüfungen gelegentlich eine **EPK** zur Darstellung von Geschäftsprozessen auf:

| Element | Symbol | Bedeutung und Regel |
|---|---|---|
| **Ereignis** | Sechseck | **passiver** eingetretener Zustand (z. B. „Störungsmeldung eingegangen“, „Ticket geschlossen“). Start und Ende einer EPK sind **immer** Ereignisse |
| **Funktion** | abgerundetes Rechteck | **aktive** Tätigkeit / Entscheidung (z. B. „Störung prüfen“, „Hardware tauschen“) |
| **Konnektoren** | Kreis mit $\wedge$ (`AND`), $\vee$ (`OR`), `XOR` | Verzweigung und Zusammenführung des Kontrollflusses |
| **Organisationseinheit / Informationsobjekt** | Ellipse mit senkrechtem Strich / Rechteck | Wer führt die Funktion aus (z. B. „1st-Level-Support“) bzw. welche Daten werden gelesen/geschrieben |

- **Grundregel 1 (Strenger Wechsel):** Auf ein **Ereignis** folgt immer eine **Funktion**, auf eine **Funktion** wieder ein **Ereignis** (ggf. über Konnektoren).
- **Grundregel 2 (Keine Entscheidung nach Ereignis):** Da ein Ereignis nur ein passiver Zustand ist, trifft es **keine Entscheidung** – nach einem Ereignis darf **kein `XOR`- oder `OR`-Split** stehen (nur ein `AND`-Split für parallele Funktionen). Entscheidungen (`XOR`/`OR`) folgen immer auf eine **Funktion**.

---
← [[AP2 FISI Start]]

