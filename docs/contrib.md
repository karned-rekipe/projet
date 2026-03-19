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

## 📋 PR Workflow

```
1. Crée une branche feat/xxx depuis main
2. Commits atomiques (Conventional Commits)
3. Ouvre une PR → CI doit être vert
4. Code review (au moins 1 approbation)
5. Rebase + Squash merge sur main
6. Suppression automatique de la branche après merge
```

### Conventional Commits

```
feat: add ingredient search endpoint
fix: correct pagination offset calculation
chore: bump kcrud to v1.3.0
docs: update README installation steps
```

---