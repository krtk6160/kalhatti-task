Section 2:
The file package_installer.py takes a json file name as an argument, iterates through the dependencies, and tries installing them one by one. Failed installation of packages is reported at the end.

The json file passed to the script should be of the following format:

{
  "Dependencies":
  {
    "dependency1":"==version",
    "dependency2":"==version"
  }
}