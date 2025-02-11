# Simple CMD Shell Program

## Introduction
A simple menu-driven command-line shell program written in Python that replicates basic Windows CMD commands. The program supports common operations like:
- Creating directories (mkdir)
- Changing directories (cd)
- Listing directory contents (dir)
- Displaying messages (echo)
- Viewing file contents (type)

## Prerequisites
- **Python 3.10 or above**: The program was written in Python 3.12.1, but it is compatible with Python 3.10 or newer.
- No additional libraries are required as it uses Python's built-in functionality.

## Installation
1. Clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/Nemesis-12/simple-cmd-shell.git
   ```
   
2. Navigate to the directory containing the script:

   ```console
   cd simple-cmd-shell
   ```

## Usage
Run the program in the terminal or an IDE:

```console
python shell.py
```

## Example

Upon running the program, you will see a menu of available commands. Select an option by typing the corresponding command. Below are a few examples to get you started.

```console
Select an action to perform
[dir]   List Current Directory
[cd]    Change Directory
[mkdir]	Create New Directory
[echo]  Display Message
[type] 	Concatenate and Display File Content
[q] 	Exit

>
```

### List current directory

```console
> dir
```

### Change directory

```console
> cd <directory-name>
```

### Create a new directory

```console
> mkdir <directory-name>
```

## Contributing
This project is an educational tool and welcomes contributions. To contribute:
- Fork the repository.
- Make your changes.
- Submit a pull request with a description of your updates.

Feel free to open an issue for suggestions or bugs.

## License
This project is licensed under the [MIT License](LICENSE).
