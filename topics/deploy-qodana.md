# Deployment options

<show-structure for="chapter" depth="3"/>

<link-summary>Learn how to deploy %product% using various deployment options.</link-summary>

This section provides information about system requirements and available deployment options.

## System requirements

<table>
  <tr>
    <td>Requirement</td>
    <td>Minimum</td>
    <td>Recommended</td>
  </tr>
  <tr>
    <td>RAM</td>
    <td>2 GB of free RAM</td>
    <td>8 GB of total system RAM</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>Any modern CPU</td>
    <td>Multicore CPU. %product% supports multithreading for different operations and processes
        making it faster the more CPU cores it can use.</td>
  </tr>
  <tr>
    <td>Disk space</td>
    <td>2.5 GB + space for all dependencies and cache</td>
    <td>At least 5 GB of free space + space for all dependencies and cache</td>
  </tr>
  <tr>
    <td>Operating system</td>
    <td><p>Officially released versions of the following:</p>
      <list>
        <li>Microsoft Windows 10 1809 64-bit or later</li>
        <li>Windows Server 2019 64-bit or later</li>
        <li>macOS 12.0 or later</li>
        <li>Two latest versions of Ubuntu LTS or Fedora Linux distributions that meet the following requirements:
          <list>
            <li>Linux kernel version 6.x</li>
            <li><a href="https://ftp.gnu.org/gnu/libc/">GLIBC</a> 2.28 or later</li>
          </list>
          <p>Pre-release versions are not supported.</p>
        </li>
      </list>
    </td>
    <td><p>The latest versions of the following:</p>
      <list>
        <li>Microsoft Windows 64-bit</li>
        <li>macOS</li>
        <li>Ubuntu LTS or Fedora Linux</li>
      </list>
    </td>
  </tr>
</table>

## Deployment modes

### Native mode
{id="deploy-qodana-native-mode"}

<link-summary>Native mode lets you run this linter without Docker.</link-summary>

> Native mode is incompatible with Docker containers of %product%, which means that you can run
> %product% either as a Docker container or in native mode. Also, this mode is incompatible with several Docker image-related 
> options like `--image`, `-e, --env`, and `-v, --volume`.
> {style="note"}

Native mode comes in handy if you have to deal with private packages or run %instance% on the operating 
systems that provide incomplete support for Docker.

%instance% supports native mode for the following languages:

| Language                                                         | Linter name(s)                              |
|------------------------------------------------------------------|---------------------------------------------|
| [Java, Kotlin, Groovy, JavaScript, TypeScript](jvm.md)           | `%jvm-linter%` and `%jvm-co-linter%`        |  
| [PHP, JavaScript, TypeScript](php.md)                            | `%php-linter%`                              |  
| [JavaScript and TypeScript](js.md)                               | `%js-linter%`                               |  
| [C#, F#, VB.NET, JavaScript, TypeScript, C and C++  ](dotnet.md) | `%dotnet-linter%`                           |  
| [Python, JavaScript, TypeScript](python.md)                      | `%python-linter%` and `%python-co-linter%`  |  
| [Go](golang.md)                                                  | `%go-linter%`                               |  
{id="deploy-qodana-native-mode-table"}

You can run native mode on Linux, macOS, and Microsoft Windows.

In this case, %instance% reuses its execution environment, which lets you execute %instance% in exactly the same
environment as you use for building the projects, use the correct operating system, have access to all repository
credentials, and resolve dependencies.

### Docker mode
{id="deploy-qodana-container-mode"}

%product% is also distributed across multiple Docker images listed in the table below:

<table id="deploy-qodana-container-mode-table">
    <tr>
        <td>Linter</td>
        <td>Docker image</td>
    </tr>
    <tr>
      <td rowspan="4">
            <p><a href="jvm.md">%jvm-langs%</a></p>
      </td>
        <td>
            <p><code>%jvm-image%</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>%jvm-co-image%</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>%jvm-co-a-image%</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>%jvm-a-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="php.md">%php-langs%</a></p>
      </td>
        <td>
            <p><code>%php-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="js.md">%js-langs%</a></p>
      </td>
        <td>
            <p><code>%js-image%</code></p>
        </td>
    </tr>
    <tr>
      <td rowspan="2">
            <p><a href="dotnet.md">%dotnet-langs%</a></p>
      </td>
        <td>
            <p><code>%dotnet-image%&lt;-privileged&gt;</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>%dotnet-co-image%&lt;-privileged&gt;</code></p>
        </td>
    </tr>
    <tr>
      <td rowspan="2">
            <p><a href="python.md">%python-langs%</a></p>
      </td>
        <td>
            <p><code>%python-image%</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>%python-co-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="golang.md">%go-langs%</a></p>
      </td>
        <td>
            <p><code>%go-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="ruby.md">%ruby-langs%</a></p>
      </td>
        <td>
            <p><code>%ruby-image%&lt;-ruby3.X&gt;&lt;-privileged&gt;</code></p>
        </td>
    </tr>
    <tr>
      <td rowspan="2">
            <p><a href="clang.md">%clang-langs%</a></p>
      </td>
        <td>
            <p><code>%clang-image%&lt;-clangXX&gt;</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><code>%cpp-image%&lt;-clangXX&gt;&lt;-privileged&gt;</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="rust.md">%rust-langs%</a></p>
      </td>
        <td>
            <p><code>%rust-image%</code></p>
        </td>
    </tr>
</table>

The table contains optional tags to let you pull pre-configured %product% images:

* The `-clangXX` tag configures the [Clang-Tidy](https://clang.llvm.org/extra/clang-tidy) version from 15 to 18.
* The `-ruby3.X` tag configures the Ruby version from 3.1 to 3.4. If not specified, version 3.4 will be used.

  The `-privileged` tag lets you run %product% in the privileged mode to execute commands that require root access.
  In this case, Qodana comes with a default `qodana` user that possesses root privileges and does not require a password.
  Where applicable, this tag requires the `-clangXX` and `-ruby3.X` tags to be configured.

## Deployment environments

You can run %product% using the following capabilities:

* IDEs by JetBrains and other vendors
* Command-line interface
* CI/CD pipelines
* As a Gradle plugin

All these options are described in the [](Quick-start.topic) section.




