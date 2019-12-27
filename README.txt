Esto es lo que hice para hacer el repositorio:

```
uriel@mash:~$ cd Projects/
uriel@mash:~/Projects$ mkdir play
uriel@mash:~/Projects$ cd play/
uriel@mash:~/Projects/play$ git init .
Initialised empty Git repository in /home/uriel/Projects/play/.git/
uriel@mash:~/Projects/play$ touch README.txt
```

y ahora estoy escribiendo el readme

voy a github.com 
creo un repositorio
despues de creado hay dos opciones@

"""
…or push an existing repository from the command line

git remote add origin git@github.com:urielarg/play.git
"""

corro ese comando, dentro del repo (ya lo hice con cd)


```
uriel@mash:~/Projects/play$ git remote add origin git@github.com:urielarg/play.git
uriel@mash:~/Projects/play$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	README.txt

nothing added to commit but untracked files present (use "git add" to track)
uriel@mash:~/Projects/play$ git add README.txt
uriel@mash:~/Projects/play$ git commit -av -m "First commit, readme"
[master (root-commit) 02f3d98] First commit, readme
 1 file changed, 26 insertions(+)
 create mode 100644 README.txt
uriel@mash:~/Projects/play$ git push origin master
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 542 bytes | 542.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To github.com:urielarg/play.git
 * [new branch]      master -> master
uriel@mash:~/Projects/play$
```

Ahora voy a crear un nuevo branch y poner en git lo que me pasaste por whatsapp:

```
uriel@mash:~/Projects/play$ git checkout -b branch_of_ian
Switched to a new branch 'branch_of_ian'
uriel@mash:~/Projects/play$ vim read_files.py
Error detected while processing function vundle#config#bundle[2]..<SNR>9_check_bundle_name:
line    2:
Vundle error: Name collision for Plugin scrooloose/nerdtree. Plugin scrooloose/nerdtree previously used the name "nerdtree". Skipping Plugin scrooloose/nerdtree.
Press ENTER or type command to continue
uriel@mash:~/Projects/play$ git commit -av -m "commiting in Ian's name what was sent by email"
On branch branch_of_ian
Untracked files:
	read_files.py

nothing added to commit but untracked files present
uriel@mash:~/Projects/play$ git add read_files.py
uriel@mash:~/Projects/play$ git status
On branch branch_of_ian
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   read_files.py

uriel@mash:~/Projects/play$ git commit -av -m "commiting in Ian's name what was sent by email"
[branch_of_ian d21861a] commiting in Ian's name what was sent by email
 1 file changed, 15 insertions(+)
 create mode 100644 read_files.py
uriel@mash:~/Projects/play$ git push origin branch_of_ian
Counting objects: 6, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.37 KiB | 1.37 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'branch_of_ian' on GitHub by visiting:
remote:      https://github.com/urielarg/play/pull/new/branch_of_ian
remote:
To github.com:urielarg/play.git
 * [new branch]      branch_of_ian -> branch_of_ian
```


Hice commit dos veces porque la primera vez me habia olvidado de hacer "add"
