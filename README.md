# Terraform

En soit tout peut-être fait depuis le fichier main.tf, j'ai fait 4 fichiers pour mieux gérer les variables et les outputs que mon fichier me fait, en plus des options pour azure.

## Commandes utilisées.

Avec ce commit, depuis le dossier ./TP4/ on peut simplement executer les commandes:

```
terraform init

terraform apply

ssh -i id_rsa devops@[ip_a_copier_coller_depuis_terraform_apply] cat /etc/os-release
```

l'ip n'est pas dans les variables d'env par défaut (je n'ai pas réussi a le faire depuis les fichiers tf) donc il faut la récuperer depuis les outputs de `terraform apply`.

## Problèmes encontrés

le principal problème était (pour une raison) le fichier generé "id_rsa" était mal encodé (j'ai du destroy, et spécifier que je devais le génerer en ascii) 
avant de destroy puis re apply.

depuis je n'ai pas eu ce problème.

sinon la création de la vm était assez rapide, plus simple que les fichiers .yaml, tout se passe dans le terminal au lieu de en ligne sur github.


