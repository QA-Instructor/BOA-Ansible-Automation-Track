# Bank of America - Automate Everything - Automation Developer Track

## Course Outline
### Day 1 - Introduction to Python
* What is Python?
* Python core syntax
* Lab PY00
* Lab PY01
* Flow Control and error handling
* Lab PY02
* Functions and Modules
* Lab PY03
* Working with files
* Lab PY04

### Day 2 - Working with APIs
* Overview of APIs and architecture
* The Python requests library
* Lab PY05
* Strategies for API Error Handling
* Lab PY06
* Async Programming
* Lab PY07
* Lab PY08

### Day 3 - Introduction to Terraform and Ansible
* Why IaC?
* Terraform key concepts
* Lab TF01
* Terraform modules and outputs
* Lab TF02
* Introduction to Configuration Management and Ansible
* Lab ANS01
* Ansible Playbooks and Inventories
* Lab ANS02

### Day 4 - Advanced Ansible and Secrets Management
* Ansible variables, facts, handlers and roles
* Lab ANS03
* Performance Management for Ansible Playbooks
* Lab ANS04
* Secrets Management Strategies for Ansible
* Lab ANS05
* Inroduction to AWX
* Lab ANS06

### Day 5
* Introduction to software testing
* TDD and CI/CD
* Key testing tools for Python
* Lab PY09
* Lab PY10
* Ansible Module Development and Testing
* Lab PY11

## Labs 
## PY00
### Lab PY00 - Setting up the Development Environment

#### Objective
The goal of this lab is to set up a Python development environment under WSL, accessible via VS Code

#### Outcomes
By the end of this lab, you will have:
* Configured VS Code with extensions
* Connected VS Code to a WSL environment
* Installed the necessary Python tooling within a WSL environment

#### High-Level Steps
* Configure VS Code
* Connect to WSL
* Install Python tooling (pip and venv)

#### Detailed Steps
##### Configure VS Code
1. [Install VS Code](https://code.visualstudio.com/download). VSCode is a popular, flexible multi-language IDE which provides an extensive ecosystem of _extensions_ for enabling wider integrations
2. Launch VS Code and open the extensions tab from the VS Code side menu  
3. Search for and install the 'WSL' extension. Wait for it to install, then close and relaunch VS Code to ensure the extension is activated

##### Connect to WSL
4. In the bottom left of the VS Code window, click the 'open a remote window' icon, and from the menu that appears choose 'connect to WSL'. If prompted, select the remote platform as 'Linux'. A new VS Code window will load, connected to your WSL environment on the classroom machine
5. In this new window, click the extensions icon in the side menu again. This time, search for 'Python' - install the Python extension from Microsoft. Make sure when installing to select 'install in remote: WSL'.
6. Once the extension is installed, click the file explorer icon in the menu, and click 'open folder'. Open your home directory (/home/qa). VS Code will reload the window and open your home directory in the file explorer. 
7. Copy the provided lab files into a new directory in your home directory called 'Labs'

##### Install Python Tooling (pip and venv)
8. Open a new integrated terminal in VS Code, by pressing ctrl+'. This will open a terminal with the working directory set to whatever your current open directory in VS Code is - in this case /home/qa, which will probably be represented in your prompt by a '~' (tilde)
9. This WSL environment is running Ubuntu, a common distribution of Linux. Python should already be installed. Verify this by executing the following command in your terminal:
```bash
python3 --version
```
10. You will also need two additional pieces of Python tooling installed. Specifically, you will be using the Python package manager, pip, and the (v)irtual (env)ironment - or _venv_ module. Install these (note: the _sudo_ password in these environments is simply qa):
```bash
sudo apt-get update
sudo apt-get install python3-pip python3-venv
```
11. Verify the installation:
```bash
pip3 --version
python3 -m venv --help
```

## PY01
### Lab PY01 - Python Introduction

#### Objective
Create and run your first Python script

#### Outcomes
By the end of this lab, you will have:
* Written a python script to perform basic I/O and string manipulation
* Executed the script

#### High-Level Steps
- Setup a new virtual environment
- Create and run a Python script

#### Detailed Steps
##### Set up a python environment
1. In the integrated terminal in VS Code, change directory into the PY01 directory: 
```shell
cd ~/Labs/PY01 
```
2. Expand this directory in the VS Code file explorer. The directory contains a single, empty file: **main.py**. 
3. You could start working on this file immediately, however it is good to utilise best practices from the beginning, so you will first create a _virtual environment_:
```shell
python3 -m venv venv 
source venv/bin/activate 
```
Observe that your prompt now begins (venv), indicating that the virtual environment is active. The purpose of the virtual environment is to allow you to install any dependencies with a limited scope - unlike tools like, say, NPM, pip implicitly installs packages globally unless a venv is used. This would be problematic if you required different versions of the same package across different projects.

4. Using the VS Code explorer, open the **main.py** file, and enter the following contents:  
```python
#! /home/qa/Labs/PY01/venv/bin/python3
if __name__ == '__main__':
    print("Hello World!")
```
##### Basic Script - Breakdown
Broadly speaking, this script has three components: 
```python     
#! /home/qa/Labs/PY01/venv/bin/python3 
```
This is known as a 'shebang'. This is used to allow the script to be invoked as if it were any other executable file on linux systems - the shebang is ignored on Windows, and by the python interpreter itself. In this instance, you have used the venv instance of python3, to ensure that any active venv configuration is respected. 
```python
if __name__ == '__main__': 
```
As with the use of venv, this is overkill in the context of this simple exercise. However, it is a matter of best practice, so you will include it here. 
```python
print("Hello World!") 
```
This is the actual logic of the script - for now, a simple print statement. You will expand on this soon.

5. Run the script to verify that all is working as intended: 
```shell
./main.py 
```
You should see "Hello World!" printed in the terminal  

NOTE: If you receive a Permission denied message, add the execute permission to the file using **chmod**

```shel
chmod +x main.py
```
NOTE: Thanks to the Python extension, VS Code will detect that the file is a python file and allow you to run the script via the IDE, using the 'play button' icon. For this exercise this will not affect the outcome, but in later labs it may cause problems as it will not autodetect the venv. Invoking the script via the shell will always work.

##### Work with some fundamental data types
6. You will now make your script do something slightly more complex, in order to demonstrate some ways of interacting with common data types. Modify the body of your **main.py** script to do the following: 
- ask a user to input a first name and a last name, and assign these values to two string variables 
- print the provided name in the format LASTNAME, Firstname 
- print whether the last name ends with '-son' 
- sum the total number of vowels in both names and print the result 
- print the square of the difference between the lengths of the first and last name
```python
#! venv/bin/python3

if __name__ == '__main__':
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    print(f"{last_name.upper()}, {first_name.capitalize()}")
    print(last_name.lower().endswith('son'))
    full_name = first_name.lower() + " " + last_name.lower()
    total_vowels = full_name.count('a') + full_name.count('e') + full_name.count('i') + full_name.count('o') + full_name.count('u')
    print(total_vowels)
    print((len(first_name) - len(last_name)) ** 2)
``` 
```shell
./main.py
```

##### Using CLI Help
7. In reality, when implementing scripts, it is unlikely that someone has given you a document like this with all the code snippets you need. As such, you will need to be able to solve problems and investigate the usage of functions and modules for yourself.
8. In the integrated terminal, run `python3 -i` to start an interactive Python interpreter session.
9. Start by reviewing the documentation for the `print` function you used in the script above:
```python
help(print)
```
NOTE: press 'q' to quit the current help screen when 'END' is shown or '*space*' to page to the next screen when a colon ':' is displayed


10. Next, review the documentation for one of the string methods used above:
```python
help(str.lower)
```
11. Note that instead of a single function, you can also review the documentation of an entire class or module:
```python
help(str)
```
12. End the interactive session using the exit function:
```python
exit()
```

#### Optional Stretch Tasks
- modify the script to take the firstname and lastname as a single string, of the format "firstname,lastname", and extract the two variables from this string (hint: see the help for the string.split method)

## PY02
### Lab PY02 - Flow Control and Error Handling

#### Objective
Create a simple terminal-based number game in python, with error handling for common issues

#### Outcomes
By the end of this lab, you will have:
* Implemented flow control, iteration and error handling
* Experienced iterative development

#### High-Level Steps
- Setup a new project with venv
- Script the core game logic
- Implement error handling on user input
- Implement replays

#### Detailed Steps
##### Setup the Project
1. Ensure you have an active VS Code session connected to WSL - refer back to Lab PY00 if you do not, and cannot remember the steps

2. From the integrated terminal within VS Code, change into the PY02 directory: 
```shell     
cd ~/Labs/PY02
```
Expand this directory in the VS Code file explorer.

3. Setup a new virtual environment for the project:
```shell     
python3 -m venv venv     
source venv/bin/activate
```
Open the **main.py** file, which contains a basic placeholder script: 
```python
#! venv/bin/python3
if __name__ == '__main__':
    print("TODO: Implement me")
```

##### Implement a simple game loop
4. For this exercise, you will aim to build a simple guessing game using the control flow constructs you have examined. The game logic itself is reasonably simple: 
- a random number is chosen 
- the player inputs integers (positive or negative) which will be summed together. The aim is to have this sum hit the target number
- The player has 10 inputs to hit the target 

Start by implementing this fundamental game loop:
```python
#! venv/bin/python3
from random import randint

if __name__ == '__main__':
    total = 0
    target = randint(0, 100) # a random number is chosen
    print("Objective: enter up to 10 numbers which sum to a randomly chosen target value")
    for move in range(0, 10): # 10 moves to hit the target
        uinp = input("Enter a number: ") # user enters a number
        inp = int(uinp)
        total += inp # inputs are summed together
        if total == target: # the aim is to hit the target
            print(f"Target hit! Moves taken: {move + 1}")
            break # stop the game if the user has 'won'
        print(f"Current total: {total} is {'greater' if total > target else 'lower'} than target")
```
5. Run the script, and play the game
```bash
./main.py
# play the game by entering inputs
``` 
Does it behave as expected?

##### Implement error handling
6. This simple game loop is a good starting point, but has possible failure points. Consider for example the cast to an integer. If the provided input cannot be parsed as an integer a ValueError exception will be thrown. This could crash the program. 

7. Add some error handling for this case using _try ... except ..._
```python
#! venv/bin/python3
from random import randint

if __name__ == '__main__':
    total = 0
    target = randint(0, 100) 
    print("Objective: enter up to 10 numbers which sum to a randomly chosen target value")
    for move in range(0, 10): 
        uinp = input("Enter a number: ") 
        try: # add this line
            inp = int(uinp) # indent this and next line
            total += inp 
        except ValueError: # add this and next two lines
            print(f"{uinp} is not a valid integer")
            continue
        if total == target: 
            print(f"Target hit! Moves taken: {move + 1}")
            break 
        print(f"Current total: {total} is {'greater' if total > target else 'lower'} than target")
```
8. Run the script again, and try entering non-numeric inputs. They should be gracefully handled without crashing the program

##### Implement the ability to play multiple rounds
Currently, you can play one round of this game at a time before the script exits. You will now implement the ability to continue playing. 

9. Wrap the existing game logic in an infinite while loop, and give the player a choice to continue playing at the end of each iteration:
```python
#! venv/bin/python3
from random import randint

if __name__ == '__main__':
    while True: # <- add this line, indent following lines
        total = 0
        target = randint(0, 100) 
        print("Objective: enter up to 10 numbers which sum to a randomly chosen target value")
        for move in range(0, 10): 
            uinp = input("Enter a number: ") 
            try:
                inp = int(uinp) 
                total += inp 
            except ValueError: 
                print(f"{uinp} is not a valid integer")
                continue
            if total == target: 
                print(f"Target hit! Moves taken: {move + 1}")
                break 
            print(f"Current total: {total} is {'greater' if total > target else 'lower'} than target")
        if input("Play again(y/n): ").lower() == "n": # add this line
            break # and this one
```

## PY03
### Lab PY03 - Functions and Modules

#### Objective
Implement a vat calculator function, which can be imported into, and used by, another script.

#### Outcomes
By the end of this lab, you will have:
* Created a python function
* Used type-hinting and docstrings to document the function
* Imported the function into another script

#### High-Level Steps
- Setup a new virtual environment
- Create a new Python file which defines a vat calculator function
- Document the function
- Make the function part of a module and import it into another script

#### Detailed Steps
##### Set up a python environment
1. From the integrated terminal, change into the PY03 directory and set up a project venv:
```shell
    cd ~/Labs/PY03
    python3 -m venv venv
    source venv/bin/activate
``` 
2. Expand this new directory in VS Code explorer and open the **calculator.py** file.

##### Create a function
3. Add the following contents to **calculator.py**:
```python
#! venv/bin/python3

def calculate_total(subtotal, rate=20):
    vat = (rate / 100) * subtotal
    return subtotal + vat

if __name__ == '__main__':
    print(calculate_total(100, 20))
```
4. Execute the script:
```shell
./calculator.py
```
The output should be 120.0

##### Review the help information for the function
5. Add a call to the **help()** function within the main block passing the name of your function as the argument:

```python
#! venv/bin/python3

def calculate_total(subtotal, rate=20):
    vat = (rate / 100) * subtotal
    return subtotal + vat

if __name__ == '__main__':
    print(calculate_total(100, 20))
    help(calculate_total) # add this line
```

You will see the function signature displayed as you have not yet added any documentation to your function.

##### Document your function
6. Now you will edit your function to be properly documented. Make the following changes to the **calculator.py** file:
```python
#! venv/bin/python3

def calculate_total(subtotal: float, rate: float = 20) -> float: # add the type hints on this line, and the following multi-line string
    '''
    calculate total amount, given subtotal and vat rate
    vat rate should be provided as a percentage
    >>> calculate_total(100, 20)
    120.0
    >>> calculate_total(10, 50)
    15.0
    '''
    vat = (rate / 100) * subtotal
    return subtotal + vat

if __name__ == '__main__':
    print(calculate_total(100, 20))
    # comment the below line
    # help(calculate_total) 
```
7. Run the script again. The behaviour should not have changed. The content that was added is purely documentational.

8. Uncomment the last line of code and re-run the script:

```python
if __name__ == '__main__':
    print(calculate_total(100, 20))
    # uncomment the below line
    help(calculate_total) 
```
You will see your help documentation displayed in the terminal. Press 'q' to quit.

Re-comment the last line of code:
```python
if __name__ == '__main__':
    print(calculate_total(100, 20))
    # comment the below line
    # help(calculate_total) 
```

9. Notice that VS Code has automatically detected the documentation you added by hovering over the name of the **calculate_total** function.

##### Creating a custom module
10. You will now make your new function available as part of a module. Create a new directory called **vat_calculator**:
```shell
mkdir vat_calculator
```
11. Move the calculator.py file into this directory, and also create an **\_\_init\_\_.py** file:
```shell
mv calculator.py vat_calculator
touch vat_calculator/__init__.py
```
12. Create a new file in the current directory, **main.py**, and add the following contents:
```python
#! venv/bin/python3
from vat_calculator.calculator import calculate_total

if __name__ == '__main__':
    print(calculate_total(100, 20))
```
13. Make this script executable and run it:
```shell
chmod +x main.py
./main.py
```

#### Optional Stretch Tasks
- Add a docstring to the \_\_init\_\_.py file explaining the purpose of the module, and use the pydoc utility to generate html-formatted documentation for your module

## PY04
### Lab PY04 - Working With Files

#### Objective
Create a script which uses all the concepts introduced so far to perform validations against a particular type of configuration file

#### Outcomes
By the end of this lab, you will have:
* Implemented file I/O in a python script
* Used libraries to parse common data formats
* Implemented real-world useful automation via python

#### High-Level Steps
- Setup the virtual environment (venv)
- Parse a YAML file into a python object
- Use flow control concepts to implement validation for the YAML file
- Write validation results as a JSON file

#### Detailed Steps
##### Set up the python project
1. From the integrated terminal within VS Code, switch into the PY04 directory and set up the project venv: 
```shell     
cd ~/Labs/PY04
python3 -m venv venv
source venv/bin/activate
```
2. Open this directory in the VS Code explorer and open the **main.py** file:
```python 
#! venv/bin/python3
if __name__ == '__main__':
    print("TODO: Implement me")
```

##### Install PyYAML and parse a yaml file
For this exercise, you will build a script to validate Kubernetes Pod manifests against certain criteria, and save the validation results as a JSON file. To do this, you will need to be able to parse YAML files.
1. Begin by installing the PyYAML library:
```shell
venv/bin/python3 -m pip install pyyaml
```
2. In **main.py**, implement the ability to parse a YAML file:
```python
#! venv/bin/python3
import yaml

if __name__ == '__main__':
    with open('pod.yml', 'r') as podfile:
        pod = yaml.safe_load(podfile)
        print(pod)
```
3. Save the file and run your python script:
```shell
./main.py
```
Observe the output. Note the structure of the dictionary object into which the YAML has been parsed.

##### Implement validation logic
4. In **main.py**, define a function called **validate_pod** which has 3 parameters **pod, prefix** and **port_range** that validates the following criteria: 
- the image used by each container begins with a given **prefix** 
- any container ports lie within a given range: **port_range**

Call this function with the following arguments:

- the **pod** dictionary object as the first argument
- "my-registry.example.io/" as the **prefix**
- (5000, 10000) as the **port_range**

<details>
<summary>Show PY04 Solution</summary>

```python
#! venv/bin/python3
import yaml

def validate_pod(pod, prefix, port_range):
    valid = True
    for container in pod["spec"]["containers"]: # could be more than one container per pod
        if not container.get("image", "").startswith(prefix): # validate that the image has a given registry prefix
            valid = False
        for port in container.get("ports", dict()): # could be multiple, or no, ports defined
            if not (port_range[0] <= port.get("containerPort", 0) <= port_range[1]): # validate that the containerPort is within the defined range
                valid = False
    return valid

if __name__ == '__main__':
    with open('pod.yml', 'r') as podfile:
        pod = yaml.safe_load(podfile)
        validation = validate_pod(pod, prefix="my-registry.example.io/", port_range=(5000, 10000)) # call the function
        print(validation)
```
</details>

5. Run your script. The validation should return as *False*.

##### Generate JSON results file
6. You are now able to validate the criteria you wish to check against but currently you have no way of knowing which criteria are, and are not, passing the checks. You will now edit your script to produce a results file, in JSON format, detailing which validations have passed and which have failed. 

7. Edit your **main.py** file:
- add an import for json
- create a dictionary with a key of "validation results" and an empty list as the value
-  within your code, append dictionary items to this list detailing the status (passed /failed) and the reason why
- write the contents of the validation results to a file

<details>
<summary>Show PY04 Part 2 Solution</summary>

```python
#! venv/bin/python3
import yaml
import json # add this import

def validate_pod(pod, prefix, port_range):
    valid = True
    results = {"validation results": []} # create dict to hold results
    with open("status_report.json", 'w') as outfile: # open json file
        for container in pod["spec"]["containers"]:
            if not container.get("image", "").startswith(prefix):
                valid = False
                results['validation results'].append({f'{container.get("name")} image validation': {'status': 'failed', 'reason': f'image {container.get("image")} not from expected registry: {prefix}'}}) # add the validation result and reason to outputs
            else:
                results['validation results'].append({f'{container.get("name")} image validation': {'status': 'passed', 'reason': f'image {container.get("image")} from expected registry: {prefix}'}})
            for port in container.get("ports", dict()):
                if not (port_range[0] <= port.get("containerPort", 0) <= port_range[1]):
                    valid = False
                    results['validation results'].append({f'{container.get("name")} port validation': {'status': 'failed', 'reason': f'port {port.get("containerPort")} not in range {port_range[0]} - {port_range[1]}'}})
                else:
                    results['validation results'].append({f'{container.get("name")} port validation': {'status': 'passed', 'reason': f'port {port.get("containerPort")} in required range {port_range[0]} - {port_range[1]}'}})
        json.dump(results, outfile, indent=2) # write out the results
        return valid
```

</details>
<br>

8. You should also update the main block so that the output directs the user as to where to find detailed results:

<details>
<summary>Show PY04 Part 3 Solution</summary>

```python
if __name__ == '__main__':
    with open('pod.yml', 'r') as podfile:
        pod = yaml.safe_load(podfile)
        validation = validate_pod(pod, prefix="my-registry.example.io/", port_range=(5000, 10000))
        if validation:
            print("all validations passed")
        else:
            print("validation failed - see status_report.json for details")
```
</details>

#### Optional Stretch Tasks
- Amend the script to read the filename, registry prefix and port range from the command-line, instead of hard-coding (HINT: the built-in _argparse_ library may be useful)
- Amend the script to also populate a global CSV file with the path to each validated file, its validation status and number of failed validations (HINT: support for reading/writing CSV files is available via the built-in _csv_ library)
- Amend the script to check whether the input yaml file defines a Pod or a Deployment. If it's a deployment, modify the logic of the script to pass just the pod part of the spec to validate_pod

## PY05
### Lab PY05 - Interacting With APIs
#### Objective
Deploy a provided REST API, and create a python script to make authenticated requests to it

#### Outcomes
By the end of this lab, you will have:
* Deployed a Python Web API using *Flask*
* Used the *requests* library to make GET, POST, PUT and DELETE requests
* Utilised Bearer token and Digest authentication to interact with secure endpoints

#### High-Level Steps
- Install dependencies and deploy the API
- Create a script which can make HTTP GET requests to the API
- Implement client-side authentication to enable POST, PUT & DELETE requests

#### Detailed Steps
##### Launch the example API
1. On your classroom machine, ensure that _docker desktop_ is started.
2. Edit the docker desktop settings and check 'enable WSL integration' (NOTE: this should already be enabled: Settings -> Resources -> WSL Integration -> Enable Integration with my default WSL distro)
3. Ensure you have an active VS Code environment connected to WSL and navigate to the lab directory:
```bash
cd ~/Labs/PY05
```
4. Deploy the sample API using docker compose:
```bash
sudo docker compose -f compose.yml up -d --build
```

##### Make HTTP get requests
5. Open the **api_requests.py** file, and add the following content:
```python
#! venv/bin/python3
import requests

if __name__ == '__main__':
    books = requests.get('http://localhost:5000/api/books')
    print(books.json())
```
6. In the VS Code terminal, install requests in a new virtual environment and run your script:
```shell
python3 -m venv venv
source ./venv/bin/activate
venv/bin/pip3 install requests
chmod +x ./api_requests.py
./api_requests.py
```
7. Observe the response from the API - an empty list ([]), as there are currently no books

##### Make a POST request
8. In your **api_requests.py** script, add a POST request to create a new book object:
```python
#! venv/bin/python3
import requests

if __name__ == '__main__':
    book = {"id": "0000012345", "title": "Lorem Ipsum", "genre": "fantasy", "blurb": "Lorem ipsum, dolor sic amet..."} # add this line
    requests.post('http://localhost:5000/api/books', json=book) # and this line
    books = requests.get('http://localhost:5000/api/books')
    print(books.json())
```
9. Run your script again. Notice there are still no books even after the POST request. Amend your script to provide some debug information:
```python
#! venv/bin/python3
import requests

if __name__ == '__main__':
    book = {"id": "0000012345", "title": "Lorem Ipsum", "genre": "fantasy", "blurb": "Lorem ipsum, dolor sic amet..."}
    p = requests.post('http://localhost:5000/api/books', json=book) # edit this line
    print(p.status_code, p.text) # add this line
    books = requests.get('http://localhost:5000/api/books')
    print(books.json())
```
You will see **401 Unauthorized** outputted.

10. This API requires authentication for any action other than a GET. The example API uses two forms of authentication: 
- bearer token authentication for POST/PUT/DELETE actions 
- Digest authentication for the generation of bearer tokens themselves 
11. First, you will amend your script to generate a bearer token you can then use for subsequent requests:
```python
#! venv/bin/python3
import requests
from requests.auth import HTTPDigestAuth # add this import

if __name__ == '__main__':
    auth = HTTPDigestAuth('learner', 'p@ssword') # provide username and password
    token = requests.post('http://localhost:5000/auth/tokens', auth=auth) # make a request to get a token
    print(token.text) # display token value

    book = {"id": "0000012345", "title": "Lorem Ipsum", "genre": "fantasy", "blurb": "Lorem ipsum, dolor sic amet..."}
    p = requests.post('http://localhost:5000/api/books', json=book)
    print(p.status_code, p.text)

    books = requests.get('http://localhost:5000/api/books')
    print(books.json())
```
12. Run the script. You should see a random token value returned by the API server. Now that you are able to generate tokens, you can use token authentication to make a POST request:
```python
#! venv/bin/python3
import requests
from requests.auth import HTTPDigestAuth

if __name__ == '__main__':
    auth = HTTPDigestAuth('learner', 'p@ssword') 
    token = requests.post('http://localhost:5000/auth/tokens', auth=auth) 
    t_auth_headers = {"Authorization": f"Bearer {token.text}"} # create request header with the new token
    book = {"id": "0000012345", "title": "Lorem Ipsum", "genre": "fantasy", "blurb": "Lorem ipsum, dolor sic amet..."}
    requests.post('http://localhost:5000/api/books', json=book, headers=t_auth_headers) # make post request with token header
    books = requests.get('http://localhost:5000/api/books')
    print(books.json())
```
13. The auth flow in this script is as follows:
- The client (i.e. the script) makes an initially unauthenticated POST request to /tokens
- The server returns a response indicating that authentication is required, and provides some server-side generated cryptographic variables
- The client uses the HTTPDigestAuth library to compute a shared secret from the given password and returned cryptographic variables. The server independently computes the same secret
- The client makes a now-authenticated POST request to /tokens, resulting in a token being created and returned
- This token is then subsequently used to authenticate future requests, via HTTP Bearer token authentication
14. Running the script again should show the book now created.

##### Make PUT and DELETE requests
Now that you have a book object to work with, you should try using some other request methods

15. First, edit your script to use a PUT request to update the existing book object:
```python
#! venv/bin/python3
import requests
from requests.auth import HTTPDigestAuth

if __name__ == '__main__':
    auth = HTTPDigestAuth('learner', 'p@ssword')
    token = requests.post('http://localhost:5000/auth/tokens', auth=auth)
    t_auth_headers = {"Authorization": f"Bearer {token.text}"}
    book = {"id": "0000012345", "title": "Lorem Ipsum", "genre": "fantasy", "blurb": "A gripping high-fantasy with sci-fi/thriller elements"} # <- edit this line
    requests.put('http://localhost:5000/api/books', json=book, headers=t_auth_headers) # <- change 'post' to 'put'
    books = requests.get('http://localhost:5000/api/books')
    print(books.json())
```
16. Run the script: `./api_requests.py`. Note the updated blurb for the returned book object.
17. Now you will DELETE the book:
```python
#! venv/bin/python3
import requests
from requests.auth import HTTPDigestAuth

if __name__ == '__main__':
    auth = HTTPDigestAuth('learner', 'p@ssword')
    token = requests.post('http://localhost:5000/auth/tokens', auth=auth)
    t_auth_headers = {"Authorization": f"Bearer {token.text}"}
    book = {"id": "0000012345"} # the only data needed to delete a book is the id
    requests.delete('http://localhost:5000/api/books', json=book, headers=t_auth_headers) # change 'put' to 'delete'
    books = requests.get('http://localhost:5000/api/books')
    print(books.json())
```
18. Re-run the script again and confirm the deletion of the book

#### Stretch Tasks
- Using your knowledge of file I/O, create JSON files for book, author and review objects. There is no defined schema for these objects in this API, so these can be any valid JSON. Amend your script to parse these files and post their contents to the API
- Modify your script further to allow the user to specify a file or files to read as the source for the JSON to post

## PY06
### Lab PY06 - Implementing Retry Logic

#### Objective
Create a script which is able to implement retries for failed API requests

#### Outcomes
By the end of this lab, you will have:
* Implemented *exponential backoff* with a time-out to handle API availability errors

#### High-Level Steps
- Implement a request to a deliberately unreliable endpoint with basic error handling
- Improve the implementation to use an exponential backoff approach

#### Detailed Steps
##### Ensure the example API is Running
1. Ensure that the sample API server is running (it may still be running from the previous lab):
```bash
sudo docker ps | grep sample-flask-app || sudo sh -c "cd ~/Labs/PY05; docker compose -f compose.yml up -d --build"
```

##### Make a get request
2. Change directory into PY06: `cd ~/Labs/PY06` 
3. Create a new virtual environment, with the requests library installed:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install requests
```
4. Open the **retry.py** file, and add the following contents:
```python
#! venv/bin/python3
import requests

if __name__ == '__main__':
    response = requests.get('http://localhost:5000/api/flaky') # intentionally flaky endpoint
    print(response.status_code)
```
5. Execute the script:
```shell
./retry.py
```
6. Due to the implementation of the deliberately flaky endpoint, you have about a 50-50 chance of getting a 200 or 500 response. If needed, run the script a few times to observe this behaviour

##### Implement retry logic
7. Edit **retry.py**, and make the changes as shown below:
```python
#! venv/bin/python3
import requests

if __name__ == '__main__':
    try:
        response = requests.get('http://localhost:5000/api/flaky')
    except:
        response = requests.Response() # if the request fails with an exception, just create an empty response object as placeholder
    while response.status_code == None or response.status_code >= 500:
        try:
            response = requests.get('http://localhost:5000/api/flaky')
        except:
            response = requests.Response()
    if response.headers.get('content-type', '') == 'application/json':
        print(response.json())
```
8. This version of the script will first make an initial attempt to connect to the API. Since this could fail with an exception, you wrap this with a try-except. You then continuously re-attempt the request until you receive a response with a successful status code, before finally printing the response JSON from the server.  

##### Improve the retry logic
The retry logic you have just implemented has several weaknesses that you would want to avoid in reality. For a start, what if the server never delivers a successful response? You ideally should have some condition under which the client gives up attempting the request and reports a failure.  

Additionally, if the server is unavailable due to traffic saturation, this infinite loop of rapid-fire requests will only make matters worse.  

For these reasons, you will enhance your script to use a more robust retry methodology: _exponential backoff with timeout_. In this method, an exponentially increasing delay is added between attempts, to give the server time to return to a healthy state before the next retry, and a timeout is used to break out of the retry loop after so many failed requests.

9. Edit **retry.py** like so:
```python
#! venv/bin/python3
import requests
from time import sleep

if __name__ == '__main__':
    delay = 2 # initial delay between requests of 2 seconds
    try:
        response = requests.get('http://localhost:5000/api/flaky')
    except:
        response = requests.Response() # if the request fails with an exception, just create an empty response object as placeholder
    while response.status_code == None or response.status_code >= 500:
        if delay > 60: # if enough iterations have passed for delay to exceed 60s, give up
            print("too many failed attempts")
            break
        sleep(delay) # wait for the delay period
        try:
            response = requests.get('http://localhost:5000/api/flaky') # retry request
        except:
            response = requests.Response()
        delay *= 2 # double the delay if no successful response
    if response.headers.get('content-type', '') == 'application/json':
        print(response.json())
```
10. Run the script again. The retry logic ensures that you have a correct response, with a parseable JSON body, before you attempt to print the JSON. It also ensures you do not make an infinite loop of requests.

##### Implement header parsing
11. In the case of a 500 response, the flaky endpoint is configured to return a custom ERROR header as part of the response. You will now parse that header to get more info about the failure. 
12. Edit **retry.py** to print the header error message:
```python
#! venv/bin/python3
import requests
from time import sleep

if __name__ == '__main__':
    delay = 2 
    try:
        response = requests.get('http://localhost:5000/api/flaky')
    except:
        response = requests.Response()
    while response.status_code == None or response.status_code >= 500:
        if delay > 60: 
            print("too many failed attempts")
            break
        # add the below line to retrieve ERROR header details
        print("Error: " + response.headers.get("ERROR", "No Error header received"))
        sleep(delay) 
        try:
            response = requests.get('http://localhost:5000/api/flaky') 
        except:
            response = requests.Response()
        delay *= 2
    if response.headers.get('content-type', '') == 'application/json':
        print(response.json())
```
13. The added print statement parses the ERROR header, if it is present, and prints a debug message with this information. Re-run the script again to observe this behaviour.

Example ouput:

Error: Bad luck<br>
Error: Bad luck<br>
Error: Bad luck<br>
{'data': [1, 2, 3], 'result': 'success'}


#### Optional Stretch Tasks
- Refactor the retry script logic to use an else clause to the while-loop for better handling of loop exit conditions

## PY07
### Lab PY07 - Async Programming

#### Objective
Adapt an existing, synchronous script to operate asynchronously

#### Outcomes
By the end of this lab, you will have:
* Implemented async behaviour into a script with *asyncio*

#### High-Level Steps
- Run a synchronous script against the data from the example API
- Edit the script logic to use async features, qualitatively compare performance (quantitative comparison will come later)

#### Detailed Steps
##### Set up the API server for this exercise
1. Ensure the API server is running:
```shell
sudo docker ps | grep sample-flask-app || sudo sh -c "cd ~/Labs/PY05; docker compose -f compose.yml up -d --build"
```
2. Switch directory into the PY07 directory, and setup a virtual environment:
```bash
cd ~/Labs/PY07
python3 -m venv venv
source venv/bin/activate
pip3 install requests
```
3. Populate the API server with some sample data using the provided script:
```bash
./populate_books.py
```

##### Starting point
4. Review the contents of **client.py**. This is the starting point for the exercise. Observe that this initial client is entirely synchronous. You have two key functions in this file. 
* get_book() - retrieves a book by id from a given array of book objects
* process_book_data() - takes a book object, constructs a string from the book objects' attributes, sleeps to imitate some further, time-intensive processing, and then returns the string

The body of the script iterates a list of ids, and for each id uses get_book to get the corresponding book from a list (retrieved via an initial GET request to the API server) and then calls process_book_data on the returned object, in an entirely synchronous process. 

5. Run the **client.py** script:
```shell
./client.py
```
6. Make a mental note of roughly how long the script takes to execute - when benchmarking the script during the development of this lab it took approx. 6-7 seconds, but this may be different from machine to machine, and depending on how much data the API already had from previous labs

##### Introducing async
7. Open the **client.py** file for editing. You will make some key changes in order to make the script asynchronous.
###### Imports
8. You will need to import **asyncio** to be able to use the async features it provides:
```python
#! venv/bin/python3
import requests
import asyncio
```
###### get_book
9. You will also make both of your key functions asynchronous, starting with **get_book()**:
```python
async def get_book(iq, books, bq):
    i = await iq.get()
    book = dict()
    for b in books:
        if b.get("id", '') == i:
            book = b
            break
    await bq.put(book)
```
Note the implementation changes. Aside from declaring the function as async, the function now pulls the book id from a queue, and pushes the book object identified by that id into a separate queue
###### process_book_data
10. You will make similar changes to the **process_book_data** implementation:
```python
async def process_book_data(queue):
    book = await queue.get()
    bookstr = ""
    bookstr += f"ID: {str(book.get('id', ''))}\n"
    bookstr += f"TITLE: {book.get('title', '')}\n"
    bookstr += f"GENRE: {book.get('genre', '')}\n"
    await asyncio.sleep(1)
    print(bookstr)
```
Observe the use of a queue to pull books from. Also note that you are now directly printing the book string from this function rather than returning it. This is to minimise the changes needed to the script. A better approach would be to write the string to yet another queue, and have another async function read from that queue and print the strings out, but this is left as an open extension task, should you wish to attempt it.
###### main
11. You will now edit your main function, which will aggregate the various async logic elements into one entrypoint:
```python
async def main():
    books = requests.get('http://localhost:5000/api/books').json()
    books_queue = asyncio.Queue()
    ids_queue = asyncio.Queue()
    for i in ids:
        await ids_queue.put(i)
    gets = [get_book(ids_queue, books, books_queue) for i in ids]
    procs = [process_book_data(books_queue) for i in ids]
    await asyncio.gather(*gets)
    await asyncio.gather(*procs)
```
This function is now handling setting up the queue objects and the use of asyncio.gather() to run multiple instances of your coroutines concurrently
###### The main block
12. With main() consolidating all of the required logic, your  main block simply needs to asyncronously invoke the main() function:
```python
if __name__ == '__main__':
    asyncio.run(main())
```
###### The complete script
```python
#! venv/bin/python3
import requests
import asyncio

ids = [
    "0000012345",
    "0000012346",
    "0000012347",
    "0000012348",
    "0000012349",
    "0000012350"
]

async def get_book(iq, books, bq):
    i = await iq.get()
    book = dict()
    for b in books:
        if b.get("id", '') == i:
            book = b
            break
    await bq.put(book)

async def process_book_data(queue):
    book = await queue.get()
    bookstr = ""
    bookstr += f"ID: {str(book.get('id', ''))}\n"
    bookstr += f"TITLE: {book.get('title', '')}\n"
    bookstr += f"GENRE: {book.get('genre', '')}\n"
    await asyncio.sleep(1)
    print(bookstr)

async def main():
    books = requests.get('http://localhost:5000/api/books').json()
    books_queue = asyncio.Queue()
    ids_queue = asyncio.Queue()
    for i in ids:
        await ids_queue.put(i)
    gets = [get_book(ids_queue, books, books_queue) for i in ids]
    procs = [process_book_data(books_queue) for i in ids]
    await asyncio.gather(*gets)
    await asyncio.gather(*procs)

if __name__ == '__main__':
    asyncio.run(main())
```

##### Run the async script
13. Save the changes to client.py, and run the script again:
```shell
./client.py
```
14. Compare the execution speed to the original, non-async version. Benchmarks during the development of this lab have the async version taking only a second or so to execute, a significant reduction compared to ~6 seconds for the synchronous implementation.

#### Optional Stretch Tasks
- amend the script to also retrieve any author and review data from the API server, and process that. 
- stretch goal 1 will require adding additional calls to requests - investigate the use of the `aiohttp` library to make these requests asynchronously as well

#### Tidy Up
In ~/Labs/PY05 tear down the Flask application that what built and run with docker compose:

```shell
sudo docker compose down
```

## PY08
### Lab PY08 - Introduction to the Sandbox API

#### Objective
Deploy and interact with a RESTful API which manages developer sandboxes

#### Outcomes
By the end of this lab, you will have:
* Deployed a RESTful API using the *FastAPI* framework
* Used the FastAPI dev server's swagger UI to test API functionality
* Implemented Authentication for an API server

#### High-Level Steps
- Deploy the API
- Test using the swagger UI
- Add simple auth

#### Detailed Steps
##### Setup the Project
1. Switch directory into the PY08 directory:
```bash
cd ~/Labs/PY08
```
2. Create a new virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
venv/bin/python3 -m pip install -r requirements.txt
```

##### Deploy the API
3. Start the API server:
```bash
fastapi dev main.py
```

##### Interact with the API via swagger
4. Navigate to http://localhost:8000/docs in your browser to visit the API's _swagger_ interface. FastAPI automatically generates this interface along with an OpenAPI spec for your application.
5. Edit the example POST request body with the following data:
```json
{
  "name": "team-alpha-sbx",
  "owner_email": "owner@bankx.com",
  "size": "small",
  "ttl_days": 7,
  "allowed_cidrs": ["203.0.113.0/24"],
"id": "1234567891011121314151617181920A"
}
```
and execute the request.

7. Copy the returned sandbox ID from the POST request, and use it to experiment with the other endpoints exposed by the API using the UI.

TIPS:
- The id must be 32 chars long and can include any valid hex characters (0-9 and a-f)
- The size can be _small_ or _medium_
- When testing PATCH, copy the _etag_ returned from the GET request for the _if-match_ header
- Test the GET operations endpoint after POST and PATCH and then again after a DELETE request to see the different statuses of the sandbox



##### Implementing Authentication
Currently, the starter API is unauthenticated. You will change that. 

8. In **auth.py** add the following to add FastAPIs authentication middleware:
```python
from fastapi.security import HTTPBearer

security = HTTPBearer()
```
9. To use this middleware, make the following changes to **main.py**:
* Add these imports:
```python
import auth
from fastapi.security import HTTPAuthorizationCredentials
```
* Add the following additional parameter to each of the handler functions:
```python
authorization: Annotated[HTTPAuthorizationCredentials, Depends(auth.security)]
```
For example:
```python
@app.get("/v1/operations/{id}")
def get_operations(id: UUID, response: Response, authorization: Annotated[HTTPAuthorizationCredentials, Depends(auth.security)]):
    if not id:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"detail": "no sandbox ID specified"}
    response.status_code = status.HTTP_200_OK
    return sorted([op for op in store.get("operations") if op.sandbox_id == id], key = lambda o: o.timestamp)
```

The API will now automatically reject, with a 403, any request which does not present a bearer token. Note that the validity of any presented token is not yet being validated, only that one has been presented.

10. Save the changes to restart the API and test it via the swagger UI. Note that there is now an 'Authorize' button on the UI. This will allow you to add an appropriate credential which will be used when making the requests.

#### Optional Stretch Tasks
- Expand auth.py to read a set of valid tokens in from a file, and provide a helper function to check whether a token is valid. Add logic to each of your handler functions to call this function on the token presented as part of a request.

- Use your understanding of the requests library to implement scripted POST, GET, PATCH and DELETE requests to the API

## TF00
### Lab TF00 - Set Up Environment for Terraform Labs
#### Objective
Get access to a cloud environment against which to run terraform commands

#### Outcomes
By the end of this lab, you will have:
* Accessed the GCP cloud console
* Configured cloud service account credentials
* Installed Terraform

#### High-Level Steps
* log into the cloud console
* generate cloud service account credentials
* configure local environment variables
* install terraform

#### Detailed Steps
##### Configuring Cloud Access
1. If you have not already done so, sign up for a [QwikLabs](https://qa.qwiklabs.com) account, and provide the email used for signup to your instructor, so that they can add you to the classroom
2. Once you have been added to the classroom, refresh QwikLabs and click on the tile that says 'BOAQAAIP Terraform' to enter the classroom. 
3. From there, navigate into the lab itself, and click 'Start Lab' - this will create a new GCP environment
4. From the environment details, copy the GCP project ID - you will need this shortly
5. Right-click the 'open console' button and click 'open in incognito/inprivate window'. This will log you into the Google Cloud console.
6. Once in the cloud console, navigate to IAM & Admin > Service Accounts, and click on the service account name for the qwiklabs user
7. Navigate to the **Keys** tab, and click **Add key** > **Create new key**. Leave the type as JSON and click **Create**. The keyfile should automatically download.
8. While you are in the cloud console, navigate to **Compute Engine** > **Metadata**. Edit the metadata and set **enable-oslogin** to _false_. This will be important later.
9. Ensure you have an open VS Code window connected to WSL, with your home directory open in the explorer.
10. From your downloads, drag and drop the keyfile into the VS Code file explorer to move it into your WSL home directory
11. In a VS Code integrated terminal, run the following:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="~/<name_of_keyfile>.json"
echo !! | tee -a ~/.bashrc
export TF_VAR_gcp_project="<project ID you copied from qwiklabs>"
echo !! | tee -a ~/.bashrc
export TF_VAR_pubkey_path="$HOME/ansible_key.pub"
echo !! | tee -a ~/.bashrc
``` 
These commands create 3 environment variables and appends them to your bash script file so that these variables are available in your bash terminals.

##### Installing Terraform
12. Download and extract the Terraform binary using the provided script:
```bash
~/Labs/TF00/install_terraform.sh
```
13. Verify the installation: `terraform version`

## TF01
### Lab TF01 - Terraform Key Concepts

#### Objective
Deploy a cloud compute resource to a custom cloud network using Terraform

#### Outcomes
By the end of this lab, you will have:
* Used a Terraform provider and Terraform resources to manage compute and network infrastructure
* Reviewed the concept of state

#### High-Level Steps
* configure a terraform provider
* create a basic cloud compute resource
* configure networking via terraform
* use a startup script to deploy software as part of initialisation

#### Detailed Steps
##### Create a compute instance
1. In your terminal, switch to the TF01 directory: `cd ~/Labs/TF01`, and expand this directory in the VS Code file explorer.

2. Open the **main.tf** file, and add the following:
```terraform
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.13.0"
    }
  }
}

variable "gcp_project" {}

provider "google" {
    project = var.gcp_project
    region = "us-east1"
}
```
See the [google provider documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs) for details on more configuration options

3. Once you have set up the provider configuration, run:
```shell
terraform init
```
At this point, Terraform will install the provider, as well as initialising a few other things, some of which you will see later

4. Review the [documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) for the google_compute_instance resource type. Add, to the **instance.tf** file, a block defining a VM with the following configuration:
* name: demo-instance-1
* machine type: e2-medium
* zone: us-east1-b
* boot disk image: debian 12
* network: default
* network access tier: standard
* allow_stopping_for_update = true

See the solution below if needed.
<details>
<summary>
Solution 1 - Compute Instance
</summary>

```terraform
resource "google_compute_instance" "vm1" {
  name         = "demo-instance-1"
  machine_type = "e2-medium"
  zone         = "us-east1-b"

  allow_stopping_for_update = true
  
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }
  
  network_interface {
    network = "default"

    access_config {
      network_tier = "STANDARD"
    }
  }
}
```

</details>

##### Deploy the Instance
5. Plan and create the resource:
```shell
terraform plan
terraform apply
```
Enter 'yes' to confirm the apply when prompted.  

6. Once the apply is complete, navigate to **Compute Engine > VM Instances**. You should see a new VM instance.
7. Review the newly-created _terraform.tfstate_ file. This is how Terraform tracks the resources that it is managing.
8. Destroy the VM: `terraform destroy` (entering 'yes' to confirm destruction when prompted)
9. Review the tfstate file again - note that it now contains no resources, as the instance has been deleted
10. Before moving on, comment out the contents of the **instance.tf** file . In VS Code editor, add a multi-line comment character to line 1 '/\*' and add a closing multi-line comment character to the last line of the file '*/'

##### Deploying the network
11. You will now redeploy your instance, but onto a custom network. Open the **network.tf** file, and add the following resources:
* a network named 'custom-vpc'
* a custom subnetwork for the custom network with the following configuration:
  * name: custom-subnet
  * ip cidr range: 10.0.1.0/24
  * region: us-east1  

For guidance, consult the following documentation:
* [network](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network)
* [subnet](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork)  

See the solution below if needed
<details>
<summary>Solution 2 - Network Configuration</summary>


```terraform
resource "google_compute_network" "lab-vpc" {
  name                    = "custom-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "lab-subnet" {
  name          = "custom-subnet"
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-east1"
  network       = google_compute_network.lab-vpc.id
}
```
</details>

12. Plan and apply the network deployment:
```shell
terraform plan
terraform apply
```
When, prompted, enter 'yes' to confirm the apply.

##### Configuring the firewall
13. To make compute instances in your new network accessible, the network will require a firewall allowing relevant access. Add a firewall resource to **firewall.tf** with the following config:
* name: custom firewall
* network: the custom network you created above
* allowed ports: 8080 and 8081
* a single source range of 0.0.0.0/0  

For guidance, consult the [firewall documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall), and see solution below if required:
<details>
<summary>
Solution 3 - Firewall Config
</summary>

```terraform
resource "google_compute_firewall" "lab-firewall" {
  name    = "custom-firewall"
  network = google_compute_network.lab-vpc.name

  allow {
    protocol = "tcp"
    ports    = [8080, 8081]
  }

  source_ranges = ["0.0.0.0/0"]
}
```
</details>

14. To add the firewall to the network, perform another plan and apply:
```shell
terraform plan
terraform apply
```

##### Deploy the VM
15. Finally, you will deploy a VM into the custom network you have created. Uncomment the contents of **instance.tf** and make the following change to the _network_interface_ section:
```terraform
  network_interface {
    subnetwork = google_compute_subnetwork.lab-subnet.name
```
Perform another plan and apply:
```shell
terraform plan
terraform apply
```
Once the apply is complete, the instance should appear in the compute engine in the GCP console.

##### Making use of the ports
16. You can make this a more interesting deployment by making a small change to the instance configuration. Add the following to the instance resource, in your **instance.tf** file:
```terraform
  metadata_startup_script=file("deploy.sh")
```
17. Re-run the terraform plan and apply:
```shell
terraform plan
terraform apply
```
18. The instance will be destroyed and recreated, and the new instance will run the provided script on boot. Once the new instance is started, you should be able to access the following ports on the VM's external IP:
- 8080: should display the default NGINX landing page
- 8081: should display the Apache 'It Works!' response

##### Clean up
19. To clean up the resources created by terraform, perform a terraform destroy:
```shell
terraform destroy
```
Type 'yes' to confirm destruction when prompted.

## TF02
### Lab TF02 - Work With Terraform Modules

#### Objective
Modularise a complex Terraform deployment, to enable greater reusability

#### Outcomes
By the end of this lab, you will have:
* Created reusable Terraform modules defining compute and network resources
* Configured variables and outputs to pass data to/from modules
* Used modules as part of a complex deployment

#### High-Level Steps
* Decompose existing configuration into modular structure
* Define variables and parameterise resources
* Define outputs to move data between modules
* Reference child modules from a root module

#### Detailed Steps
##### Configuring the modules
1. Change directory into the lab folder: `cd ~/Labs/TF02`, and review the starting point for the lab. Terraform, like Python, allows the importing of code from another source for use as a _module_

2. Begin by breaking up your existing configuration from the previous lab:
* `instance/main.tf` should contain the google_compute_instance resource block
* `network/main.tf` should contain the google_compute_network, google_compute_subnetwork and google_compute_firewall blocks
* the root `main.tf` file should contain only the provider configuration, for now

3. Now you can begin parameterising the existing code using _variables_ for better reusability. Open `network/variables.tf` and add the following:
```terraform
variable "network_name" {}
variable "ip_cidr_range" {}
variable "allowed_ports" {}
variable "region" {}
```
3. You can then parameterize the `network/main.tf` file using these values. You should be able to work out where they go from the variable names, but see the solution below if needed.

<details>

<summary>Solution: network/main.tf</summary>

```terraform
resource "google_compute_network" "lab-vpc" {
  name                    = var.network_name
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "lab-subnet" {
  name          = "${var.network_name}-subnet"
  ip_cidr_range = var.ip_cidr_range
  region        = var.region
  network       = google_compute_network.lab-vpc.id
}

resource "google_compute_firewall" "lab-firewall" {
  name    = "${var.network_name}-firewall"
  network = google_compute_network.lab-vpc.name

  allow {
    protocol = "tcp"
    ports    = var.allowed_ports
  }

  source_ranges = ["0.0.0.0/0"]
}
```

</details>
<br>

4. Now do the same for the instance. Add the following contents to `instance/variables.tf`:
```terraform
variable "instance_name" {}
variable "region" {}
variable "machine_type" {}
variable "subnet_name" {}
variable "script_path" {}
```
Update `instance/main.tf` to use these variables.

See the solution below if needed.

<details>

<summary>Solution: instance/main.tf</summary>

`instance/main.tf` contents:
```terraform
resource "google_compute_instance" "vm" {
  name         = var.instance_name
  machine_type = var.machine_type
  zone         = "${var.region}-b"

  allow_stopping_for_update = true
  
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }
  
  metadata_startup_script = file(var.script_path)
  
  network_interface {
    subnetwork = var.subnet_name

    access_config {
      network_tier = "STANDARD"
    }
  }
}
```
</details>
<br>

##### Adding Outputs
5. There is one more thing needed. Since the subnet and instance are defined in separate modules, the instance cannot access the subnet name directly from the resource as it did previously. Instead, the network module must expose the subnet name as an *output* which can then be passed to the instance module. Add the following to `network/outputs.tf`:
```terraform
output "subnet_name" {
  value = google_compute_subnetwork.lab-subnet.name
}
```
7. While you are configuring outputs, add an output to the instance module as well:
```terraform
output "vm_ip" {
  value = google_compute_instance.vm.network_interface[0].access_config[0].nat_ip
}
```

##### Using the modules
8. Now that your modules are set up, you can call them from main.tf. Edit the _root_ **main.tf** and add the following to what is already there:
```terraform
module "network" {
  source = "./network"
  network_name = "lab2-vpc"
  region = "us-east1"
  allowed_ports = ["22", "80", "8080", "8081"]
  ip_cidr_range = "10.0.1.0/24"
}

module "server" {
  source = "./instance"
  region = "us-east1"
  subnet_name = module.network.subnet_name
  machine_type = "e2-medium"
  instance_name = "app-server"
  script_path = "${path.root}/deploy.sh"
}
```
9. To make sure that you get the VM IP, add the following to `outputs.tf`:
```terraform
output "server_ip" {
  value = module.server.vm_ip
}
```

10. Deploy the resources using the init-plan-apply workflow:
```shell
terraform init
terraform plan
terraform apply
```

11. Once the apply is complete, you should see the server_ip output in the terminal. Test that the deployment worked:
```shell
curl http://<server_ip>:8080
curl http://<server_ip>:8081
```

### Leveraging reusability
12. Now that you have modularised this deployment, you could use these same modules to create as many VPC and compute instance resources as you need. To demonstrate this, you will deploy a second instance. Add another module using instance/ as its source to **main.tf**, like so:
```terraform
module "proxy" {
  source = "./instance"
  region = "us-east1"
  subnet_name = module.network.subnet_name
  machine_type = "e2-medium"
  instance_name = "proxy-server"
  script_path = "${path.root}/proxy.sh"
}
```

13. And add another output to `outputs.tf`:
```terraform
output "proxy_ip" {
  value = module.proxy.vm_ip
}
```

14. The provided proxy.sh script will need to be updated with the correct IP address - there are many ways you could do this, but for now you will use _sed_:
```bash
sed -i 's,{{ SERVER_IP }},<your server ip>,g;' proxy.sh
```

15. Once again, init, plan and apply the deployment - only the new instance should need to be created. 
```shell
terraform init # needs to be re-run because you've added a new module
terraform plan
terraform apply
```

16. Once the apply is complete, grab the value of the proxy_ip output, and test it with curl:
```shell
curl http://<proxy_ip>/nginx # should return nginx landing page
curl http://<proxy_ip>/apache # should return It Works!
```

### Clean up
17. To clean up the resources created by terraform, perform a terraform destroy:
```shell
terraform destroy
```
## ANS01
### Lab ANS01 - Ansible Introduction

#### Objective
Use ansible to deploy a webserver resource locally

#### Outcomes
By the end of this lab, you will have:
* Installed Ansible
* Used an ad-hoc command to configure a local webserver

#### High-Level Steps
* Install Ansible
* Install NGINX via an ad-hoc command
* Uninstall NGINX via an ad-hoc command

#### Detailed Steps
##### Installation
1. You can install Ansible in many ways, here you are going to use `apt`. Switch into the ANS01 directory and run the provided install script:
```bash
cd ~/Labs/ANS01
./install_ansible.sh
```

##### Use Ansible to Install a Web Server
2. Now you are going to run an ad-hoc command to install NGINX. Start a bash terminal as the superuser:

```bash
sudo bash
```
Run an ad-hoc command to install NGINX:
```bash
ansible 127.0.0.1 -m apt -a "name=nginx state=present update_cache=true" --become
```

`-m apt` is letting Ansible know to use the `apt` module and the `-a` defines any arguments to pass to that module. `--become` is giving you sudo privileges for this play. 

You should see that Ansible returns a JSON object, showing you that it has completed the task. 

##### Check NGINX has been Installed Correctly
3. The `curl` command can be used to check that your web server is running correctly:
```bash
curl http://localhost
```
You should get a response back similar to this:
```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

4. Run the ansible command again. You should see that the execution is a lot quicker and that you get a different output, like this:
```bash
ansible 127.0.0.1 -m apt -a "name=nginx state=present update_cache=true" --become
```
```
localhost | SUCCESS => {
    "cache_update_time": 1612268706, 
    "cache_updated": true, 
    "changed": false
}
```
You can see that the changed value is false; this means Ansible noticed that NGINX was already installed and didn't make any changes as the state is already present. You can run this command as many times as you like and you will see a success message.

5. You will now remove nginx, so that you can install it again in a subsequent lab. Run the following:
```bash
ansible 127.0.0.1 -m apt -a "name=nginx state=absent update_cache=true" --become
```
Note the change here: state=absent instead of state=present

## ANS02
### Lab ANS02 - Ansible Playbooks and Inventories

#### Objective
Use an Ansible playbook to define a configuration job declaratively and execute it against an inventory of cloud targets

#### Outcomes
By the end of this lab, you will have:
* Created an Ansible playbook
* Executed a playbook using Ansible

#### High-Level Steps
* Use an Ansible _playbook_ to configure a local host
* Define a _static inventory_ of remote hosts to configure
* Use a _dynamic inventory_ to automatically detect remote targets

#### Detailed Steps
##### Setup
1. Start by switching into the ANS02 lab directory:
```bash
cd ~/Labs/ANS02
```

##### NGINX Configuration
2. NGINX web server is configured using a `.conf` file. Review the provided nginx.conf:
```conf
events {}
http {
    server {
       listen 80;
       location / {
            return 200 "Hello new nginx\n";
        }
    } 
}
```
This will eventually change what NGINX presents.

##### Ansible Playbook
3. Open the playbook.yml file, and review the contents:
```yaml
- hosts: localhost
  connection: local
  become: true
  tasks: []
```
This defines a single, currently empty _play_, targeting the local machine. A play is made up of _tasks_, which are the individual configuration actions required by the play. A _playbook_ can define one or more plays.

4. With reference to the documentation for the [apt](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/apt_module.html) module, add a task to this play which installs nginx - i.e. the same outcome as you acheived with the ad-hoc command previously. See the solution below if required.

<details>
<summary>Playbook - Solution 1</summary>

```yaml
- hosts: localhost
  connection: local
  become: true
  tasks:
  - name: Install NGINX
    apt:
      name: nginx
      state: present
      update_cache: true
```
</details>

##### Apply the configuration
5. Using the `ansible-playbook` command, apply the configuration. Use the **-K** switch to prompt ansible to ask for the password for the _become: true_ privilege escalation. Enter 'qa' when prompted:
```bash
ansible-playbook playbook.yml -K
```
6. Now you can perform the curl command to check that NGINX is installed.
```bash
curl localhost
```
You should see something like this:
```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

##### Add new tasks / configurations
7. Now add two more tasks to the playbook - one to copy the custom nginx configuration from the local workspace to **/etc/nginx/nginx.conf**, and one to restart the NGINX service to ensure the new configuration is loaded. 

Refer to the docs for the [copy](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/copy_module.html) and [service](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/service_module.html) modules, and see the solution below if needed.

<details>
<summary>Playbook - Solution 2</summary>

```yaml
- hosts: localhost
  connection: local
  become: true
  tasks:
  - name: install nginx
    apt:
      name: nginx
      state: present
      update_cache: true
  
  - name: Copy nginx file over
    copy:
      src: nginx.conf
      dest: /etc/nginx/nginx.conf

  - name: Restart nginx if needed
    service:
      name: nginx
      state: restarted
```
</details>

<br>
8. Re-run the playbook:

```bash
ansible-playbook playbook.yml
```
You should see this in the output:

```
TASK [Restart nginx if needed] ***************************************************************************************************************************************************
changed: [localhost]
```

9. Now see what NGINX is showing.
```bash
curl localhost
```
You should see:
```
Hello new nginx
```
10. Run the playbook again. Notice that, even though nothing has changed, NGINX still gets restarted. 

This can be improved upon by adding a condition to the task that restarts NGINX to only execute when the copy task changes something. Amend the nginx tasks like so:
```yaml

  - name: Copy nginx file over
    copy:
      src: nginx.conf
      dest: /etc/nginx/nginx.conf
    register: nginx_config # add this line

  - name: Restart nginx if needed
    service:
      name: nginx
      state: restarted
    when: nginx_config.changed == true # add this line
```
11. Now run the playbook again and see how the output changes.
```bash
ansible-playbook playbook.yml
```
Now the same section in the output should say this.
```
TASK [Restart nginx if needed] ***************************************************************************************************************************************************
skipping: [localhost]
```
It has skipped that last section because the copy section was unchanged.

##### Working With Inventories
So far you have run all of your tasks against localhost. The real power of Ansible lies in its ability to configure remote hosts. For this, you must make remote host information available to Ansible via an _inventory_

##### Configure SSH Keys
When connecting to remote linux hosts, Ansible uses SSH. This means you will need an SSH key that Ansible can use to connect to the instances you will be working with. 
1. Generate a new SSH key pair. You will reuse this key pair often so for convenience, place it in your home directory:
```bash
ssh-keygen -q -t ed25519 -f ~/ansible_key # make sure to leave the key WITHOUT a passphrase
```

##### Provision Instances
Now that you have a key pair, you can provision some VM instances. The lab folder already contains the necessary Terraform files to deploy a set of VMs onto a network with access to required ports. Feel free to review the terraform configuration. It should be mostly familiar to you.

NOTE: The count attribute is used to create 2 VM instances using the 'servers' module. All 3 VMs (the 2 servers and the proxy VM) have had a 'role' label of _appserver_ or _proxy_ added by the Terraform configuration.

2. Provision the infrastructure by following the usual Terraform workflow:
```bash
cd ~/Labs/ANS02/terraform
terraform init
terraform plan 
terraform apply 
```
3. Wait for the apply to finish. Once the apply is complete, make a note of the IPs of your VMs as displayed by the Terraform outputs.

##### Connectivity Check
4. Before continuing, it would be a good idea to check that everything is configured correctly for SSH. For each of the IP addresses output by terraform, run the following:
```bash
ssh -i ~/ansible_key ansible@<ip_address>
```
When prompted, enter 'yes' to trust the host keys from the VMs.  
Note: the username 'ansible' is important, as this is the username for which the public SSH key has been added to the VMs.

Use _exit_ to disconnect each ssh terminal as you test each IP address.

##### Creating the inventory
Now that you have remote hosts configured for SSH access, you can use an inventory to provide this information to Ansible. 

5. Edit the **inventory.yml** file, filling in your IP addresses:
```yaml
all:
  children:
    test:
      hosts:
        IP_OF_HOST_1: # replace 
        IP_OF_HOST_2: # replace
        IP_OF_HOST_3: # replace
      vars:
        ansible_user: ansible
        ansible_ssh_private_key_file: '~/ansible_key'
```
Example:

Note: the IP addresses end with a colon.

```yaml
all:
  children:
    test:
      hosts:
        35.207.39.191: 
        35.211.10.250:
        35.211.130.212:
      vars:
        ansible_user: ansible
        ansible_ssh_private_key_file: '~/ansible_key'
```
This defines a single group of hosts, called 'all', with one subgroup called 'test'. You have also defined the ansible user and SSH key file to use to make the SSH connection.

##### Playbook
6. Open the **test_playbook.yml** file, and add the following contents:
```yaml
---
- hosts: all
  name: Ping Hosts
  tasks:
  - name: "Ping {{ inventory_hostname }}"
    ping:
    register: ping_info
  
  - name: "Show ping_info in console"
    debug:
      msg: "{{ ping_info }}"
```
This playbook tells Ansible to connect to all hosts defined in the inventory file and run the `ping` module. It then takes the output of the ping operation and uses the debug module to print it to the terminal.

7. This playbook will confirm that you can successfully connect to all of the hosts and execute tasks on them. Remember to navigate out of the terraform directory before running the playbook: `cd ..`


```bash
ansible-playbook -v -i inventory.yml test_playbook.yml
```
The `-i` command is used to pass the inventory file.

The `-v` command is used to cause Ansible to print more debug messages.

You should see output similar to the following, indicating that Ansible was able to connect successfully to the hosts configured in the inventory file:

```text
<output omitted>
TASK [Show ping_info in console] ************************************************************************************
ok: [IP_OF_HOST_1] => {
    "msg": {
        "changed": false, 
        "failed": false, 
        "ping": "pong"
    }
}
ok: [IP_OF_HOST_2] => {
    "msg": {
        "changed": false, 
        "failed": false, 
        "ping": "pong"
    }
}
ok: [IP_OF_HOST_3] => {
    "msg": {
        "changed": false, 
        "failed": false, 
        "ping": "pong"
    }
}

PLAY RECAP **********************************************************************************************************
IP_OF_HOST_1                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
IP_OF_HOST_2                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
IP_OF_HOST_3                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```
8. Update the **test_playbook.yml** to install _nginx_ and _git_ on the remote servers. Refer back to previous solutions if needed.

Test by issuing `curl` commands to each IP address. SSH into each VM and check the version of git with `git --version`

##### Using a Dynamic Inventory
The inventory file you have just created, with hardcoded host IPs, is called a _static inventory_. This is not particularly useful when configuring environments that have ephemeral infrastructure, with instances being constantly provisioned and deprovisioned. For such environments, you can instead use _dynamic inventories_ to automatically detect and group hosts within a cloud environment.

9. Destroy the existing instances, and create new ones:
```bash
cd ~/Labs/ANS02/terraform
terraform destroy 
terraform apply 
```
This will create new instances with new IP addresses.

10. Review the provided `inventory.gcp_compute.template.yml`. This uses the relevant dynamic inventory plugin to query GCP for instances, and construct an inventory from the results. See the [documentation](https://docs.ansible.com/projects/ansible/latest/collections/google/cloud/gcp_compute_inventory.html) for the plugin for more details.

11. Before you can use the plugin, you need a few more things.
* Ansible needs access to the `google-auth` python package to be able to authenticate to GCP:
```bash
sudo apt-get update
sudo apt-get install python3-google-auth
```
* The inventory file currently holds a placeholder for the project. You can fill this in using the ansible _template_ module:
```bash
cd ~/Labs/ANS02
ansible 127.0.0.1 -m template -a "src=$(pwd)/inventory.gcp_compute.template.yml dest=$(pwd)/inventory.gcp_compute.yml" -e "GCP_PROJECT=$TF_VAR_gcp_project"
```
This creates a new file `inventory.gcp_compute.yml` with the GCP_PROJECT variable changed to your GCP Project name (line 5).

12. Verify that the new inventory can detect the new hosts:
```bash
ansible-inventory -i inventory.gcp_compute.yml --list
```
13. In order to execute playbooks against these dynamically detected hosts, there is one thing missing: the SSH configuration. Since this will not be included in the generated inventory, you will need to define this information elsewhere. One way to do this is via a config file, _ansible.cfg_, located in the same directory as your inventory and playbook.

Add the following to **ansible.cfg**:
```ini
[defaults]
  remote_user=ansible
  private_key_file=~/ansible_key

[ssh_connection]
  ssh_args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"
```
This defines the user and keyfile that were previously set in inventory.yml, and also disables host key checking.  

14. You can now use the dynamic inventory to run the same playbook as before, against the new hosts:
```bash
ansible-playbook -i inventory.gcp_compute.yml test_playbook.yml -K
```
15. As before, test that NGINX has been successfully installed using curl.

##### Clean Up
16. Destroy the resources you have created:
```bash
cd ~/Labs/ANS02/terraform
terraform destroy 
```
## ANS03
### Lab ANS03 - Variables, Handlers, Facts and Templates

#### Objective
Parameterise Ansible configuration files and enhance the reusability of Ansible config.

#### Outcomes
By the end of this lab, you will have:
* Used variables and facts to parameterise an Ansible playbook
* Used Ansible's template module to dynamically alter the contents of a file
* Used handlers to make individual tasks repeatable on-demand
* Used a role to streamline the reuse of Ansible configuration 

#### High-Level Steps
* Parameterise the existing playbook
* Use Jinja2 templating to parameterise files
* Decompose existing config into roles

#### Detailed Steps

##### Deploy the Infrastructure
1. You can use the same terrform files from the previous lab to provision the target infrastructure for this lab. Change directory into the folder and apply the configuration:
```bash
cd ~/Labs/ANS02/terraform
terraform plan 
terraform apply 
```
2. Make a note of the server IPs and proxy IP outputs, as you will use these later

##### Starting Point - Playbook, Inventory and NGINX Configs
Change into the ANS03 directory and review the initial playbook state:
```yaml
---
- hosts: all
  become: true
  tasks:
  - name: Install NGINX
    apt:
      pkg: 
      - nginx
      - git
      state: latest
      update_cache: true
  - name: Start NGINX Service
    service:
      name: nginx
      state: started
- hosts: gcp_role_appserver
  become: true
  tasks:
  - name: 'update website from the git repository'
    git:
      repo: "https://gitlab.com/qacdevops/static-website-example"
      dest: "/opt/static-website-example"
  - name: 'install the nginx.conf file on to the remote machine'
    copy:
      src: nginx-server.conf
      dest: /etc/nginx/nginx.conf
  - name: Restart NGINX Service
    service:
      name: nginx
      state: restarted
- hosts: gcp_role_proxy
  become: true
  tasks:
  - name: transfer_nginx_conf
    copy:
      src: nginx-proxy.conf
      dest: /etc/nginx/nginx.conf
  - name: Restart NGINX Service
    service:
      name: nginx
      state: restarted
```
Summary:
* Install NGINX and git on all hosts
* Setup a static website on the appserver hosts, and supply a custom nginx.conf to serve it
* For the proxy, supply a custom NGINX config which will load balance between the appservers.

4. Use the template **inventory.gcp_compute.template.yml** to fill in your project ID:
```bash
cd ~/Labs/ANS03
ansible 127.0.0.1 -m template -a "src=$(pwd)/inventory.gcp_compute.template.yml dest=$(pwd)/inventory.gcp_compute.yml" -e "GCP_PROJECT=$TF_VAR_gcp_project"
```
5. Now edit lines 5 and 6 in the **nginx-proxy.conf** file and add the server IP addresses you noted earlier (Note: be careful to use the server IPs, NOT the proxy IP):
```conf
    upstream appservers {
        server SERVER_1_IP:8080; # <- edit this line
        server SERVER_2_IP:8080; # <- and this one
    }
```

6. Copy the **ansible.cfg** file from ANS02 to ANS03 to ensure Ansible connects to the remote VMs as the 'ansible' user rather than your user (qa). This will also stop errors regarding changes to host key files.

7. Execute the playbook:
```bash
ansible-playbook -i inventory.gcp_compute.yml playbook.yml
```
8. Once the execution is complete, navigate to the proxy IP in a browser. You should be presented with the static website. 

9. Before continuing, destroy and recreate the infrastructure, so that you have a clean slate for the next part of the lab:
```bash
cd ~/Labs/ANS02/terraform
terraform destroy 
terraform apply 
```
When the apply is complete, note the new proxy IP.

##### Improvements
So far, whilst this is a longer playbook than those you have used previously, everything you have done should be fairly familiar from previous activities. You will now improve upon the basic playbook by introducing _variables_, _handlers_, _roles_ and _templates_:
* _Variables_ allow for parameterised execution of playbooks. The same playbook can be executed against the same set of hosts, with different parameters, leading to potentially very different results. The same playbook can be executed on multiple systems using variables to manage the differences between those systems. This ensures greater reusability of playbooks.
* _Handlers_ are tasks within a playbook that can be triggered on-demand by a notification from another task.
* _Roles_ are directories containing a collection of tasks and other resources which can be referenced within playbooks, in order to streamline the re-use of complex configurations. Ansible roles are a similar concept to Terraform modules.
* _Templates_ are used to dynamically alter the contents of a file before copying to a remote host, allowing for the reuse of config files.  

10. You will start by using variables to parameterise the playbook. Edit lines 21 and 22 of **playbook.yml** and replace the hard-coded git repo and install path with variables:
```yaml
...
  - name: 'update website from the git repository'
    git:
      repo: "{{ repository_url }}" # <- edit this line
      dest: "{{ install_dir }}"    # <- and this one
...
```
Now the repository and the install directory are parameterised, you could potentially re-use this playbook to install any repository into any location on the target hosts.  

11. Next, you will reconfigure the nginx config files to act as templates. Starting with **nginx-server.conf**, edit line 5:
```conf
        root {{ install_dir }}; # <- add the template expression here
```
Ansible templates are rendered by the _Jinja2_ templating engine prior to transfer to the host, allowing for injection of dynamic parameters. The server config is a fairly simple template, referencing the same install_dir variable as in the playbook. You can also use templates to improve the proxy config.  

12. Replace the contents of **nginx-proxy.conf** with the following:
```conf
events {}

http {
    upstream appservers {
        {% for host in groups['gcp_role_appserver'] %}
        server {{ hostvars[host]['ansible_facts']['default_ipv4']['address'] }}:8080;
        {% endfor %}
    }
    server {
        listen 80;
        location / {
            proxy_pass http://appservers;
        }
    }
}
```
This is a slightly more complex template which uses a for-loop over the hosts in the gcp_role_appserver group to dynamically construct the upstream, using _facts_ about the hosts to retrieve the IP addresses.  

13. To use these templates effectively, you must also update the playbook again, replacing 'copy' with 'template' on lines 24 and 35. 

14. The complete playbook should now be as follows:
```yaml
---
- hosts: all
  become: true
  tasks:
  - name: Install NGINX
    apt:
      pkg: 
      - nginx
      - git
      state: latest
      update_cache: true
  - name: Start NGINX Service
    service:
      name: nginx
      state: started
- hosts: gcp_role_appserver
  become: true
  tasks:
  - name: 'update website from the git repository'
    git:
      repo: "{{ repository_url }}"
      dest: "{{ install_dir }}"
  - name: 'install the nginx.conf file on to the remote machine'
    template:
      src: nginx-server.conf
      dest: /etc/nginx/nginx.conf
  - name: Restart NGINX Service
    service:
      name: nginx
      state: restarted
- hosts: gcp_role_proxy
  become: true
  tasks:
  - name: transfer_nginx_conf
    template:
      src: nginx-proxy.conf
      dest: /etc/nginx/nginx.conf
  - name: Restart NGINX Service
    service:
      name: nginx
      state: restarted
```

15. Execute the playbook, passing in the variables:
```bash
cd ~/Labs/ANS03
ansible-playbook -i inventory.gcp_compute.yml playbook.yml -e "repository_url=https://gitlab.com/qacdevops/static-website-example install_dir=/opt/static-website-example"
```

16. Once execution is complete you should again be able to access the website by navigating to the proxy IP in a browser.

NOTE: Ensure you are using `http` not https 

17. Destroy and recreate the infrastructure once again, to provide a clean slate:
```bash
cd ~/Labs/ANS02/terraform
terraform destroy 
terraform apply 
```

##### Handlers and Roles
18. You can now make a few more changes to your configuration to reduce a lot of the repetition and improve reusability. You will start by initialising 3 _roles_:
```bash
cd ~/Labs/ANS03
ansible-galaxy init common
ansible-galaxy init appserver
ansible-galaxy init proxy
```
A role defines a collection of tasks, templates, variables and other data which can then by used within a playbook without having to duplicate the config. You will configure the three roles to hold most of your configuration.  

19. Backup your existing playbook, for comparison later:
```bash
cp playbook.yml playbook-old.yml
``` 

20. Move the 'Install NGINX' and 'Start NGINX Service' tasks from _playbook.yml_ to _common/tasks/main.yml_

21. Move the 'update website from the git repository' and 'install the nginx.conf file on to the remote machine' tasks from _playbook.yml_ to _appserver/tasks/main.yml_

22. Move the 'transfer_nginx_conf' task from _playbook.yml_ to _proxy/tasks/main.yml_

23. Copy the two nginx.conf templates into their respective roles' templates directory:
```bash
cp nginx-server.conf appserver/templates/nginx-server.conf
cp nginx-proxy.conf proxy/templates/nginx-proxy.conf
```
24. Now that you have your roles, you will define a _handler_ for restarting NGINX, to avoid duplicated tasks. Add the following to _common/handlers/main.yml_:
```yaml
- name: restart nginx
  service:
    name: nginx
    state: restarted
```
25. Now, go through the tasks for each of your roles and add the following to each of the templating tasks:
```yaml
  notify: restart nginx
```
Example:

```yaml
- name: 'install the nginx.conf file on to the remote machine'
  template:
    src: nginx-server.conf
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```
##### Solutions
The files you have edited so far should now hold the following contents:
* `common/tasks/main.yml`:
```yaml
---
- name: Install NGINX
  apt:
    pkg: 
    - nginx
    - git
    state: latest
    update_cache: true
- name: Start NGINX Service
  service:
    name: nginx
    state: started
```
* `common/handlers/main.yml`:
```yaml
---
- name: restart nginx
  service:
    name: nginx
    state: restarted
```
* `appserver/tasks/main.yml`:
```yaml
---
- name: 'update website from the git repository'
  git:
    repo: "{{ repository_url }}"
    dest: "{{ install_dir }}"
- name: 'install the nginx.conf file on to the remote machine'
  template:
    src: nginx-server.conf
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```
* `proxy/tasks/main.yml`:
```yaml
---
- name: transfer_nginx_conf
  template:
    src: nginx-proxy.conf
    dest: /etc/nginx/nginx.conf
  notify: restart nginx
```

26. Now with most of your configuration separated out into roles, the playbook itself can become much simpler.

* `playbook.yml`
```yaml
---
- hosts: gcp_role_appserver
  become: true
  vars:
    repository_url: "https://gitlab.com/qacdevops/static-website-example"
    install_dir: "/opt/static-website-example"
  roles:
  - common
  - appserver
- hosts: gcp_role_proxy
  become: true
  roles:
  - common
  - proxy
```
NOTE: you have included the variables within the playbook as an alternative to supplying them from the command prompt.

27. Executing the playbook and navigating to the proxy IP in a browser should, once again, result in the website being accessible:
```bash
ansible-playbook -i inventory.gcp_compute.yml playbook.yml
```

28. Deprovision the insfrastructure used in this lab:

```bash
cd terraform
terraform destroy
```
## ANS0X
### Lab ANS0X - Optional Stretch Goal
If you have completed the main labs, you should be able to synthesise what you have covered to:
* provision a compute instance, on a custom network, with a firewall exposing ports 22 and 5000
* set up a dynamic inventory
* set up a playbook which targets your compute instance and:
  * installs git and docker
  * clones the sample flask API from earlier: (this can be found in its own repo at https://github.com/qa-tech-training/example_python_flask_apiserver.git)
  * uses docker to build the container image and deploy a container from it (hint: see the documentation for the Ansible [community.docker](https://docs.ansible.com/projects/ansible/latest/collections/community/docker/index.html) collection)

You might also then be able to amend your playbook to:
* install the docker compose plugin for the ansible user on the remote machine
* use docker compose to orchestrate the creation of the container image and deployment of the container

## ANS04
### Lab ANS04 - Playbook Performance Optimisation

#### Objective
Use ansible configuration options and advanced features of ansible to profile and optimise the performance of your playbooks

#### Outcomes
By the end of this lab, you will have:
* Configured performance profiling for Ansible playbooks
* Configured fact and inventory caching
* Configured performance-impacting SSH parameters

#### High-Level Steps
* Enable performance profiling
* Enable caching
* Set up SSH optimisations

#### Detailed Steps

##### Setup Instances
1. Switch into the ANS04 directory, and review the starting point for this lab:
```bash
cd ~/Labs/ANS04
```

2. Provision the infrastructure with terraform:
```bash
cd terraform
terraform init
terraform apply
```
##### Profiling playbook execution
3. Switch into the ansible directory:
```shell
cd ~/Labs/ANS04/ansible
```
4. Before configuring the compute instances, edit the **ansible.cfg** file, adding the following line to the _defaults_ section:
```ini
    callbacks_enabled = timer, profile_tasks, profile_roles
```
NOTE: this adds 3 callback plugins which add new behaviours to Ansible when responding to events:
* the _timer_ callback plugin adds total play duration to the play stats in stdout
* the _profile_tasks_ plugin is used to measure and display the execution time of individual tasks within a playbook and provide a performance summary at the end (tasks recap)
* the _profile_roles_ plugin adds timing information to roles and provides a summary at the end (roles recap)


5. Update the inventory and invoke the playbook:
```shell
ansible 127.0.0.1 -m template -a "src=$(pwd)/inventory.gcp_compute.template.yml dest=$(pwd)/inventory.gcp_compute.yml" -e "GCP_PROJECT=$TF_VAR_gcp_project"

ansible-playbook -i inventory.gcp_compute.yml playbook.yml -e "state=present"
```
6. Observe that ansible will provide a detailed breakdown of how long each task took to execute. This is useful information for figuring out where to start optimising performance.  

One possible source of performance optimisations is in the fact gathering that happens implicitly on each play by default. It is possible to disable fact gathering altogether from within your playbook if you do not need it, but you are using the facts to template the nginx.conf file. Instead, you will configure *fact caching* to enable reuse of these values.  

7. Switch back to the terraform directory and destroy the resources:
```shell
cd ~/Labs/ANS04/terraform
terraform destroy
```

8. Redeploy the resources with terraform:
```shell
terraform apply
```

##### Enable caching

9. Switch back into the ansible directory. Edit the **ansible.cfg** file:
```ini
[defaults]
  remote_user=ansible
  private_key_file=~/ansible_key
  callbacks_enabled = timer, profile_tasks, profile_roles
  fact_caching = jsonfile # <- add this and next three lines
  fact_caching_prefix = ansible_facts_
  fact_caching_timeout = 3600
  fact_caching_connection = facts.d

[ssh_connection]
  ssh_args="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null"

[inventory] # <- add this section
  cache = true
  cache_plugin = jsonfile
  cache_timeout = 3600
  cache_connection = inventory.d
```
These changes have enabled two kinds of caching. _Fact caching_, will reduce the amount of time spent gathering facts during playbook execution. _Inventory caching_ will prevent ansible from having to regenerate the inventory via the plugin on every run. 

10. Execute the playbook:
```shell
ansible-playbook -i inventory.gcp_compute.yml playbook.yml -e "state=present"
```
11. Review the generated cache files to see the information that Ansible has stored

##### Exploiting Caching
The first run of the playbook with caching enabled will, if anything, probably have been a little slower, as Ansible has to write the data to the cache. It is on subsequent executions that you will see the benefit.  

12. Execute the playbook again, but this time set the state to absent, to uninstall packages:
```bash
ansible-playbook -i inventory.gcp_compute.yml playbook.yml -e "state=absent"
```
You should notice faster execution.  

13. To prove that the speedup was not simply down to uninstalling being faster than installing, edit the **playbook.yml** and change the _install_dir_ variable value, to force ansible to re-clone the repo. Then re-run the playbook with state=present:
```bash
ansible-playbook -i inventory.gcp_compute.yml playbook.yml -e "state=present"
```

##### Optimising SSH
Another source of performance issues can be the time taken to establish SSH connections. You have already somewhat reduced this by disabling host key checking. But you can optimise the SSH configuration further. 

14. Re-execute the playbook with `state=absent` to uninstall packages

15. Before re-invoking the playbook, edit **ansible.cfg**, like so:
```ini
[defaults]
  remote_user=ansible
  private_key_file=~/ansible_key
  callbacks_enabled = timer, profile_tasks, profile_roles
  fact_caching = jsonfile
  fact_caching_prefix = ansible_facts_
  fact_caching_timeout = 3600
  fact_caching_connection = facts.d

[ssh_connection]
  ssh_args = "-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ControlMaster=auto -o ControlPersist=90s"
   # <- add extra arguments to above line
  pipelining = True # <- add this line

[inventory] # <- add this section
  cache = true
  cache_plugin = jsonfile
  cache_timeout = 3600
  cache_connection = inventory.d
```
The additional ssh connection settings will cause connections to be left open for longer, allowing them to be reused across plays. Pipelining will make background operations more efficient by reducing the number of connection operations required to execute a module on a remote server. 

16. Edit the _install_dir_ again, then re-invoke the playbook with **state=present** and see if you observe a noticeable difference in performance:
```shell
ansible-playbook -i inventory.gcp_compute.yml playbook.yml -e "state=present"
```

##### Clean Up
17. Before moving on, destroy any resources:
```bash
cd ~/Labs/ANS04/terraform
terraform destroy
```
## ANS05
### Lab ANS05 - Secret Management With Ansible-Vault

#### Objective
Securely store and retrieve sensitive data using ansible-vault

#### Outcomes
By the end of this lab, you will have:
* Created a vault file to securely store variables
* Retrieved data from a vault during playbook execution

#### High-Level Steps
* Deploy a sample app that requires authentication
* Use ansible to make an authenticated request to the app
* Store the credentials in a vault file
* Reconfigure the playbook to retrieve the credentials from the vault file

#### Detailed Steps
##### Deploy a Sample App
1. Ensure that the sample API is running - this is the same sample API you worked with previously:
```bash
sudo ss -tap | grep 5000 || sudo sh -c "docker compose -f ~/Labs/PY05/compose.yml up -d --build"
```
Note: this path may be incorrect. Try `/home/qa/Labs/PY05/compose.yml`

2. Switch into the ANS05 directory and review the provided playbook:
```bash
cd ~/Labs/ANS05
```
```yaml
---
- hosts: localhost
  connection: local
  name: Use Credentials
  tasks:
  - name: Make API Call
    uri:
      url: "http://localhost:5000/auth/tokens"
      method: "POST"
      url_username: "learner"
      url_password: "p@ssword"
      return_content: true
    register: result
  
  - name: print info
    debug:
      msg: "{{ result.content }}"
```
3. Execute the playbook:
```bash
ansible-playbook playbook.yml
```
4. You should see in the output a generated token, something like:
```
97506f8a1816434b5291a349f0dd5bd4574962ebf82f66505bccc87baf257ac3
```

##### Secure the Credential
Having a hardcoded password in the playbook like this is a problem, especially if you want to share that playbook with others. Alternatively, simply passing the value as a variable on the command line is not an ideal solution either, as this leaves the sensitive credential potentially exposed via command history. Instead, a better approach would be to use _ansible-vault_ to encrypt the data at rest, and retrieve it during playbook execution. 

5. Create a new vault file:
```bash
ansible-vault create vault.yml
```
6. Once you have set a password on the vault file itself, you will be presented with an editor. Add the following content:
```yaml
password: "p@ssword"
```
7. Then save and quit the editor. You now have a new vault file. Attempt to cat the contents:
```bash
cat vault.yml
```
8. You should see output similar to:
```
$ANSIBLE_VAULT;1.1;AES256
33313334323633626365616266313161636134343635313038396162666533376665666562323164
6361303938643739383338663631623538303933356630360a366666366661653866616537643761
66623737316632366435613435393666306661303536333236643335333062633063323531623533
3462653266643330370a656531326535616439633637666164376630646531366138623335663437
39333034343132326634376363363934323762316633393430383237363832626639
```
Demonstrating that the vault file has been encrypted.

##### Update the Playbook
9. Edit **playbook.yml** so that the contents are as follows:
```yaml
---
- hosts: localhost
  connection: local
  name: Use Credentials
  vars_files: # <- add this line
  - vault.yml # <- and this line
  tasks:
  - name: Make API Call
    uri:
      url: "http://localhost:5000/auth/tokens"
      method: "POST"
      url_username: "learner"
      url_password: "{{ password }}" # <- edit this line to reference the password variable
      return_content: true
    register: result
  
  - name: print info
    debug:
      msg: "{{ result.content }}"
```
10. Now re-run the playbook, but this time add the `-J` flag, which instructs ansible to prompt for the vault password:
```bash
ansible-playbook playbook.yml -J
```
You should again expect to see a token returned, if the request was successful.

##### Stretch Task
By consulting the [documentation](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html) for the uri module, and recalling how you interacted with the API previously, add extra tasks to the playbook which use the token received from the initial request to create, update and delete objects through the API. See the solution below if needed.  

<details>
<summary>Stretch Task Solution - POST /api/book</summary>

```yaml
---
- hosts: localhost
  connection: local
  name: Use Credentials
  vars_files: 
  - vault.yml
  tasks:
  - name: Make API Call
    uri:
      url: "http://localhost:5000/auth/tokens"
      method: "POST"
      url_username: "learner"
      url_password: "{{ password }}" 
      return_content: true
    register: result
  - name: Add book
    uri:
      url: "http://localhost:5000/api/books"
      method: "POST"
      headers:
        Authorization: "Bearer {{ result.content }}"
      body_format: json
      body:
        title: "Example"
        author: "John Smith"
        genre: "scifi"
        id: "0000012345"
      return_content: true
    register: result2
  - name: print info
    debug:
      msg: "{{ result2 }}"
```
Other requests to other endpoints will be similar

</details>

##### Tidy Up
- Stop the sample API:
```bash
sudo ss -tap | grep 5000 || sudo sh -c "docker compose -f ~/Labs/PY05/compose.yml down"
```
Note: this path may be incorrect. Try `/home/qa/Labs/PY05/compose.yml`

## ANS06
### Lab ANS06 - Introduction to AWX

#### Objective
Create a job in AWX to manage scheduled ansible executions

#### Outcomes
By the end of this lab, you will have:
* Deployed an AWX cluster
* Configured credentials in AWX
* Configured an AWX job to run scheduled maintenance activities

#### High-Level Steps
* Deploy AWX
* Add an SSH key as a credential to AWX
* Create and run an AWX job

#### Detailed Steps
##### Deploy Resources
1. In your terminal, switch to the ANS06 directory: `cd ~/Labs/ANS06`

2. Initialise Terraform and apply the provided resource configuration:
```bash
terraform init
terraform apply -auto-approve
``` 
This will provision the instances which AWX will configure.  

##### Deploy AWX
3. For performance reasons, you will run AWX on a local VM using Hyper-V. Launch Hyper-V and start the AWX VM.

4. Connect to the VM. The username and password are both 'qa'. Make a note of the VM's IP (run `ip addr show eth0 | grep "inet "`), and run the provided install_awx_kind.sh script:
```bash
./install_awx_kind.sh
```
5. The AWX init script takes several minutes to run, after which AWX will need another several minutes to fully initialise. Take the time to review the [explanation](#the-awx-init-script-explained) of what the script is actually doing

6. Navigate to `http://<awx_vm_ip>:30080` in a new browser tab. If AWX is still configuring, you may see connection refused or an internal server error - wait until the page reloads

7. Once AWX is finally ready, log in with the following credentials:
    * username: admin
    * password: ChangeMe123!

You should now see the AWX dashboard.

##### Create an AWX Job
1. In the AWX dashboard, create a new organization:
    * Click on Organizations under Access from the side pane
    * Click Add to Create New Organization
    * Name: enter `BOAAWX`
    * Click on Save

2. Return to the AWX dashboard and select Resources > Projects > Add

3. Configure the project as follows:
    * name: site-sync
    * Organizations as `BOAAWX` 
    * Source Control Type: `Git` 
    * Source control URL: https://github.com/qa-tech-training/sample-awx-project 
    * Save

##### Add SSH Credentials
To be able to connect to your machines, AWX will need access to the private SSH key that corresponds to the public key used to build the infrastructure.

1. Navigate to Resources > Credentials, click 'Add'
2. Configure the new credential as follows:
    * name: ansible_ssh_key
    * organization: BOAAWX
    * credential type: machine
    * username: ansible
    * SSH Private Key: copy and paste in the material from ~/ansible_key
    * privilege escalation method: sudo
    * privilege escalation password: leave blank
3. Save the credential

##### Add an Inventory
1. Navigate to Resources > Inventories, click 'Add'
2. Name the inventory 'webservers', and associate it to the BOAAWX organization, and Save

You will keep things simple with a static inventory for now, but this could be dynamic via an inventory source

3. Click on Hosts.
4. Add a host by clicking 'Add'. Enter the IP of one of your app servers as the name and choose `webservers` as the Inventory.
5. Repeat for the second app server and your proxy server.
6. Once you have added all your hosts, you need to group them, following the pattern gcp_role_<role>. From Inventories -> webservers, click Groups. Add 2 groups: `gcp_role_appserver` and `gcp_role_proxy`. 
7. Click on each Host and click Groups > Add, and select the corresponding group based on its IP.

##### Create a Job Template
1. Navigate to Resources > Templates, click 'Add', 'Add Job Template'.
2. Configure the following:
    * NAME: Deploy Site
    * Description : Ensure Site is Deployed
    * JOB TYPE: Run 
    * INVENTORY: webservers
    * PROJECT: site-sync
    * PLAYBOOK: ansible/playbook.yml
    * CREDENTIALS: ansible_ssh_key
    * VARIABLES:
    ```yaml
    repository_url: https://github.com/qa-tech-training/sample-awx-project
    ```
3. Save the template configuration, then `Launch` the job manually to test connectivity

##### Create a Schedule
Manually triggering job executions is not the preferred way to run AWX jobs, as it somewhat defeats the point of automation. AWX is excellent for scheduling jobs, to be run at specific times.
1. Select your job template, edit it and select `schedules`
2. Configure the schedule so that the job runs once per day 

###### The AWX Init Script Explained
The primary distribution mechanism for AWX is as a Kubernetes operator. Detailed understanding of Kubernetes is beyond the scope of this course, but in short it is the de-facto standard orchestration platform for containerised workloads. Running AWX through Kubernetes allows for highly available, scalable deployments of the workloads needed to execute AWX jobs. To set up AWX, the init script does the following:
* installs and configures _docker_, a common container management tool
* installs **K**ubernetes-**in**-**D**ocker (KinD), a tool for running a Kubernetes cluster as a set of containers
* Creates a KinD cluster with appropriate ports mapped
* Deploys the AWX operator and associated resources into the KinD cluster
[back to instructions](#deploy-awx)

## ANS07
### Lab ANS07 - Configuring AWX to Work With Hashicorp Vault

#### Objective
Deploy Hashicorp Vault and use it to store credentials

#### Outcomes
By the end of this lab, you will have:
* Deployed hashicorp vault in development mode
* Created a Vault secret
* Configured AWX to retrieve a secret from a vault

#### High-Level Steps
* Deploy Hashicorp vault
* Move an SSH key into vault
* Reconfigure AWX jobs to read credentials from vault

#### Detailed Steps
##### Deploy Vault
1. In WSL, switch into the ANS07 directory, and run the following to deploy a vault server:
```bash
cd ~/Labs/ANS07
terraform init
terraform apply -auto-approve
```
2. Make a note of the output `vault_ip` value, and also the root token that this vault installation has been deployed with: `example-vault-token-1234`. You will use these in the next step.

##### Store a Credential
Let's store your first credential in vault. You will start by storing the private SSH key that you have been using for ansible jobs. 

3. Run the following in your WSL terminal, *making sure to fill in your vault server IP*:
```bash
export VAULT=<your vault IP>
export VAULT_TOKEN=example-vault-token-1234
cd ~/Labs/ANS07
./generate_post_data.py
curl \
    -H "X-Vault-Token: $VAULT_TOKEN" \
    -H "Content-Type: application/json" \
    -XPOST \
    -d@data.json \
    http://$VAULT:8200/v1/secret/data/ansible-ssh-key
```
4. Verify the credential creation:
```bash
curl \
    -H "X-Vault-Token: $VAULT_TOKEN" \
    http://$VAULT:8200/v1/secret/data/ansible-ssh-key > secret.json
cat secret.json
```

##### Configure AWX to Retrieve Credentials from Vault
1. Return to your AWX dashboard and navigate to the credentials overview.
2. Create a new credential with the following configuration:
    * Name: `vault_credential`
    * Credential Type: `HashiCorp Vault Secret Lookup`
    * Server URL: `http://<your vault server IP>:8200`
    * Token: `example-vault-token-1234`
    * API version: `v1`
3. Save this credential and return to the credentials overview
4. Edit the configuration for the credential you created earlier:
    * Replace the existing key material
    * Use the `key icon` next to the input field to configure an external source
    * Use the `vault_credential` you just created
    * Set the Path to Secret `/secret/data/ansible-ssh-key`
    * Set the Key Name as `sshkey`
    * OK
    * Save

5. Return to the job template you defined earlier and trigger a new execution, to test the connectivity with the key now pulled from vault.

### Optional Stretch Lab
* In Hyper-V, start the 3 Centos VMs
* Generate a new SSH key pair, and:
  * place the _public key_ material in the authorized_keys file (`/home/qa/.ssh/authorized_keys`) on each of the centos VMs
  * store the _private key_ material as a new vault credential, and create a new AWX credential with the username 'qa', privilege escalation method 'sudo', privilege escalation password 'qa', and your new vault credential as its source
* Create a Github Account if you do not already have one, and sign in
* fork the https://github.com/qa-tech-training/sample-awx-project repo. Update the tasks for the _common_ role to work on centos instead of ubuntu. (hint: see documentation for the ansible.builtin.yum module)
* Add a new AWX project which uses _your fork_ of the sample repo as a source
* add a new AWX inventory with the hostnames of the three centos VMs. Create groups gcp_role_appserver and gcp_role_proxy, allocating one of the VMs as the proxy and the other two as app servers
* Create a new job definition to run the playbook against the centos VMs. If successful, the job when run should deploy the same sample website onto the centos VMs

##### Tidy Up:
- In `~/Labs/ANS07` use **terraform destroy** to deprovision the vault VM
- In `~/Labs/ANS06` use **terraform destroy** to deprovision the 2 appservers and proxy server plus supporting network resources
- Turn off the AWX Hyper-V machine

## PY09
### Lab PY09 - Fundamentals of Testing Python Applications

#### Objective
Implement automated test suites for Python code

#### Outcomes
By the end of this lab, you will have:
* Implemented documentation testing using doctest
* Implemented unit tests using unittest and pytest
* Implemented _patching_ of functions

#### High-Level Steps

#### Detailed Steps
1. In the VS Code Terminal, switch directory into PY09:
```bash
cd ~/Labs/PY09
```
Expand this directory in the VSCode explorer.  

2. Create and initialise a new virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Open **calculator.py** and review the contents. This builds upon the solution to Lab PY03 and adds two extra functions: _calculate_original_ and _calc_input_vat_.

4. You will implement several key testing strategies in this lab, the first being _documentation testing_. It is essential the documentation is kept up-to-date.

5. Review the docstring for the _calculate_total_ function. Note the following sections:
```
    >>> calculate_total(100, 20)
    120.0
    >>> calculate_total(10, 50)
    15.0
```
These are usage examples which will be included in any generated documentation. Documentation testing ensures these usage examples work and give the expected results. 

6. Add the following to **test_calculator.py**:
```python
import calculator
import doctest

def test_docs():
    doctest.testmod(calculator)

if __name__ == '__main__':
    test_docs()
```
7. Make the executable and then execute the test script:
```bash
chmod +x ./test_calculator.py
./test_calculator.py
```
Expect no output. By default, doctest takes the approach of "no news is good news".

8. Doctest can be made more chatty by adding the `-v` (verbose) flag:
```bash
./test_calculator.py -v
```
9. Things to try before moving on:
   * Change the usage examples in the existing docstring and observe the resulting failure
   * Add a docstring, with usage examples, for the _calculate_original()_ function, and re-run the test script

##### Implementing Unit Tests
Whilst documentation testing is a good form of _sanity testing_, it tests the correctness of your documentation rather than testing your code conforms to requirements. For this, you need additional forms of _functional testing_. The simplest form of testing is _unit testing_.

10. In your **test_calculator.py** script, add the following in addition to the existing content:
```python
import unittest
class TestVatCalc(unittest.TestCase):
    def test_calculate_total(self):
        self.assertEqual(calculator.calculate_total(200, 20), 240.0)
```
Add the following to the _main_ block:
```python
unittest.main()
```
The built-in `unittest` library provides a base class for test cases. Any class inheriting from this base class will have all methods prefixed with `test_` collected and executed by unittest.main(). 

11. Execute the test script and observe the additional test output:
```bash
./test_calculator.py # omitting the -v flag will suppress doctest output and make unittest output more obvious.
```
12. Things to try before moving on:
    * Add additional test cases for the calculate_total function to the existing test class
    * Add another test class with test cases for the calculate_original function

##### Introducing PyTest
Whilst the builtin `unittest` library provides everything necessary to implement unit testing for your code, it does require the boilerplate of creating test case classes. It also does not provide many options for exporting detailed test results. To improve the testing experience, the `PyTest` library was created as a general test orchestrator.

13. Install pytest and pytest-cov into your venv:
```bash
venv/bin/pip3 install -r requirements.txt # these packages have been provided as a requirements file for convenience
```
14. Add the following to your test script:
```python
def test_vat_calc_calculate_total():
    assert calculator.calculate_total(30, 15) == 34.5
    assert calculator.calculate_total(75, 50) == 112.5
```
15. Use pytest to collect and execute the tests in the test script:
```bash
venv/bin/python3 -m pytest
```
Observe that pytest gives a much more helpful breakdown of the test results. Pytest can also optionally report on _coverage_ - i.e. the percentage of the code which has been tested. 

16. Re-run pytest with coverage reporting enabled for the calculator module:
```bash
venv/bin/python3 -m pytest --cov=calculator
```
17. On the topic of coverage, pytest can also export coverage reports in a variety of formats. Export the coverage for your tests as an HTML document:
```bash
venv/bin/python3 -m pytest --cov=calculator --cov-report=html
```
Review the coverage report by opening htmlcov/index in a browser. In the Windows Host machine open File Explorer. Expand Linux -> Ubuntu -> home -> qa -> Labs -> PY09 -> htmlcov -> index.html

Right-click and Open with Google Chrome.


18. Things to try before moving on:
    * Refactor your existing tests to be defined as pytest functions, without test classes
    * Experiment with other available coverage report output formats (xml, json and markdown, might be good examples)

##### Mocking External Dependencies
As the name suggests, the point of a unit test is to test a single unit of code (i.e. a function) in isolation. A way is needed, therefore, to _mock_ external dependencies (inputs or sources of data) during unit tests to isolate the logic of just the function under test. 

19. In **calculator.py**, review the second of the two extra functions, _calc_input_vat_. This function takes in user input, and therefore has an external dependency on the user.  

You can break this dependency during testing by _patching_ the input function to return a specific string. Thus for each test you can have a predictable input that you can make assertions against, without requiring a user to submit that input.

20. Add the following to the test script:
```python
from unittest.mock import patch

def test_calc_input():
    with patch('calculator.input') as inp:
        inp.return_value = "100@20"
        assert calculator.calc_input_vat() == 120.0
```
21. Re-run your tests with pytest.
22. Things to try before moving on:
    * Add additional test cases for different patched inputs
    * Add a test to confirm that the _calc_input_vat_ function raises a ValueError exception if it cannot parse the input values as ints (hint: look into the usage of the `pytest.raises()` function)

#### Optional Stretch Tasks
* Write unit tests for the `validate_pod()` function from Lab PY04. Aim for as close to 100% coverage as possible

## PY10
### Lab PY10 - Performance Benchmarking With Timeit

#### Objective
Profile the performance of Python scripts with `timeit`

#### Outcomes
By the end of this lab, you will have:
* Used timeit to implement performance benchmarking
* Quantitatively compared the execution time of sync vs async code

#### High-Level Steps
* Benchmark a single execution of synchronous code
* Determine average execution time
* Comparative benchmark of sync vs async code

#### Detailed Steps
1. This lab requires the sample API from earlier. Ensure that it is running:
```bash
cd ~/Labs/PY05
docker compose -f compose.yml up -d --build
```
2. Switch into the PY10 directory, create and activate a new venv, and populate the sample data:
```bash
cd ~/Labs/PY10
python3 -m venv venv
source venv/bin/activate
venv/bin/pip3 install -r requirements.txt
chmod +x ./populate_data.py
./populate_data.py
```
Review the code in **sync_client.py** and **async_client.py**. It is essentially the same sync/async code you worked with in Lab PY07.

3. You will use the `timeit` library to profile the performance of your code. Performance profiling is a common form of _non-functional_ testing. Code that works but is slow is generally considered bad code.

4. Add the following to `benchmark.py`:
```python
import timeit

def test_sync():
    result = timeit.timeit('sync.main()', setup='import sync_client as sync', number=1)
    return result

if __name__ == '__main__':
    time_sync = test_sync()
    print(f"Execution time (synchronous): {time_sync}")
```
Make the file executable and then run the script:

```bash
chmod +x ./benchmark.py
./benchmark.py
```
You should see a result of approx. 10 seconds.

5. Here you have used the `timeit` method, with one execution, to execute the sync code exactly once and return the execution time. In reality, you would want a proper benchmark to include multiple executions, to enable you to determine an average execution time.

6. Amend the benchmark code to use the `timeit.repeat()` method to run a total of 25 executions, and return the average execution time. Try this yourself, and see the solution below _if needed_.  

<details>
<summary>Solution - Multiple Executions</summary>

The `timeit.repeat()` method offers a reliable way to run multiple executions, in batches, repeating the setup for each batch. This ensures that if the setup code itself is time-consuming you are able to factor it in without skewing the performance profile. Using `timeit.repeat()`, your benchmark code should now look like:
```python
#! venv/bin/python3
import timeit

def test_sync():
    results = timeit.repeat('sync.main()', setup='import sync_client as sync', repeat=5, number=5)
    avg_sync_time = sum(results) / 25
    return avg_sync_time

if __name__ == '__main__':
    avg_time_sync = test_sync()
    print(f"Execution time (synchronous): {avg_time_sync}")
```
</details>

#### Comparing Sync and Async Code
7. When introducing async code in Lab PY07, you qualitatively compared the performance of the sync and async client code. You can now make that comparison quantitatively. Add another function to your benchmark script, `test_async()`, which uses `timeit.repeat()` to run 25 executions of the async code:  

```python
def test_async():
    results = timeit.repeat('asyncio.run(asyn.main())', setup='import async_client as asyn\nimport asyncio', repeat=5, number=5)
    avg_async_time = sum(results) / 25
    return avg_async_time
```

8. Add code to the _main_ block to call your `test_async()` function and output the result:
```python
if __name__ == '__main__':
    avg_time_sync = test_sync()
    avg_time_async = test_async()
    print(f"Average execution time (synchronous): {avg_time_sync}")
    print(f"Average execution time (asynchronous): {avg_time_async}")
```

9. Re-run your benchmark and compare the performance of the sync and async implementations.

#### Optional Stretch Tasks
* Benchmark your `validate_pod()` function from Lab PY04

## PY11
### Lab PY11 - Custom Ansible Module Development

#### Objective
Develop, document, test, install and use a custom Ansible module which interacts with a RESTful API

#### Outcomes
By the end of this lab, you will have:
* Developed a custom ansible module
* Added documentation to your module
* Implemented unit testing for your module
* Installed and used your module in a playbook

#### High-Level Steps
* Set up Ansible dev environment
* Develop module code
* Implement unit tests
* Document your module
* Deploy the sample API
* Use your module in a playbook

#### Detailed Steps
##### Setting Up the Dev Environment
1. This lab will require, amongst other things, the ansible test utility to execute tests against your code. This is not included when ansible is installed via apt. You will need to instead set up a virtual environment with ansible installed:
```bash
cd ~
python3 -m venv ansible-venv
ansible-venv/bin/pip3 install ansible pytest pytest-cov pytest-xdist requests

alias "ansible-test"="/home/qa/ansible-venv/bin/python3 -m ansible test"
echo !! | tee -a ~/.bashrc
```
You have also created an alias to run the ansible test command and added the alias to your bash profile.

2. You will also need a very particular file structure for your module development activities:
```bash
mkdir -p ~/ansible_collections/custom
cd ~/ansible_collections
ansible-galaxy collection init custom.bankx
mkdir custom/bankx/plugins/modules
mkdir -p custom/bankx/tests/unit
```

3. Open the `ansible_collections/custom/bankx` directory in VS Code, as this is where you will do most of your work.

##### Develop the Custom Module
4. Create a new file in `plugins/modules` called **sandbox.py**, and add the following:
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import re
import requests
from uuid import uuid4

class APIClient():
    def __init__(self, module):
        self.module = module
        self.base_url = module.params['api_endpoint']
        self.token = module.params['api_token']
    
    def make_request(self, uri_path, method, data=None):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "If-Match": self.module.params.get("resource_version", "")
        }

        data = dict(
            name = self.module.params['name'],
            owner_email = self.module.params['owner_email'],
            size = self.module.params["size"],
            ttl_days = self.module.params["ttl_days"],
            allowed_cidrs = self.module.params["allowed_cidrs"],
            id = str(uuid4())
        )    

        url = self.base_url + ('' if uri_path.startswith('/') else '/') + uri_path
        try:
            if method == "PATCH":
                response = requests.patch(url, json=data, headers=headers)
            elif method == "POST":
                response = requests.post(url, json=data, headers=headers)
            elif method == "DELETE":
                response = requests.delete(url, json=data, headers=headers)
            elif method == "GET":
                response = requests.get(url, json=data, headers=headers)
        except Exception as e:
            self.module.fail_json(
                msg=str(e)
            )

        if response.status_code and response.status_code >= 400:
            self.module.fail_json(msg="API failure", **response.json())

        return response.json(), response.status_code

def main():
    module_args = dict(
        api_endpoint = dict(type=str, required=True),
        api_token = dict(type=str, required=True),
        name = dict(type=str, required=True), 
        owner_email = dict(type=str, required=True),
        size = dict(type=str, required=True),
        ttl_days = dict(type=int, required=True),
        allowed_cidrs = dict(type=list[str], required=True),
        resource_version = dict(type=str, required=False),
        state = dict(type=str, required=True, choices=['present', 'absent']),
        sandbox_id = dict(type=str, required=False)
    )
    
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    client = APIClient(module)

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    if module.params.get("state") == "present":
        _id = module.params.get("sandbox_id", "")
        if _id:
            response, code = client.make_request(f"/v1/sandboxes/{_id}", "PATCH")
        else:
            response, code = client.make_request("/v1/sandboxes", "POST")
        if code == 200:
            result["msg"] = "Sandbox configuration already up-to-date"
            result["original_message"] = response
            module.exit_json(**result)
        elif code == 202:
            _id = response.get("sandbox_id")
            ops, code = client.make_request(f"/v1/operations/{_id}", "GET")
            result["changed"] = True
            result["original_message"] = response
            result["msg"] = ops
            module.exit_json(**result)

    if module.params.get("state") == "absent":
        _id = module.params.get("sandbox_id", "")
        response, code = client.make_request(f"/v1/sandboxes/{_id}", "DELETE")
        if code == 200:
            result["msg"] = "Sandbox already deleted"
            result["original_message"] = response
            module.exit_json(**result)
        elif code == 202:
            result["changed"] = True
            result["original_message"] = response
            result["msg"] = f"sandbox deleted"
            module.exit_json(**result)
        
def validate_input(module):
    email = module.params["email"]
    valid_email = re.compile("^[a-zA-Z0-9._-]+@[a-zA-Z0-9_.-]+.[a-z]{2,3}$")
    valid_cidr = re.compile("^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-9]{1,2}$")
    if not valid_email.match(email):
        module.fail_json(
            msg="Provided email does not match regular expression ^[a-zA-Z0-9._-]+@[a-zA-Z0-9_.-]+.[a-z]{2,3}$"
        )
    if not 0 < module.params['ttl_days'] <= 30:
        module.fail_json(
            msg="ttl_days must be between 1 and 30"
        )
    for cidr in module.params['allowed_cidrs']:
        if not valid_cidr.match(cidr):
            module.fail_json(
                msg=f"invalid cidr range in allowed_cidrs: {cidr}"
            )

if __name__ == '__main__':
    main()
```
This is quite a lengthy bit of code, but there are really only three main parts:
```python
class APIClient():
    ...
```
The `APIClient` class is a utility class which is handling marshalling the provided object spec into a JSON object and making a request to the API server.  

```python
def main():
    ...
```
The `main` function is where your Ansible-module specific logic lives. This is defining the schema of the arguments for this module, initialising the module and API client, and using the API client to make the necessary requests to the API.  

```python
def validate_input(module):
    ...
```
The `validate_input` function is an optional helper function which is being used to ensure that the ansible module will impose restrictions on its parameters that match those enforced on the API side by the API server itself. Make sure to read the code and understand the logic as fully as possible before moving on.

##### Testing the Module
5. Now that you have the module code, it is time to implement some tests. Create a new file in the `tests/unit` directory, called **test_sandbox.py**, and add the following:
```python
import plugins.modules.sandbox
from unittest.mock import MagicMock, patch

def test_api_post():
    mock_module = MagicMock()
    mock_module.params = {
        "api_endpoint": "http://localhost:8000",
        "api_token": "foobarbaz",
        "name": "foo",
        "owner_email": "bar@baz.com",
        "size": "small",
        "ttl_days": 30,
        "allowed_cidrs": ["0.0.0.0/0"]
    }

    def mock_post(url, json, headers):
        response = MagicMock()
        response.status_code=202
        response.json.return_value=json
        return response

    with patch('plugins.modules.sandbox.requests') as requests:
        requests.post = mock_post
        client = plugins.modules.sandbox.APIClient(mock_module)
        response = client.make_request("/sandboxes", "POST") 
        assert response[1] == 202
        assert response[0]["name"] == "foo"
        assert response[0]["id"]
```
Explanation: You first import the sandbox module you just created, as well as some key utilities from unittest: `patch`, which you have already seen, and `MagicMock`, a base class for creating mock objects.  

In the `test_api_post` test, you create a MagicMock object to mock the module that needs to be passed to the API client, setting a params field holding a dictionary containing sample data. You also define a function which simulates the behaviour of a post request: `mock_post`, returning a mock object with a status code of 202 and whatever JSON was passed to the function.  

Finally, you patch the requests module, replacing `requests.post` with your own _mock_ function. You then initialise an API client, call the `make_request` function with the `POST` method, and make the following assertions:
  * You receive a 202 ACCEPTED status code
  * The returned JSON has the name that you supplied in your dummy data
  * The returned JSON has a non-empty ID

6. Run the test:
```bash
cd ~/ansible_collections/custom/bankx
ansible-test units
```
You should see successful test execution.

7. Now that you have this example to refer to, try to implement additional test cases for other request methods, and for the `validate_input` function.

##### Document the Module
8. To add documentation to your module, add a documentation string to the **sandbox.py** file. The format is a little different to the docstrings you have seen previously. This is to enable it to be parsed by `ansible-doc`.

9. Add the following near the start of the **sandbox.py** file:
```python
DOCUMENTATION = r'''
module: custom.bankx.sandbox
description: provision development sandboxes via the internal sanbox api
parameters:
  api-endpoint: 
    type: string
    description: the host + port of the API server
  api-token: 
    type: string
    description: bearer token for the API server 
'''
```
Complete the documentation for the remaining parameters. Refer to the schema defined in `main()`, if you need.

##### Install the module
10. You can install the module, making it globally available to ansible, using the `ansible-galaxy` utility:
```bash
cd ~/ansible_collections/custom/bankx
ansible-galaxy collection install .
```

11. Once the module is installed, review the documentation you created:
```bash
ansible-doc custom.bankx.sandbox
```

##### Deploy the API
12. Switch into the `PY11` directory, which has the source files for the sample API. Add a tokens file, **valid_tokens.json**, with the following contents:
```json
[
    {"token": "byy27wsb0gjeodps2kd0re9d.71j0gx1", "scopes": ["sandboxes:list"]}, 
    {"token": "q6zn6o28056ia3hfesl0j4be7p16wcgw", "scopes": ["sandboxes:list", "sandboxes:create", "operations:list"]}, 
    {"token": "0r61bm74t1jiymxnq3qqf2pwvplkj13a", "scopes": ["sandboxes:list", "sandboxes:create", "sandboxes:delete", "operations:list"]},
    {"token": "ro5b64n4kehaurbuofkfbmnrhvxn0.yk", "scopes": ["sandboxes:list"]},
    {"token": "mpzn3oqk3ymaijybadhcssh5nf.mpri0", "scopes": ["sandboxes:list", "operations:list"]},
    {"token": "5vgud9glj60q1xrd.uicpjru.xxr8jhd", "scopes": ["sandboxes:list", "sandboxes:create", "sandboxes:update", "sandboxes:delete", "operations:list"]},
    {"token": "9nvd5y5.jlyh1e93zmo50nk3wpynxin.", "scopes": ["sandboxes:create", "operations:list", "sandboxes:delete"]},
    {"token": "4bvnx.c02koyvujjwsn7dan.iw0ow9ej", "scopes": ["sandboxes:list", "sandboxes:update", "operations:list"]},
    {"token": "jtl.pmxmkvsrnu87m0eywx0vms4u8iv2", "scopes": ["sandboxes:list"]},
    {"token": "4ryebmgw3q0hdv1ksgr.2rb0f6dvr2j2", "scopes": ["sandboxes:list"]}
]
```

13. Deploy the API server:
```bash
docker compose -f compose.yml build
docker run -d -p 8000:8000 -v ./valid_tokens.json:/opt/app/valid_tokens.json bankx-sandbox-api:latest
```

14. Create a playbook, **playbook.yml**, which uses your new module:
```yaml
---
- name: Deploy sandbox
  hosts: localhost
  tasks:
  - name: create sandbox
    custom.bankx.sandbox:
      api_token: "5vgud9glj60q1xrd.uicpjru.xxr8jhd"
      api_endpoint: "http://127.0.0.1:8000"
      name: "team-alpha-sbx"
      owner_email: "team-alpha@bankx.com"
      size: "small"
      ttl_days: 30
      allowed_cidrs: ["0.0.0.0/0"]
      state: "present"
    register: out
  - name: dump output
    debug:
      msg: '{{ out }}'
```

15. Run the playbook:
```bash
ansible-playbook playbook.yml
```

#### Optional Stretch Tasks
* Experiment with changing the playbook configuration to verify update and delete functionality
* Create an ansible-vault to store your API token, rather than hard-coding it into the playbook
* Use terraform to provision a cloud server running the sample API, and update your playbook to talk to the remote server

## Bibliography

### Python
- [Python stdlib docs](https://docs.python.org/3/library/)
- [PEP8 - Python coding conventions](https://peps.python.org/pep-0008/)
- [Pip - index of external libraries](https://pypi.org/)

### Terraform
- [Main Terraform docs](https://developer.hashicorp.com/terraform)
- [Terraform Registry](https://registry.terraform.io/)
- [Provider docs - Azure](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Provider docs - AWS](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Provider docs - GCP](https://registry.terraform.io/providers/hashicorp/google/latest/docs)

### Ansible
- [Ansible docs](https://docs.ansible.com/)
- [RedHat AAP](https://docs.ansible.com/platform.html)
- [The AWX Project](https://ansible.readthedocs.io/projects/awx/en/latest/)
- [Misc. additional resources](https://github.com/ansible-community/awesome-ansible)

### Extra Resources
- [Killercoda](https://killercoda.com) - an excellent lab platform for getting further practice with many tools, including several of those used in this course