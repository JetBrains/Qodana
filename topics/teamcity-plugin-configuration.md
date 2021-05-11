[//]: # (title: Configuration)

The main Qodana functionality comes from the 'engine' shaped into the Docker image. If you want to go beyond the boundaries of the default settings, refer to the [Docker image guide](https://www.jetbrains.com/help/qodana/qodana-docker-readme.html). Note that you don't need to write `docker run` on your own: the plugin will do it for you. You can just use all other options and provide them via the dedicated UI or DSL properties.

### Advanced Configuration

Advanced configuration lets you report all found problems via the standard TeamCity tests mechanism. It means
you can assign investigations, mute, see history, and do everything else you can do with regular tests in TeamCity. Qodana IntelliJ reports tests in four different ways:

- per problem
- per inspection type
- per inspection type/per module (if this information is available)
- per inspection type/per file