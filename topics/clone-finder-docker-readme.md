# Qodana Clone Finder


## How to
You can launch the tool in two steps.

First, download the repositories with which you want to compare a repository and map the directories as shown in the Docker arguments section.

Example:
```
/
├── project
│   └── some_code
└── versus
    ├── proj1
    │   └── some_code
    └── proj2
        └── some_code
```
Second, launch Qodana Clone Finder.

```shell script
docker run \
  -v "/project:/data/project" \
  -v "/versus:/data/versus" \
  -p 8080:8080 --rm \
registry.jetbrains.team/p/pdt/containers/qodana-clone-finder:qodana-stable --show-report
```
By default, it searches clones in all six languages but you can explicitly specify languages to search. For more information, see the Languages section below.

## Docker arguments
### Common arguments
`--rm` cleans up docker container's file system after it exits (recommended).

`--name qodana-clone-finder` names the container (optional).

### Mounted volumes
Mount the following volumes to the docker image:
* `/data/project` (mandatory)
* `/data/versus` (mandatory)
* `/data/result` (optional).

#### `/data/project`
This directory inside docker should contain your project that you want to compare against other projects and should always be mounted to `/data/project`.

Example: `-v "/local/path/to/project:/data/project"`

Full example:
```shell script
docker run \
  -v "/local/path/to/project:/data/project" \
  -v "/versus:/data/versus" \
  -p 8080:8080 --rm \
registry.jetbrains.team/p/pdt/containers/qodana-clone-finder:qodana-stable --show-report
```

#### `/data/versus`
This directory inside docker contains repositories to compare against.

Example, if the reference repositories are in one local directory:

`-v "/versus/dirs:/data/versus"`
```
/
├── project
└── versus
    └── dirs
        ├── proj1
        └── proj2
```

Full example:
```shell script
docker run \
  -v "/project:/data/project" \
  -v "versus/dirs:/data/versus" \
  -p 8080:8080 --rm \
registry.jetbrains.team/p/pdt/containers/qodana-clone-finder:qodana-stable --show-report
```
If they are located in different locations - `-v "/somepath/versus_proj1:/data/versus/proj1" -v "/another/versus_proj2:/data/versus/proj2" `
```
/
├── project
├── anotherpath
│   └── versus_proj2
└── somepath
    └── versus_proj1
```
Full example:
```shell script
docker run \
  -v "/project:/data/project" \
  -v "/somepath/versus_proj1:/data/versus/proj1" \
  -v "/anotherpath/versus_proj2:/data/versus/proj2" \
  -p 8080:8080 --rm \
registry.jetbrains.team/p/pdt/containers/qodana-clone-finder:qodana-stable --show-report
```

#### `/data/results`
This directory inside docker will contain JSONs with results - you can attach a local directory to store them if you want to analyze results without Qodana UI.

Example, if you want to store results in the `report` directory:
```
/
├── report
├── project
│   └── some_code
└── versus
    ├── proj1
    │   └── some_code
    └── proj2
        └── some_code
```
Run the following command:
```shell script
docker run \
  -v "/report:/data/result" \
  -v "/project:/data/project" \
  -v "/versus:/data/versus" \
  -p 8080:8080 --rm \
registry.jetbrains.team/p/pdt/containers/qodana-clone-finder:qodana-stable --show-report
```
Example, if the structure is the same as above but you don't want to use the Qodana UI&mdash;just store the results:
```shell script
docker run \
  -v "/report:/data/result" \
  -v "/project:/data/project" \
  -v "/versus:/data/versus" \
  --rm \
registry.jetbrains.team/p/pdt/containers/qodana-clone-finder:qodana-stable
```

### Ports
The report is shown on port 8080 in docker. If you want to access it, bind the port: `-p 8080:8080`.


### Qodana Clone Finder arguments
Clone Finder has only four arguments:
```shell script
  --show-report                   After searching, display a web report in the Qodana UI additionally to saving it as JSON files in /data/results
  -l, --language [PHP|Go|JavaScript|TypeScript|Java|Kotlin|Python]
                                  One or more languages to search clones in.
  --verbose                       Show logs and debugging info.
  --help                          Show this message and exit.
```

For more information on the `--show-report` & `--language` arguments, see the sections below.

#### Show report
You can view the report in the Qodana UI (keep in mind binding the docker port 8080) using the argument `--show-report`.

Example:
```shell script
docker run \
  -v "$(pwd) /project:/data/project" \
  -v "$(pwd)/versus:/data/versus" \
  -p 8080:8080 --rm \
registry.jetbrains.team/p/pdt/containers/qodana-clone-finder:qodana-stable --show-report
```

#### Languages
You can specify languages in which to search clones. Important: When specifying language names, mind that Clone Finder is case-sensitive.

Example, if you want to use only Java and Kotlin:
```shell script
docker run \
  -v "$(pwd)/project:/data/project" \
  -v "$(pwd)/versus:/data/versus" \
  -p 8080:8080 --rm \
registry.jetbrains.team/p/pdt/containers/qodana-clone-finder:qodana-stable --show-report \
-l Java -l Kotlin
