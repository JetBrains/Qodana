# Running behind a proxy server

<p>Depending on your needs, you can run %product% behind a proxy server using an existing %product% Docker image,
    or create a Docker image from scratch.</p>
<tabs>
    <tab title="Existing Docker image" group-key="existing">
        <p>Follow these steps to prepare an existing %product% Docker image to run behind a proxy server:</p>
        <procedure id="troubleshooting-behind-a-proxy-existing">
            <step>Create the <code>proxy.settings.xml</code> file and save it in the <code>.qodana</code> directory of your project root.</step>
            <step><p>In the <code>proxy.settings.xml</code> file, save information about the proxy server that will be used by %product%:</p>
                <code-block lang="xml">
            &lt;application&gt;
                &lt;component name="HttpConfigurable"&gt;
                    &lt;option name="USE_HTTP_PROXY" value="true" /&gt;
                    &lt;option name="PROXY_HOST" value="&lt;ProxyHost&gt;" /&gt;
                    &lt;option name="PROXY_PORT" value="&lt;ProxyPort&gt;" /&gt;
                    &lt;!-- Add more settings as needed --&gt;
                &lt;/component&gt;
            &lt;/application&gt;
        </code-block>
            </step>
            <step><p>In the <a href="configuration-reference.md" anchor="Run+custom+commands"><code>qodana.yaml</code></a> file,
                save this <code>boostrap</code> command that will copy the <code>proxy.settings.xml</code> file
                to a %product% Docker image:</p>
                <code-block>
            boostrap: cp .qodana/proxy.settings.xml /root/.config/idea/options/proxy.settings.xml
        </code-block>
            </step>
            <step>
                <p>Run %product% using proxy server settings specified in the <code>JAVA_TOOL_OPTIONS</code> environment variable:</p>
                <tabs group="cli-settings">
                    <tab title="Docker image" group-key="docker-image">
            <code-block lang="shell" prompt="$">
                docker run \
                   -v $(pwd):/data/project/ \
                   -e JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=&lt;ProxyHost&gt; -Dhttps.proxyPort=&lt;ProxyPort&gt; -Dhttp.proxyHost=&lt;ProxyHost&gt; -Dhttp.proxyPort=&lt;ProxyPort&gt;" \
                   -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                   jetbrains/qodana-&lt;image&gt;
            </code-block>
                    </tab>
                    <tab title="Qodana CLI" group-key="qodana-cli">
            <code-block lang="shell" prompt="$">
                qodana scan \
                   -e JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=&lt;ProxyHost&gt; -Dhttps.proxyPort=&lt;ProxyPort&gt; -Dhttp.proxyHost=&lt;ProxyHost&gt; -Dhttp.proxyPort=&lt;ProxyPort&gt;" \
                   -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
            </code-block>
                    </tab>
                    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              -e JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=&lt;ProxyHost&gt;
                                                    -Dhttps.proxyPort=&lt;ProxyPort&gt;
                                                    -Dhttp.proxyHost=&lt;ProxyHost&gt;
                                                    -Dhttp.proxyPort=&lt;ProxyPort&gt;
                                                   "
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana
                                '''
                            }
                        }
                    }
                }
            </code-block>
                    </tab>
                    <tab title="Bitbucket Cloud" group-key="bitbucket-cloud">
                        <code-block lang="yaml">
                            &nbsp;
                            image: atlassian/default-image:4
                            &nbsp;
                                pipelines:
                                &nbsp;&nbsp;branches:
                                &nbsp;&nbsp;&nbsp;&nbsp;main:
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- step:
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name: Qodana
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;caches:
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- qodana
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;image: jetbrains/qodana-&lt;image&gt; # Specify a Qodana linter here. For example, jetbrains/qodana-jvm:latest
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;script:
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- export QODANA_TOKEN=$QODANA_TOKEN  # Export the environment variable
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- export JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=&lt;ProxyHost&gt; -Dhttps.proxyPort=&lt;ProxyPort&gt; -Dhttp.proxyHost=&lt;ProxyHost&gt; -Dhttp.proxyPort=&lt;ProxyPort&gt;"
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- qodana --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$HOME/.qodana/cache
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;artifacts:
                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- .qodana/report
&nbsp;
                                definitions:
                                &nbsp;&nbsp;caches:
                                &nbsp;&nbsp;&nbsp;&nbsp;qodana: .qodana/cache
                                </code-block>
                            </tab>
                        </tabs>
                    </step>
                </procedure>
            </tab>
            <tab title="Custom Docker image" group-key="custom">
                <p>To create your custom %product% image containing proxy server settings, follow this procedure:</p>
                <procedure id="troubleshooting-behind-a-proxy-custom">
                    <step><p>Create the <code>proxy.settings.xml</code> file and save proxy server settings in it:</p>
                        <code-block lang="xml">
                    &lt;application&gt;
                        &lt;component name="HttpConfigurable"&gt;
                            &lt;option name="USE_HTTP_PROXY" value="true" /&gt;
                            &lt;option name="PROXY_HOST" value="&lt;ProxyHost&gt;" /&gt;
                            &lt;option name="PROXY_PORT" value="&lt;ProxyPort&gt;" /&gt;
                            &lt;!-- Add more settings as needed --&gt;
                        &lt;/component&gt;
                    &lt;/application&gt;
                </code-block>
                    </step>
                    <step>
                        <p>Use this sample to create the <code>Dockerfile</code>:</p>
                        <code-block lang="docker">
                    FROM docker.io/jetbrains/qodana-&lt;image&gt;:2025.3&lt;-eap&gt;
                    LABEL version="1.0.0"
&nbsp;
                    ##Copy the proxy.settings.xml file
                    COPY proxy.settings.xml /root/.config/idea/options/proxy.settings.xml
&nbsp;
                    ##Copy the gradle.properties file (optional)
                    COPY gradle.properties ~/.gradle/gradle.properties
&nbsp;
                    ##Install certificates
                    COPY &lt;your_certificate&gt; &lt;path_to_certificate&gt;
                    RUN $JAVA_HOME/bin/keytool -import -trustcacerts -alias dc-ca -keystore $JAVA_HOME/lib/security/cacerts -noprompt -storepass changeit -file &lt;path_to_certificate&gt;
                    COPY &lt;your_certificate&gt; /etc/ssl/certs
                    RUN chmod  444 /etc/ssl/certs/&lt;your_certificate&gt;
&nbsp;
                    ##Set proxy
                    ENV http_proxy &lt;proxy&gt;
                    ENV https_proxy &lt;proxy&gt;
                    ENV HTTP_PROXY &lt;proxy&gt;
                    ENV HTTPS_PROXY &lt;proxy&gt;
                    ENV ftp_proxy $http_proxy
                    ENV dns_proxy $http_proxy
                    ENV rsync_proxy $http_proxy
                </code-block>
                    </step>
                    <step>
                        <p>Run %product% using proxy server settings configured in the <code>JAVA_TOOL_OPTIONS</code> environment variable:</p>
                        <tabs group="cli-settings">
                            <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -e JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=&lt;ProxyHost&gt; -Dhttps.proxyPort=&lt;ProxyPort&gt; -Dhttp.proxyHost=&lt;ProxyHost&gt; -Dhttp.proxyPort=&lt;ProxyPort&gt;" \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           &lt;image&gt;
                    </code-block>
                            </tab>
                            <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=&lt;ProxyHost&gt; -Dhttps.proxyPort=&lt;ProxyPort&gt; -Dhttp.proxyHost=&lt;ProxyHost&gt; -Dhttp.proxyPort=&lt;ProxyPort&gt;" \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --image &lt;image&gt;
                    </code-block>
                            </tab>
                            <tab title="Jenkins" group-key="jenkins">
                    <code-block lang="groovy">
                        pipeline {
                            environment {
                                QODANA_TOKEN=credentials('qodana-token')
                            }
                            agent {
                                docker {
                                    args '''
                                      -v "${WORKSPACE}":/data/project
                                      -e JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=&lt;ProxyHost&gt;
                                                            -Dhttps.proxyPort=&lt;ProxyPort&gt;
                                                            -Dhttp.proxyHost=&lt;ProxyHost&gt;
                                                            -Dhttp.proxyPort=&lt;ProxyPort&gt;
                                                           "
                                      --entrypoint=""
                                      '''
                                    image '&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
                    </tab>
                    <tab title="Bitbucket Cloud" group-key="bitbucket-cloud">
                        <code-block lang="yaml">
                        &nbsp;
                        image: atlassian/default-image:4
                        &nbsp;
                        pipelines:
                        &nbsp;&nbsp;branches:
                        &nbsp;&nbsp;&nbsp;&nbsp;main:
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- step:
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name: Qodana
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;caches:
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- qodana
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;image: jetbrains/qodana-&lt;image&gt; # Specify a Qodana linter here. For example, jetbrains/qodana-jvm:latest
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;script:
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- export QODANA_TOKEN=$QODANA_TOKEN  # Export the environment variable
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- export JAVA_TOOL_OPTIONS="-Dhttps.proxyHost=&lt;ProxyHost&gt; -Dhttps.proxyPort=&lt;ProxyPort&gt; -Dhttp.proxyHost=&lt;ProxyHost&gt; -Dhttp.proxyPort=&lt;ProxyPort&gt;"
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- qodana --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$HOME/.qodana/cache
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;artifacts:
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- .qodana/report
                        &nbsp;
                        definitions:
                        &nbsp;&nbsp;caches:
                        &nbsp;&nbsp;&nbsp;&nbsp;qodana: .qodana/cache
                        </code-block>
                    </tab>
                </tabs>
            </step>
        </procedure>
    </tab>
</tabs>
