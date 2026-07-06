---
created: 2026-02-12
last updated: 2026-02-15
publish: true
title: Dependency Injection
---

# Dependency Injection (DI)

Siehe: [[Objektorientierte Programmierung]]

Ein simples aber wichtiges [[Programmierung|Programmier]]-Pattern, bei dem Objekte oder Funktionen andere Objekte/Funktionen von außen bereitgestellt bekommen, anstatt sie intern selbst zu erzeugen:

```TypeScript
// OHNE Dependency Injection: Database wird intern erstellt
class Storage {
	private database: Database;
	
	constructor() {
		this.database = new Database('db.sqlite');
		
		//...
	}
}

// MIT Dependency Injection: Database wird in constructor übergeben
class Storage {
	private database: Database;
	
	constructor(database: Database) {
		this.database = database;
		
		//...
	}
}
```

Damit setzt es vor allem konkret das [[Dependency Inversion Principle]] um.

Es wird sichergestellt, dass “Clients”, die einen bestimmten “Service” nutzen möchten, nicht wissen müssen, wie dieser konstruiert wird.

Terminologie: (die vier “Rollen”, die bei DI involviert sind)

- **Services & Clients:** Ein Service ist eine Klasse mit nützlicher Funktionalität. Ein Client ist eine Klasse, die solche Services verwendet. Die Services, die ein Client verwendet sind dessen *dependencies*.
- **Interfaces:** Clients sollten nicht wissen, wie dessen dependencies implementiert sind, nur wie deren Schnittstelle aussieht.
- **Injectors:** Ein Injector (auch Assembler, Container, Provider, Factory) bereitet Services vor, die von Clients benutzt werden.

Analogie/Beispiel:

- Autos können als Services verstanden werden, welche die nützliche Funktionalität haben, Menschen von einem Ort zum nächsten zu transportieren
- Die Motoren der Autos benötigen etwa [[Diesel]] oder [[Elektrizität]], aber dieses Detail des Services ist für den Client (etwa ein Passagier) irrelevant.
- Autos haben ein uniformes Interface (Pedale, Lenkrad, etc.), sodass es am Ende irrelevant ist, welcher Motor genau in der Fabrik (Injector) eingebaut wurde.

---

- ↩
	- [Wikipedia](https://en.wikipedia.org/wiki/Dependency_injection)
	- [(CodeAesthetic, 2023) Dependency Injection](https://youtu.be/J1f5b4vcxCQ)