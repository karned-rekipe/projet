# contribution

**Une seule branche principale stable**, des branches de courte durée.

```  
main          ← toujours stable, toujours déployable  
├── feat/xxx  ← max 1-2 jours de vie  
├── fix/xxx  
└── chore/xxx  
```

---

## 🏷️ Convention de nommage des branches

```bash
feat/<ticket-id>-short-description    # nouvelle fonctionnalité
fix/<ticket-id>-short-description     # correction de bug
chore/<ticket-id>-short-description   # maintenance, refacto, deps
docs/<ticket-id>-short-description    # documentation
release/v1.2.0                        # branche de release (si besoin)
hotfix/v1.2.1-description             # fix critique en prod
```

---

