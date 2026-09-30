"""Read-only Inhaltsregression. Benötigt Python 3 und Node.js, keine Zusatzpakete.

Aufruf im Vault: python -X utf8 "AP1/99 System/scripts/inhalte-pruefen.py"
Prüft Datenkonsistenz, Generatoren und ausgewählte unabhängige Referenzfälle.
Ersetzt keine fachliche Prüfung aller Freitextlösungen.
"""
from pathlib import Path
import json
import re
import sqlite3
import subprocess

ROOT = Path(__file__).resolve().parents[3]
JS = r'''
const fs = require('fs'), path = require('path');
function files(dir) { return fs.readdirSync(dir, {withFileTypes:true}).flatMap(x => x.isDirectory() ? files(path.join(dir,x.name)) : [path.join(dir,x.name)]); }
const result = {areas:[], reference:[], errors:[]};
function check(ok, message) { if (!ok) result.errors.push(message); }
for (const ap of ['AP1','AP2']) {
  const root = path.join(ap,'99 System');
  const k = new Function(fs.readFileSync(path.join(root,'scripts/ap1-kern.js'),'utf8'))();
  let seed=93026;
  k.setzeZufall(() => { seed=(Math.imul(seed,1664525)+1013904223)>>>0; return seed/4294967296; });
  let questions=0, cards=0, cases=0, fields=0;
  const ids=new Set();
  for (const p of files(path.join(root,'fragen')).filter(p=>p.endsWith('.js'))) {
    const qs = new Function('return ('+fs.readFileSync(p,'utf8')+'\n);')();
    for (const q of qs) {
      questions++;
      check(q.id && !ids.has(q.id), `${ap}: doppelte/fehlende ID ${q.id}`); ids.add(q.id);
      check(q.modul && q.frage && q.richtig!==undefined, `${ap}: unvollständige Frage ${q.id}`);
      if (q.typ==='mc') check(Number.isInteger(q.richtig) && q.richtig>=0 && q.richtig<q.optionen.length, `${ap}: MC-Schlüssel ${q.id}`);
      if (q.typ==='zahl') check(Number.isFinite(q.richtig), `${ap}: Zahlenlösung ${q.id}`);
    }
  }
  for (const p of files(path.join(root,'karten')).filter(p=>p.endsWith('.md'))) {
    const parsed=k.kartenParsen(fs.readFileSync(p,'utf8')); cards+=parsed.karten.length;
    check(parsed.warnungen.length===0, `${p}: Kartenparser ${JSON.stringify(parsed.warnungen)}`);
  }
  for (const [id,g] of Object.entries(k.generatoren)) for(let i=0;i<200;i++) {
    const task=g.erzeuge(); cases++;
    for(const field of task.felder) {
      fields++;
      const input=field.art==='zahl' ? String(field.loesung).replace('.',',') : String(field.loesung);
      check(k.pruefeFeld(field,input).ok, `${ap}/${id}: eigene Lösung abgewiesen ${input}`);
    }
    if(['usv-akku','subnetz-analyse','ipv6-kuerzen','ipv6-expandieren'].includes(id)) result.reference.push({ap,id,task});
  }
  for(let i=0;i<5000;i++) result.reference.push({ap,id:'sql-ergebnis',task:k.generatoren['sql-ergebnis'].erzeuge()});
  // Bewusst leere Ergebnismengen: sechs inaktive Kunden desselben Orts, Umsatz 200.
  for(const choice of [0.21,0.41,0.99]) {
    const values=[0,...Array.from({length:6},()=>[0,0,0.9]).flat(),0,0.99,choice]; let i=0;
    k.setzeZufall(()=>values[i++] ?? 0.99);
    const task=k.generatoren['sql-ergebnis'].erzeuge();
    check(task.felder[0].loesung==='NULL', `${ap}: leeres SQL-Aggregat ${task.code}`);
    check(k.pruefeFeld(task.felder[0],'NULL').ok && !k.pruefeFeld(task.felder[0],'0').ok, `${ap}: NULL-Antwortprüfung`);
    result.reference.push({ap,id:'sql-ergebnis',task});
  }
  const field={art:'ipv6',loesung:'2001:db8::/64'};
  for(const [answer,expected] of [['2001:0db8:0:0:0:0:0:0/64',true],['2001:db8::',false],['2001:db8::/63',false],['2001:db8::/64/7',false],['2001:db8::/129',false]]) check(k.pruefeFeld(field,answer).ok===expected, `${ap}: IPv6 ${answer}`);
  result.areas.push({ap,questions,cards,generators:Object.keys(k.generatoren).length,cases,fields});
}
console.log(JSON.stringify(result));
'''

def main():
    data = json.loads(subprocess.check_output(['node', '-e', JS], cwd=ROOT, encoding='utf-8'))
    errors = data['errors']
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE Kunde (KundenID INTEGER, Ort TEXT, Umsatz REAL, Aktiv INTEGER)')
    counts = {}
    for item in data['reference']:
        task, kind = item['task'], item['id']
        fields = task['felder']
        expected = None
        if kind == 'sql-ergebnis':
            db.execute('DELETE FROM Kunde')
            db.executemany('INSERT INTO Kunde VALUES (?,?,?,?)', task['tabelle'][1:])
            rows = db.execute(task['code']).fetchall()
            expected = len(rows) if 'GROUP BY' in task['code'] else rows[0][0]
            actual = fields[0]['loesung']
            ok = actual == 'NULL' if expected is None else isinstance(actual, (int,float)) and abs(actual-expected) <= 0.011
        elif kind == 'usv-akku':
            values = re.findall(r'\*\*([\d,.]+)(?: Ah| V| W)?\*\*', task['text'])
            q,u,eta,p = [float(x.replace('.','').replace(',','.')) for x in values]
            # Energiebilanz auf der Gleichstromseite, inklusive Umrichterverlusten.
            current = p / eta / u
            minutes = q / current * 60
            ok = abs(fields[0]['loesung']-minutes) <= 0.051 and abs(fields[1]['loesung']-current) <= 0.0051
        else:
            # Diese Generatoren werden oben auf Selbstkonsistenz geprüft.
            continue
        counts[kind] = counts.get(kind,0)+1
        if not ok:
            errors.append(f"{item['ap']}/{kind}: Referenzabweichung {task}")
    db.close()
    print(json.dumps({'areas':data['areas'], 'independent_checks':counts, 'errors':errors}, ensure_ascii=False, indent=2))
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(main())
