# atqc
atqc examples

For current files:
fibo.py
Run from concole like:
python fibo.py -n 10 -> will output the 10th number of Fibonacci sequence
python fibo.py --number 10 -> will do the same

pairs.py
Run from concole like:
python pairs.py -s 10 "[1,2,3,4,5]" -> will process list [1,2,3,4,5] and compair with sum = 10
python pairs.py "[1,2,3,4,5]" -> will use default sum = 10
python pairs.py -h(or --help) -> will show usage into console

Vagrant file full description:
Step by step in ubuntu:
1. sudo apt-get install virtualbox
2. sudo apt-get install vagrant
3. mkdir vagrantProjects
4. cd vagrantProjects && mkdir project1 && cd project1
5. vagrant box add ubuntu/trusty64
6. vagrant up
7. vagrant ssh
