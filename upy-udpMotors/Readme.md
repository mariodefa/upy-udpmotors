# Run tests
start docker  
create the container for testing  
```Shell
docker build -t tmotrs .
```
Run container and enter the container bash  
```Shell
python3 -m unittest discover -s tests -v
```