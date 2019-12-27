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

