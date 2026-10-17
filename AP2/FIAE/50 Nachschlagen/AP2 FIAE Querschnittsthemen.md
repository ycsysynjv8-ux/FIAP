---
tags: [ap2/nachschlagen, ap2/fiae]
---
# AP2 FIAE – Querschnittsthemen

Themen, die in keinem Fachmodul stehen, in den AP2-Prüfungen aber immer wieder als 3- bis 16-Punkte-Teilaufgabe auftauchen. Der **englische Fachtext** ist der wichtigste Kandidat: er kam in den letzten Prüfungen fast jedes Mal vor. Die übrigen Themen sind schnell gelernt und bringen sichere Punkte.

> [!info] Herkunft
> Abgeglichen mit dem Community-Projekt [fiae-ap2-pruefungstrainer](https://github.com/StrohhalmKatze/fiae-ap2-pruefungstrainer) (MIT-Lizenz, komplett KI-erstellt, daher ohne Gewähr). Die Texte hier sind neu formuliert. Rechtsangaben (AI Act, eRechnung) vor der Prüfung gegenprüfen.

| Thema | Typische Punkte | Wichtigste Fähigkeit |
|---|---|---|
| [[#1. Englischer Fachtext]] | 3–12 | Text gezielt auswerten, deutsch antworten, aufs Szenario übertragen |
| [[#2. Tabellenkalkulation]] | ca. 16 | `$`-Bezüge, WENN, SVERWEIS, WOCHENTAG, Grenzen von Tabellen |
| [[#3. Ticketsystem und IT-Service]] | ca. 12 | Vor-/Nachteile erläutern, Priorität und SLA bestimmen |
| [[#4. Künstliche Intelligenz]] | 4–8 | Begriffe, Trainings-/Testdaten, Bias, AI Act, Akzeptanz |
| [[#5. Green IT]] | ca. 4 | Begriff, Ziele, PUE rechnen, Maßnahmen |

---

## 1. Englischer Fachtext

**Aufgabe:** Mitten in einer Fachaufgabe steht ein englischer Text (½–1 Seite, oft mit Zwischenüberschriften). Die Fragen sind deutsch, du antwortest deutsch. Das Thema stammt aus dem Szenario (NoSQL, User Stories, Überdeckungsmaße, eRechnung, LoRa …).

**Vorgehen**
1. **Aufgabe zuerst lesen:** Operator (nennen / beschreiben / erläutern / begründen), Anzahl, „laut Text“ oder Szenariobezug?
2. **Überfliegen:** Überschriften und erste Sätze. Die Zwischenüberschriften sind oft schon dein Antwortgerüst.
3. **Gezielt lesen:** Fundstellen nummerieren, Signalwörter markieren.
4. **Deutsch antworten:** Aussage + Begründung (+ Bezug zum Projekt, falls verlangt).
5. **Kontrollieren:** Anzahl stimmt? Kein Argument doppelt?

> [!warning] Übersetzen ist nicht Erläutern
> „Fast queries“ nur mit „schnelle Abfragen“ zu übersetzen bringt höchstens ein Drittel der Punkte. Volle Punkte gibt es für **Aussage + Begründung aus dem Text**.

**Signalwörter**

| Englisch | Deutsch | Hinweis |
|---|---|---|
| whereas, while, in contrast to, unlike | wohingegen, im Gegensatz zu | Gegensatz: hier stehen Unterschiede und Nachteile |
| however, but, on the other hand | jedoch, aber, andererseits | Einschränkung |
| provided that, as long as, unless | vorausgesetzt, solange, es sei denn | **Bedingung / Voraussetzung** |
| therefore, thus, consequently | daher, folglich | Folge, Begründungskette |
| such as, e.g., for instance | zum Beispiel | Beispiel |
| at least / at most / up to | mindestens / höchstens / bis zu | Mengenangaben genau übernehmen |
| must / shall · should · may, can | muss · soll · darf, kann | Verbindlichkeit bei Normen und Anforderungen |

**Falsche Freunde:** *eventually* = schließlich (nicht eventuell) · *actual* = tatsächlich (nicht aktuell) · *to become* = werden (nicht bekommen) · *sensitive data* = vertrauliche Daten · *billion* = Milliarde · Zahlenformat: `1,000.50` ist 1000,5.

**Fachvokabular Englisch → Deutsch (Auswahl)**

| Englisch | Deutsch | Englisch | Deutsch |
|---|---|---|---|
| requirement | Anforderung | throughput | Durchsatz |
| deployment | Bereitstellung | latency | Antwortzeit |
| maintainability | Wartbarkeit | scalability | Skalierbarkeit |
| legacy system | Altsystem | dependency | Abhängigkeit |
| backward compatible | abwärtskompatibel | edge case | Grenzfall |
| statement / branch / path coverage | Anweisungs- / Zweig- / Pfadüberdeckung | regression test | Regressionstest |
| redundancy | Redundanz | consistency | Konsistenz |
| primary / foreign key | Primär- / Fremdschlüssel | transaction | Transaktion |
| bandwidth | Bandbreite | range | Reichweite |
| availability | Verfügbarkeit | on-premises | im eigenen Haus betrieben |
| authentication / authorization | Authentifizierung (wer?) / Autorisierung (was darf er?) | vulnerability | Schwachstelle |
| directive / regulation | Richtlinie (national umzusetzen) / Verordnung (gilt direkt) | personal data | personenbezogene Daten |
| stakeholder | Beteiligte(r) | scope | Projektumfang |
| acceptance criteria | Abnahmekriterien | backlog | priorisierte Aufgabenliste |
| lessons learned | gewonnene Erkenntnisse | bottleneck | Engpass |

**Typische Fehler:** den ganzen Text übersetzen (kostet Zeit) · Sätze abschreiben · Bedingungen überlesen (`provided that`, `unless`) · Informationen ergänzen, obwohl „laut Text“ gefragt ist · denselben Vorteil zweimal nennen.

---

## 2. Tabellenkalkulation

**Grundlagen:** Arbeitsmappe → Arbeitsblätter → Zellen (`B3`) → Bereiche (`B3:D8`). Formeln beginnen mit `=`. Deutsch: Semikolon als Trenner, Dezimalkomma; englisch: Komma und Dezimalpunkt. Maßgeblich ist die Schreibweise im **Belegsatz** der Prüfung. Bezug auf ein anderes Blatt: `Blattname!Zelle`. **Datumswerte sind Zahlen** (Tage seit 1900): `Datum + 1` = Folgetag, `Datum − Datum` = Abstand in Tagen.

**Zellbezüge beim Kopieren**

| Schreibweise | Art | Verhalten |
|---|---|---|
| `B2` | relativ | wandert mit (Normalfall) |
| `$B$2` | absolut | bleibt fest (Parameter wie Steuersatz, Nachschlagematrix) |
| `$B2` | Spalte fest | Zeile wandert |
| `B$2` | Zeile fest | Spalte wandert |

Merkfrage bei jedem Bezug: *Soll er beim Kopieren mitwandern?* Nein → `$` davor.

**Wichtige Funktionen (deutsch / englisch)**

| Funktion | Wirkung |
|---|---|
| `SUMME`, `MITTELWERT`, `MIN`, `MAX` / `SUM`, `AVERAGE` | Grundrechenarten über Bereiche |
| `ZÄHLENWENN` / `COUNTIF` | zählt Zellen mit Kriterium: `=ZÄHLENWENN(B2:B40;"Jugend")` |
| `SUMMEWENN` / `SUMIF` | `(Kriterienbereich; Kriterium; Summenbereich)` |
| `RUNDEN` / `ROUND` | `=RUNDEN(A2;2)` |
| `WENN`, `UND`, `ODER` / `IF`, `AND`, `OR` | Logik, auch verschachtelt |
| `SVERWEIS` / `VLOOKUP`, `XVERWEIS` / `XLOOKUP` | Nachschlagen in Tabellen |
| `HEUTE`, `JAHR`, `MONAT`, `TAG`, `DATUM` / `TODAY`, `YEAR` … | Datumsrechnung |
| `WOCHENTAG` / `WEEKDAY` | Wochentag als Zahl, Typ beachten |

**WENN verschachtelt (Notenschlüssel, höchste Schwelle zuerst):**
`=WENN(B2>=92;1;WENN(B2>=81;2;WENN(B2>=67;3;WENN(B2>=50;4;WENN(B2>=30;5;6)))))`. Jede öffnende Klammer braucht eine schließende.

**SVERWEIS:** `SVERWEIS(Suchkriterium; Matrix; Spaltenindex; Bereich_Verweis)`. Der Spaltenindex zählt ab der **ersten Spalte der Matrix**. Die Matrix steht meist **absolut** (`$A$2:$B$5`).
- `FALSCH` (0): genau suchen, sonst `#NV`. Richtig für Schlüssel (Artikelnummer, Mitgliedsart).
- `WAHR` (oder weggelassen): ungefähr suchen in **aufsteigend sortierter** erster Spalte, liefert die Zeile mit dem größten Wert ≤ Suchkriterium. Richtig für Staffeln (Versandkosten, Rabatt).
- **Falle:** Wer das vierte Argument vergisst, bekommt bei unsortierten Schlüsseln keinen Fehler, sondern einen **falschen Wert**.

**WOCHENTAG:** Typ 1 (Excel-Standard): Sonntag = 1. Typ 2: Montag = 1 … Sonntag = 7, in Deutschland am praktischsten (`WOCHENTAG(A2;2)<=5` = Montag bis Freitag). Der Belegsatz kann abweichen (je nach Vorgabe gilt teils standardmäßig 1 = Montag) – **Typ immer ausdrücklich angeben**.

**Fehlerwerte:** `#NV` nicht gefunden · `#WERT!` falscher Datentyp · `#DIV/0!` · `#BEZUG!` Bezug gelöscht · `#NAME?` Funktionsname falsch.

**Grenzen von Tabellenkalkulation** (typische Frage „Problem beim Einsatz“):

| Tabellenkalkulation | Anwendung mit Datenbank |
|---|---|
| Mehrbenutzerbetrieb eingeschränkt, Konflikte | viele Nutzer gleichzeitig, Transaktionen (ACID) |
| jede Zelle frei editierbar, keine Datentypen/Fremdschlüssel | Datentypen, Pflichtfelder, Integrität |
| Rechte nur auf Dateiebene, kein Änderungsprotokoll | Rollen und Rechte, Protokollierung |
| Logik in Zellen verteilt, schwer testbar | Logik zentral im Code, versioniert, getestet |
| viele Kopien („final_neu2.xlsx“), personenbezogene Daten per Mail | zentrale Datenhaltung, Datenschutz steuerbar |

Gut geeignet für: Kalkulationen, Was-wäre-wenn-Rechnungen, Auswertungen mit Diagrammen, kleine Listen einer Person, Prototyp einer Berechnungslogik.

---

## 3. Ticketsystem und IT-Service

Ein **Ticketsystem** (Helpdesk, Service Desk, Issue-Tracker) erfasst jede Anfrage als Ticket mit eindeutiger Nummer und verfolgt sie bis zur Erledigung. Eingangskanäle: E-Mail, Webformular/Portal, Telefon, Chat, Feedback-Knopf in der App.

**Inhalt eines Tickets:** Nummer · Melder · Zeitstempel · Kanal · Kategorie/betroffener Dienst · Beschreibung (Fehlerbild, Schritte, Version) · Auswirkung und Dringlichkeit → Priorität · Status · Bearbeiter/Gruppe · Verlauf · Lösung.

**ITIL-Begriffe**

| Begriff | Bedeutung |
|---|---|
| Service Desk / SPOC | zentrale Anlaufstelle für alle Anfragen |
| Incident (Störung) | ungeplante Unterbrechung; Ziel: schnell wiederherstellen, notfalls per **Workaround** |
| Service Request | Standardanfrage ohne Störung (Zugang, Passwort-Reset) |
| Problem | (unbekannte) **Ursache** mehrerer Incidents; Ziel: dauerhaft beseitigen |
| Change | geplante, genehmigte und dokumentierte Änderung |
| SLA / OLA | Vereinbarung über Servicezeit, Reaktions- und Lösungszeit, Verfügbarkeit (OLA = intern zwischen Teams) |

**Ticket-Status:** Neu → Zugewiesen → In Bearbeitung ⇄ Wartend (SLA-Uhr ruht) → Gelöst → Geschlossen (Wiedereröffnung möglich). *Gelöst* heißt: Lösung eingetragen. *Geschlossen* erst nach Bestätigung des Melders oder Fristablauf. Eignet sich als Vorlage für ein UML-**Zustandsdiagramm**.

**Priorität = Auswirkung × Dringlichkeit** (1 = höchste):

| Dringlichkeit ↓ / Auswirkung → | hoch | mittel | gering |
|---|---|---|---|
| hoch | 1 kritisch | 2 hoch | 3 mittel |
| mittel | 2 hoch | 3 mittel | 4 niedrig |
| gering | 3 mittel | 4 niedrig | 5 Planung |

Begründe immer mit **beiden** Größen: Wer/was ist betroffen (Impact)? Wie schnell entsteht Schaden, gibt es einen Workaround (Urgency)?

**SLA prüfen:** Priorität bestimmen → Fristen ablesen → Dauer berechnen (nur innerhalb der Servicezeit) → vergleichen. Reaktionszeit = bis zur ersten *qualifizierten* Rückmeldung (eine automatische Eingangsbestätigung zählt nicht).
**Verfügbarkeit:** 99,5 % bei 720 h/Monat → erlaubter Ausfall 0,5 % · 720 h = 3,6 h; 99,9 % → 43,2 min.

**Support-Level:** Level 0 Self-Service (FAQ, Portal) → 1st Level Service Desk (erfassen, einstufen, Standardlösungen) → 2nd Level Fachspezialisten → 3rd Level Entwicklung/Hersteller (Bugfix, Patch).
- **Funktionale (horizontale) Eskalation:** weiter an die Stufe mit mehr Fachwissen.
- **Hierarchische (vertikale) Eskalation:** Vorgesetzte einschalten, wenn eine SLA-Frist reißt oder Entscheidungen/Ressourcen fehlen.

**Kennzahlen:** Erstlösungsquote = beim ersten Kontakt gelöste ÷ alle Tickets · 100 · SLA-Erfüllungsquote · mittlere Lösungszeit (MTTR) · Backlog · Wiedereröffnungsquote · Kundenzufriedenheit. Beispiel: 248 von 400 Tickets sofort gelöst → 62 %.

**Vor- und Nachteile** (typisch „drei Vorteile und einen Nachteil erläutern“, je 3 Punkte):

| Vorteile | Nachteile / Risiken |
|---|---|
| nichts geht verloren (zentrale Erfassung) | Kosten für Lizenz, Einführung, Betrieb |
| Transparenz über den Status, weniger Nachfragen | Pflegeaufwand und Schulung |
| Priorisierung und Zuweisung nach festen Regeln | wirkt formal, Nutzer umgehen es („kurz anrufen“) |
| Vertretung möglich, Wissen nicht nur im Kopf einer Person | Fehleinstufung verzögert die Lösung |
| Kennzahlen, SLA-Überwachung | Datenschutz: personenbezogene Daten in Tickets |
| Wissensaufbau, Probleme fallen auf | Abhängigkeit vom System |

> [!warning] Typische Fehler
> „Erläutern“ verlangt zu jedem Punkt eine Begründung. „Löst Probleme schneller“ ist zu pauschal: das System schafft Überblick und Priorisierung, lösen müssen weiterhin Menschen. Transparenz und Statusabfrage im Portal sind **derselbe** Vorteil.

---

## 4. Künstliche Intelligenz

**Begriffe:** KI (Oberbegriff) ⊃ Machine Learning (lernt Muster aus Beispieldaten statt festen Regeln) ⊃ Deep Learning (tiefe neuronale Netze). Generative KI / **LLM** erzeugt Text, Bild, Code; Eingabe = **Prompt**.
- Klassisch programmiert der Mensch die Regeln, beim ML ermittelt der Lernalgorithmus sie aus Daten mit richtigen Antworten (**Labels**). Ergebnis: ein **Modell**.
- **Training:** Modell wird angepasst (rechenintensiv). **Inferenz:** fertiges Modell wird auf neue Daten angewendet.
- **Konfidenz:** Wahrscheinlichkeitsangabe des Modells, keine Garantie.

| Lernverfahren | Daten | Ziel | Beispiel |
|---|---|---|---|
| überwachtes Lernen | mit Labels | Klassifikation, Regression | Abfall per Kamera sortieren, Strombedarf vorhersagen |
| unüberwachtes Lernen | ohne Labels | Clustering, Anomalieerkennung | Kundengruppen bilden |
| bestärkendes Lernen | Belohnung/Strafe | Strategie lernen | Roboterarm lernt Greifen |

**Daten aufteilen:** z. B. 70 % Training, 15 % Validierung, 15 % Test. **Testdaten dürfen im Training nicht vorkommen**, sonst misst man nur Auswendiglernen (**Overfitting**). Die Daten müssen den späteren Einsatz abbilden (Kameras, Licht, Jahreszeiten, Varianten).

**Ergebnis bewerten (Beispiel 1 000 Flaschen, 50 defekt; 40 erkannt, 10 übersehen, 19 Fehlalarme, 931 richtig OK):**
- Genauigkeit (Accuracy) = (40 + 931) ÷ 1 000 = **97,1 %** (Anteil korrekter Vorhersagen insgesamt)
- Trefferquote (Recall) = 40 ÷ 50 = **80 %** (Anteil erkannter Defekte an allen tatsächlich defekten Flaschen)
- Präzision (Precision) = 40 ÷ (40 + 19) ≈ **67,8 %** (Anteil echter Defekte an allen gemeldeten Alarmen)
- Falle: Ein Modell, das immer „in Ordnung“ meldet, hätte 95 % Genauigkeit und fände keinen einzigen Defekt. Bei seltenen, wichtigen Fällen zählt, wie viele übersehen werden.

**Bias** (systematische Verzerrung) entsteht meist durch die Daten: nicht repräsentativ, unausgewogene Klassen, historische Vorurteile, uneinheitliche Labels, veraltete Daten (Data Drift). Gegenmaßnahmen: vielfältige Daten, klare Label-Richtlinien, Ergebnisse je Gruppe prüfen, im Betrieb überwachen und nachtrainieren.

**Halluzination:** Sprachmodell erzeugt plausible, aber falsche Aussagen, weil es wahrscheinliche Wortfolgen berechnet und keine Fakten prüft. Maßnahmen: Antworten auf geprüfte Dokumente stützen (**RAG**), Quellen anzeigen, Themenbereich begrenzen, Mensch einbinden, Nutzer hinweisen.
**Erklärbarkeit:** neuronale Netze sind eine Blackbox. Wichtig für Vertrauen, Fehlersuche, Haftung und DSGVO Art. 22 (keine rein automatisierte Entscheidung mit erheblicher Wirkung ohne Mensch).

**Datenschutz:** Enthalten Trainings-/Eingabedaten Personenbezug, gilt die DSGVO (Zweckbindung, Datenminimierung, Löschpflichten). Maßnahmen: anonymisieren/pseudonymisieren, Auftragsverarbeitungsvertrag, keine Kundendaten in öffentliche KI-Chats. Kamera-/KI-Auswertungen eignen sich zur Leistungskontrolle → **Mitbestimmungsrecht des Betriebsrats** (§ 87 Abs. 1 Nr. 6 BetrVG).

**EU AI Act** (Verordnung (EU) 2024/1689, gilt als Verordnung direkt in allen Mitgliedstaaten). Risikobasiert, Pflichten gestaffelt in Kraft (Verbote und KI-Kompetenz seit Feb. 2025, Allzweck-KI/GPAI seit Aug. 2025, allgemeine Geltung inkl. Hochrisiko-KI nach Anhang III und Transparenzpflichten ab Aug. 2026):

| Stufe | Beispiele | Folge |
|---|---|---|
| unannehmbar | Social Scoring, manipulative Techniken | **verboten** |
| hoch | Bewerberauswahl, Prüfungsbewertung, Kreditwürdigkeit, kritische Infrastruktur | erlaubt mit strengen Pflichten (Risikomanagement, Datenqualität, Dokumentation, menschliche Aufsicht) |
| begrenzt | Chatbots, Deepfakes | **Transparenzpflicht** (Kennzeichnung) |
| minimal | Spamfilter, Rechtschreibprüfung | keine besonderen Pflichten |

Einordnen in fünf Schritten: Einsatzzweck und Betroffene → verbotene Praxis? → Hochrisiko-Bereich? → Interaktion/Inhalte erzeugt (Transparenz)? → sonst minimal. Immer die **Folge** nennen.

**KI-Assistenten beim Programmieren**

| Chancen | Risiken |
|---|---|
| Routinecode, Tests, Dokumentation, Code erklären | plausibel aussehender, aber fehlerhafter/unsicherer Code (z. B. SQL-Injection) |
| Refactoring-Hinweise, schnelle Prototypen | erfundene Methoden oder Pakete |
| Lernhilfe für neue Sprachen | Abfluss von Quellcode, Zugangsdaten, Kundendaten |
| | Lizenz-/Urheberrecht, Abhängigkeit, Code, den niemand versteht |

Regeln: Verantwortung bleibt beim Entwickler, erzeugter Code durchläuft Review und Tests, Firmenlizenz mit Datenschutzvertrag, keine Geheimnisse in Prompts.

**Akzeptanz bei Mitarbeitenden** (Workshop-Ziele, vgl. Change-Management in [[FIAE-1 Projektmanagement in der Softwareentwicklung]]): Befürchtungen sind Arbeitsplatzverlust, Überwachung, Kontrollverlust („Maschine entscheidet“), Haftung für KI-Fehler. Maßnahmen: früh und ehrlich informieren (Ziel, Nutzen, was sich ändert), Betroffene beteiligen (Pilotgruppe), schulen, Mensch behält die Entscheidung, Betriebsrat und Datenschutz einbinden, schrittweise einführen. Im Workshop außerdem Befürworter, Gegner und Unentschlossene erkennen.

---

## 5. Green IT

**Green IT** = Informations- und Kommunikationstechnik über den gesamten **Lebenszyklus** (Herstellung, Betrieb, Entsorgung) umwelt- und ressourcenschonend gestalten und IT einsetzen, um anderswo Energie und Ressourcen zu sparen.

**Ziele:** Energieverbrauch senken · CO₂-Emissionen verringern · Rohstoffe schonen · Lebensdauer verlängern, Elektroschrott vermeiden · Recycling · Betriebskosten senken · gesetzliche Vorgaben/Nachhaltigkeitsberichte erfüllen.

| Green **in** IT | Green **by** IT |
|---|---|
| IT selbst wird umweltfreundlicher | IT spart in anderen Bereichen |
| effiziente Netzteile, optimierte Kühlung, Geräte ausschalten, sparsamer Code, Ökostrom | Routenoptimierung, intelligente Heizungssteuerung, digitale Akten, Smart Grid, Homeoffice |

**Rechenzentrum:** Virtualisierung und Konsolidierung (viele Server sind nur 10–15 % ausgelastet), bessere Kühlung (Kalt-/Warmgang-Einhausung, freie Kühlung, Abwärme nutzen), effiziente USV/Netzteile, Ökostrom, Monitoring.

**PUE** (Power Usage Effectiveness) = Gesamtenergie des Rechenzentrums ÷ Energie der IT-Geräte. Beispiel: 72 kW gesamt ÷ 40 kW IT = **1,8**, also 0,8 kWh Zusatzaufwand je kWh Nutzen. Je näher an 1, desto effizienter.

---

← [[AP2 FIAE Start]] · Fachmodule: [[Übersicht FIAE Planen eines Softwareproduktes]] · [[Übersicht FIAE Algorithmen]]
