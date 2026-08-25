<!--    <chapter id="docker-config-reference-configuration-examples" title="Configuration examples">

    <chapter id="docker-config-reference-image-paths" title="Paths in linters">

        <link-summary>List of paths available in Qodana linters.</link-summary>

        <p>This table lists the paths available in %product% linters.</p>

        <table>
            <tr>
                <td>Path</td>
                <td>Description</td>
            </tr>
            <tr>
                <td><code>/data/project</code></td>
                <td>Root directory of the project</td>
            </tr>
            <tr>
                <td><code>/data/results</code></td>
                <td>Directory to store analysis reports. It should be empty before running %instance%</td>
            </tr>
            <tr>
                <td><code>/opt/idea</code></td>
                <td>IDE distributive directory</td>
            </tr>
            <tr>
                <td><code>/root/.config/idea</code></td>
                <td>IDE configuration directory</td>
            </tr>
            <tr>
                <td><code>/data/profile.xml</code></td>
                <td>The default profile file containing the <code>qodana.starter</code> profile configuration. This file
                    is used if a profile was not previously configured either via the CLI or the <code>qodana.yaml</code> file.
                    See <a href="inspection-profiles.md" anchor="Order+of+resolving+a+profile"/> for details</td>
            </tr>
            <tr>
                <td><code>/data/project/.idea/inspectionProfiles/</code></td>
                <td>Directory for binding <a anchor="docker-config-reference-profile-profile-name">profile files</a></td>
            </tr>
            <tr>
                <td><code>/data/cache/.m2</code></td>
                <td>Maven project dependencies</td>
            </tr>
            <tr>
                <td><code>/root/.m2/</code></td>
                <td>Directory for overriding the <code>settings.xml</code> configuration file for Maven</td>
            </tr>
            <tr>
                <td><code>/data/cache/gradle</code></td>
                <td><a anchor="docker-config-reference-gradle-settings">Gradle</a> project dependencies</td>
            </tr>
            <tr>
                <td><code>/data/cache/nuget</code></td>
                <td>NuGet project dependencies</td>
            </tr>
            <tr>
                <td><code>/data/coverage</code></td>
                <td>Directory for mapping <a href="code-coverage.md">code coverage</a> files</td>
            </tr>
        </table>

        <p>You can find below several examples of how these paths can be applied.</p>

        <chapter id="docker-config-reference-override-inspection-profile" title="Override the default inspection profile">

            <link-summary>Learn how you can override the default inspection profile.</link-summary>

            <p>By default, %instance% employs the <code>qodana.starter</code> profile, but you can
                <a anchor="docker-config-reference-image-paths">bind</a> and use your own profile instead:</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -v $(pwd)/&lt;profile-file&gt;:/data/profile.xml \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt;
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -v $(pwd)/&lt;profile-file&gt;:/data/profile.xml \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                    &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: -v &lt;profile-file&gt;:/data/profile.xml
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      -v "${WORKSPACE}"/&lt;profile-file&gt;:/data/profile.xml
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''qodana'''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                        - component: %gitlab-version%
                          inputs:
                             args: |
                                -v &lt;profile-file&gt;:/data/profile.xml
                                --linter &lt;linter&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Inspection profile</ui-path> dropdown list and select the <ui-path>Profile path</ui-path> option.
                    In the field that appears below the dropdown list, specify the path to your profile file relatively to the project root.</p>
                </tab>
            </tabs>

            <p>To learn more about profiles, see the
                <a href="inspection-profiles.md" anchor="Order+of+resolving+a+profile">order of resolving a profile</a> and
                <a href="inspection-profiles.md" anchor="inspection-profiles-setup-a-profile"/> sections in this documentation.</p>

        </chapter>

        <chapter id="docker-config-reference-gradle-settings" title="Override Gradle settings">

            <link-summary>Learn how you can override the default Gradle settings.</link-summary>

            <p>For JVM linters, you can override the default Gradle settings:</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -v $(pwd)/gradle.properties:/data/cache/gradle/gradle.properties \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt;
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -v $(pwd)/gradle.properties:/data/cache/gradle/gradle.properties \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: -v gradle.properties:/data/cache/gradle/gradle.properties
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      -v "${WORKSPACE}"/gradle.properties:/data/cache/gradle/gradle.properties
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''qodana'''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      -v gradle.properties:/data/cache/gradle/gradle.properties
                                      --linter &lt;linter&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
                        specify the path to the file containing new Gradle settings:</p>
                    <code-block lang="shell">
                        -v gradle.properties:/data/cache/gradle/gradle.properties
                    </code-block>
                </tab>
            </tabs>

        </chapter>

        <chapter id="docker-config-reference-overview-logs" title="View Qodana logs">

            <link-summary>Learn how you can view log files generated by %product%.</link-summary>

            <p>Depending on the tool, you can view log files generated by Qodana:</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">

                    <p>You can mount the <code>$(pwd)/.qodana/results/</code> directory to the <code>/data/results</code>
                    directory of the Docker image:</p>

                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -v $(pwd)/.qodana/results/:/data/results \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt;
                    </code-block>

                    <p>Once the Qodana run is complete, you can view log files in the
                        <code>$(pwd)/.qodana/results/</code> directory.</p>

                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <p>After running Qodana, in the project root run the <code>$ qodana show -d</code> command
                        for opening the directory containing log files.</p>
                </tab>
            </tabs>

            <p>There are several options for examining %instance% behavior using the <code>/data/results</code> directory:</p>
            <list>
                <li><p>The <code>/data/results/projectStructure</code> directory.</p>
                    <p>The <code>Modules.json</code> file in this directory contains a list of all modules detected by
                        %instance%. It should be identical to the list that you expect to see while opening your project in
                        IntelliJ IDEA. If this is no longer the case, check <code>pom.xml</code> for Maven or the
                        <code>build.gradle</code> file for Gradle configurations.</p>
                    <p>The <code>SDKs.json</code> file in this directory contains the interpreter paths in case of Python.</p>
                </li>
                <li>In the <code>/data/results/</code> directory, each inspection that detected a possible problem creates
                    its own file named <code>ID.json</code>, where <code>ID</code> is the inspection name that can be used in
                    <code>qodana.yaml</code> for including or excluding inspections. You can find the complete list of
                    inspection IDs in the <code>/data/results/.descriptions.json</code> file using the
                    <code>/groups/*/inspections/*/shortName</code> pattern.</li>
                <li>In <code>/data/results/log/idea.log</code>, you can investigate suspicious warnings.</li>
            </list>

        </chapter>


    </chapter>

    <chapter id="docker-config-reference-directories" title="Directories">

        <link-summary>Learn available CLI options for overriding default paths. </link-summary>

        <p>Using these options, you can override the paths described in the
            <a anchor="docker-config-reference-image-paths">Docker image paths</a> section.</p>

        <table>
            <tr>
                <td>Option</td>
                <td/>
                <td>Default setting</td>
            </tr>
            <tr id="docker-config-reference-directories-repository-root">
                <td>
                    <code>--repository-root &lt;string&gt;</code>
                </td>
                <td>
                    <p>Specify the VCS root directory for your project. This option is required for Git-related operations</p>
                </td>
                <td>None</td>
            </tr>
            <tr>
                <td><code>-i</code>, <code>--project-dir</code></td>
                <td><p>Root directory of the inspected project can be either a subdirectory of
                    <a anchor="docker-config-reference-directories-repository-root"><code>--repository-root</code></a> or identical to it.</p>
                    <p>Files and directories contained in the outside directory are not used while running %instance%</p>
                </td>
                <td><code>/data/project</code></td>
            </tr>
            <tr>
                <td><code>-o</code>, <code>--results-dir</code></td>
                <td>Directory to save %instance% inspection results to</td>
                <td><code>/data/results</code></td>
            </tr>
            <tr>
                <td><code>-r</code>, <code>--report-dir</code></td>
                <td><p>Directory for saving the generated HTML report. To open the report, you will need to add the
                    <a anchor="docker-config-reference-report"><code>--save-report</code></a> option</p>
                    <note>This option is not available in Qodana CLI.</note>
                </td>
                <td><code>/data/results/report</code></td>
            </tr>
            <tr>
                <td><code>--cache-dir</code></td>
                <td>Directory to store <a anchor="docker-config-reference-cache-dependencies">cache</a></td>
                <td><code>/data/cache</code></td>
            </tr>
            <tr>
                <td><code>-d</code>, <code>--source-directory</code></td>
                <td>
                    <note>This option is deprecated and will be removed in future versions of the product.
                        See the <code>--only-directory</code> option for details.</note>
                    <p>Directory inside <code>--project-dir</code>. If missing, the whole project is inspected.</p>
                    <p>Files and directories contained in the outside directory like <code>.git</code> and
                        <code>build.gradle</code> are used by %instance% while inspecting code</p>
                </td>
                <td>None</td>
            </tr>
            <tr>
                <td>
                    <code>--only-directory &lt;string&gt;</code>
                </td>
                <td>
                    <p>Specify the directory inside the <code>project-dir</code> directory that must be analyzed. If not specified,
                        the whole project will be analyzed</p>
                    <p>Files and directories contained in the outside directory like <code>.git</code> and
                        <code>build.gradle</code> are used by %instance% while inspecting code</p>
                </td>
                <td>None</td>
            </tr>
        </table>

        <chapter id="docker-config-reference-directories-save-report" title="Override the report directory">

            <link-summary>Override the directory containing %product% analysis reports.</link-summary>

            <tip><p>During analysis, Qodana CLI automatically saves analysis reports in the
                <code>./&lt;userCacheDir&gt;/JetBrains/Qodana/&lt;linter&gt;/&lt;project-id&gt;/results/report</code> directory.</p>
                <p>Here, the <code>linter</code> and <code>project-id</code> directories have the hash format.</p>
            </tip>

            <p>This Docker command overrides the default report directory using the <code>--report-dir</code>
                option, and saves the generated report to the local filesystem using the
                <a anchor="docker-config-reference-report"><code>--save-report</code></a> option:</p>

        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v &lt;html-report-directory&gt;:/data/results/newreportdir/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --report-dir /data/results/newreportdir/ \
               --save-report
        </code-block>

            <p>The generated report is saved to the local filesystem as configured by the
                <code>-v &lt;html-report-directory&gt;:/data/results/newreportdir/</code> line in this command.</p>

        </chapter>

        <chapter id="troubleshooting-inspect-specific-directory" title="Analyze a specific project directory within a repository">

            <link-summary>A typical project structure can have a directory structure explained in this section.</link-summary>

            <p>A typical project structure can have a directory structure similar to this:</p>

            <code-block lang="bash">
            repo/
            .git/
            project/
            ...
        </code-block>

            <p>Here, the <code>repo/.git</code> directory contains information that should be accessible to %instance%, and
                the <code>repo/project</code> directory contains the project that needs to be inspected by %instance%. All
                these samples mount the <code>repo/project</code> directory using the
                <a href="docker-image-configuration.topic" anchor="docker-config-reference-directories"><code>--project-dir</code></a>
                option, while the <code>QODANA_TOKEN</code> variable refers to the %cloud%
                <a href="project-token.md">project token</a>:</p>

            <tabs>
                <tab title="Docker image">
                <code-block lang="bash" prompt="$">
                    docker run \
                    -v repo/:/data/project/ \
                    -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                    jetbrains/qodana-&lt;image&gt; \
                    --project-dir=/data/project/project/
                </code-block>
                </tab>
                <tab title="Qodana CLI">
                <code-block lang="bash" prompt="$">
                    qodana scan \
                    -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                    --project-dir=/data/project/project/
                </code-block>
                </tab>
                <tab title="GitHub Actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches:
                                - main
                                - 'releases/*'

                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --project-dir project
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                </code-block>
                </tab>
            </tabs>

        </chapter>


        <chapter id="docker-config-reference-cache-dependencies" title="Cache dependencies">

            <link-summary>You can improve Qodana performance by persisting cache between analyses. For example, package and
                dependency management tools such as Maven, Gradle, npm, Yarn, and NuGet keep a local cache of
                downloaded dependencies.</link-summary>

            <tip><p><a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> automatically manages cache and requires no action.</p>
            <p>After the first run, Qodana CLI stores cache in the <code>./&lt;userCacheDir&gt;/JetBrains/&lt;linter&gt;/cache</code>
                directory.</p></tip>

            <p>You can improve %instance% performance by persisting cache between analyses. For example, package and
                dependency management tools such as Maven, Gradle, npm, Yarn, and NuGet keep a local cache of downloaded dependencies.</p>

            <p>By default, %instance% save caches to the <code>/data/cache</code> directory inside a container. You can override
                this location using the <a anchor="docker-config-reference-directories"><code>--cache-dir</code></a> option.
                This data is per-repository, so you can pass cache from <code>branch-a</code> to build checking
                <code>branch-b</code>. In this case, only new dependencies would be downloaded if they were added.</p>

            <p>In a GitHub workflow, you can use
                <a href="https://docs.github.com/en/actions/guides/caching-dependencies-to-speed-up-workflows">dependency caching</a>.
                GitLab CI/CD also has the <a href="https://docs.gitlab.com/ee/ci/caching/">cache</a> that can be stored
                <a href="https://docs.gitlab.com/ee/ci/yaml/README.html#cachepaths">only inside</a> the project directory.
                In this case, you can exclude the cache directory from inspection via
                <a href="qodana-yaml.md" anchor="include-example"><code>qodana.yaml</code></a>.</p>

            <p>This command maps the local directory with the <code>/data/cache</code> directory of the
                Docker image, which saves cache to your local filesystem: </p>

            <code-block lang="shell" prompt="$">
                docker run \
                   -v $(pwd):/data/project/ \
                   -v &lt;local-cache-directory&gt;:/data/cache/ \
                   -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                   jetbrains/qodana-&lt;image&gt;
            </code-block>

            <p>Using the <code>--cache-dir</code> option, you can override the cache directory:</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -v &lt;local-cache-directory&gt;:/data/newcachedir/ \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt; \
                           --cache-dir /data/newcachedir
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --cache-dir /opt/newcachedir
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --cache-dir /data/newcachedir
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --cache-dir /data/newcachedir
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --cache-dir /data/newcachedir
                                      --linter &lt;linter&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                        specify the path to the cache directory:</p>
                    <code-block lang="shell">
                        --cache-dir /data/newcachedir
                    </code-block>
                </tab>
            </tabs>
        </chapter>

    </chapter>

    <chapter id="docker-config-reference-profile" title="Profile">

        <link-summary>Learn more about available profile-related %product% options.</link-summary>

        <p>By default, %instance% inspects your code using the <code>qodana.starter</code> profile.</p>

        <p>You can configure and override %instance% profiles either in the <a href="inspection-profiles.md" anchor="inspection-profiles-setup-a-profile"><code>qodana.yaml</code></a>
            file, or using the options from this table.</p>

        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
                <td>Default setting</td>
            </tr>
            <tr>
                <td><code>--disable-sanity</code></td>
                <td>Skip running the inspections configured by the <a href="inspection-profiles.md" anchor="inspection-profiles-existing-profiles"><code>qodana.sanity</code></a> profile</td>
                <td>Enabled</td>
            </tr>
            <tr>
                <td><code>-n</code>, <code>--profile-name</code></td>
                <td><p>The <a anchor="docker-config-reference-profile-profile-name">profile name</a> from the list of predefined %instance% profiles, or a profile name of a custom profile
                    stored in XML-formatted profile files as <code ignore-vars="true">&lt;option name="myName" value="%profileName%"/&gt;</code>.</p>
                    <p>You can also configure this option using the <a href="inspection-profiles.md" anchor="inspection-profiles-setup-a-profile"><code>qodana.yaml</code></a> file</p>

                </td>
                <td><code>qodana.starter</code></td>
            </tr>
            <tr>
                <td><code>-p</code>, <code>--profile-path</code></td>
                <td>
                    <p>The <a anchor="docker-config-reference-profile-profile-path">absolute path</a> to the profile file.</p>
                    <p>You can also configure this option using the <a href="inspection-profiles.md" anchor="inspection-profiles-setup-a-profile"><code>qodana.yaml</code></a> file</p>
                </td>
                <td>None</td>
            </tr>
            <tr>
                <td><code>--run-promo</code></td>
                <td><p>Run promo inspections as a part of the <code>qodana.starter</code> profile</p>
                    <note>This option is not available in the <a href="dotnet.md">%dotnet%</a> linter.</note>
                </td>
                <td>Enabled only if %instance% is configured for the <code>qodana.starter</code> profile, and the <code>--run-promo true</code> option is invoked</td>
            </tr>
        </table>

        <chapter id="docker-config-reference-profile-profile-name" title="Profile name">

            <p filter="for-inspection-profiles">The <code>--profile-name</code> option lets you run %instance% using either
                the <a href="inspection-profiles.md" anchor="inspection-profiles-existing-profiles">default profiles</a> or
                the profile name from a <a href="inspection-profiles.md" anchor="inspection-profiles-custom-profiles">custom profile</a>. </p>

            <tip>You can also configure this option using the <a href="inspection-profiles.md" anchor="inspection-profiles-yaml-file"><code>qodana.yaml</code></a> file.</tip>

            <p filter="for-inspection-profiles">This command lets you override the default profile und run %instance% using the
                <a href="inspection-profiles.md" anchor="inspection-profiles-existing-profiles"><code>qodana.recommended</code></a> profile: </p>

            <tabs group="cli-settings" filter="for-inspection-profiles">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt; \
                           --profile-name qodana.recommended
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --profile-name qodana.recommended
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --profile-name qodana.recommended
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --profile-name qodana.recommended
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --profile-name qodana.recommended
                                      --linter &lt;linter&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                        specify the profile name:</p>
                    <code-block lang="shell">
                        --profile-name qodana.recommended
                    </code-block>
                </tab>
            </tabs>

            <p filter="for-inspection-profiles">To run %instance% with a custom profile, use its actual
                profile name.</p>

            <p filter="for-inspection-profiles">The following lets you bind a custom profile:</p>

            <tabs group="cli-settings" filter="for-inspection-profiles">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/.idea/inspectionProfiles/&lt;file-name&gt; \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt; \
                           --profile-name &lt;profile-name-from-file&gt;
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/.idea/inspectionProfiles/&lt;file-name&gt; \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --profile-name &lt;profile-name-from-file&gt;
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --profile-name &lt;profile-name-from-file&gt;
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --profile-name &lt;profile-name-from-file&gt;
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --profile-name &lt;profile-name-from-file&gt;
                                      --linter &lt;linter&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                        specify the custom profile name:</p>
                    <code-block lang="shell">
                        --profile-name &lt;profile-name-from-file&gt;
                    </code-block>
                </tab>
            </tabs>

        </chapter>

        <chapter id="docker-config-reference-profile-profile-path" title="Profile path">

            <p>The <code>--profile-path</code> option lets you override the path to the file containing the profile.</p>

            <tip>You can also configure this option using the <a href="inspection-profiles.md" anchor="inspection-profiles-yaml-file"><code>qodana.yaml</code></a> file.</tip>

            <p>This command lets you bind the file to the profile directory,
                and the <code>--profile-path</code> option tells %instance% which profile file to read:</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/myprofiles/&lt;file-name&gt; \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt; \
                           --profile-path /data/project/myprofiles/&lt;file-name&gt;
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/myprofiles/&lt;file-name&gt; \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --profile-path /data/project/myprofiles/&lt;file-name&gt;
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --profile-path /data/project/myprofiles/&lt;file-name&gt;
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --profile-path /data/project/myprofiles/&lt;file-name&gt;
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --profile-path /data/project/myprofiles/&lt;file-name&gt;
                                      --linter &lt;linter&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                        specify the path your custom profile:</p>
                    <code-block lang="shell">
                        --profile-path /data/project/myprofiles/&lt;file-name&gt;
                    </code-block>
                </tab>
            </tabs>

        </chapter>

    </chapter>

    <chapter id="docker-config-reference-custom-yaml-config" title="Custom configuration file">

        <link-summary>You can save %product% settings in your custom YAML-formatted file. You can then invoke this file
            using the --config option and a path to a file relatively to the project root.</link-summary>

        <p>Your project can have several %product% configurations contained in
            <a href="qodana-yaml.md">YAML-formatted files</a>. This comes in handy if you analyze monorepo projects or
            run a single CI job.</p>

            <p>You can use the <code>--config</code> option and a path
            to a file relatively to the project root:</p>
        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                    &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project \
                    &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                    &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
                    &nbsp;&nbsp;&nbsp;--config relative/path/to/config.yaml
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                qodana scan \
                &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                &nbsp;&nbsp;&nbsp;--config relative/path/to/config.yaml
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --config relative/path/to/config.yaml
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --config relative/path/to/config.yaml
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --config relative/path/to/config.yaml
                                      --linter &lt;linter&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                    specify the path to your custom configuration file:</p>
                <code-block lang="shell">
                        --config relative/path/to/config.yaml
                    </code-block>
            </tab>
        </tabs>
    </chapter>


    <chapter id="docker-config-reference-baseline" title="Baseline">

        <link-summary>In the baseline mode, each new %product% run is compared to some initial run, which helps when you
            have no possibility to fix old problems and rather want to prevent the appearance of new ones.</link-summary>

        <p>In the <a href="baseline.topic">baseline</a> run mode, each new %instance% run is compared to some initial run. This can help in
            situations when you have no possibility to fix old problems and rather want to prevent the appearance of new ones.</p>

        <p>To use the baseline feature, first run %instance%, and in the report UI select the problems that will be considered as baseline.
        Finally, save the <a href="qodana-inspection-output.md" anchor="SARIF+Output">SARIF-formatted file</a> containing the baseline problems. </p>

        <p>This is the list of baseline-related options:</p>

        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
            </tr>
            <tr>
                <td><code>-b</code>, <code>--baseline</code></td>
                <td>Run %instance% in the <a href="baseline.topic">baseline</a> mode. Provide the path to an existing SARIF report to be used in the baseline state calculation</td>
            </tr>
            <tr>
                <td><code>--baseline-include-absent</code></td>
                <td>Include in the output report the results from the baseline run that are absent during the current analysis</td>
            </tr>
        </table>

        <p>This command invokes all baseline options:</p>

        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                       -v $(pwd):/data/project/ \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       jetbrains/qodana-&lt;image&gt; \
                       --baseline &lt;path-to-the-SARIF-file&gt; \
                       --baseline-include-absent
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       --baseline &lt;path-to-the-SARIF-file&gt; \
                       --baseline-include-absent
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: |
                                          --baseline &lt;path-to-the-SARIF-file&gt;
                                          --baseline-include-absent
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --baseline &lt;path-to-the-SARIF-file&gt; \
                                        --baseline-include-absent
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --baseline &lt;path-to-the-SARIF-file&gt;
                                      --baseline-include-absent --linter &lt;linter&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                    configure a baseline:</p>
                <code-block lang="shell">
                      --baseline &lt;path-to-the-SARIF-file&gt; --baseline-include-absent --linter &lt;linter&gt;
                    </code-block>
            </tab>
        </tabs>

        <p>Here, the <code>&lt;path-to-the-SARIF-file&gt;</code> is the path to a <code>qodana.sarif.json</code> file relative
            to the project root and taken from a previous %instance% run. If <code>--baseline-include-absent</code>
            is invoked, the inspection results will include absent problems or the problems detected only in the
            baseline run but not in the current run. </p>

        <p>Based on this run, the <a href="qodana-inspection-output.md" anchor="SARIF+Output">SARIF output report</a> will contain the per-problem information on the
            baseline state.</p>

    </chapter>

    <chapter id="docker-config-reference-code-coverage" title="Code coverage">

        <link-summary>You can run the code coverage by mapping the directory containing code coverage files to
            the /data/coverage directory of a %instance% linter image.</link-summary>

        <note>
            For the <a href="golang.md">%go%</a> linter, the code coverage requires that a project contains no <code>.idea</code> directory.
        </note>

        <p>You can run the <a href="code-coverage.md">code coverage</a> by mapping the directory containing code coverage files to
            the <code>/data/coverage</code> directory of a %instance% linter image:</p>

        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                       -v /my/dir/with/coverage:/data/coverage \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       jetbrains/qodana-&lt;image&gt;
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                       -v /my/dir/with/coverage:/data/coverage \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: -v /my/dir/with/coverage:/data/coverage
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        -v /my/dir/with/coverage:/data/coverage
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      -v /my/dir/with/coverage:/data/coverage
                                      --linter &lt;linter&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
                    specify the path the file containing code coverage results:</p>
                <code-block lang="shell">
                        -v /my/dir/with/coverage:/data/coverage
                    </code-block>
            </tab>
        </tabs>
    </chapter>

    <chapter id="docker-config-reference-report" title="Report">

        <link-summary>Learn more about available profile-related %product% options.</link-summary>

        <p>This table contains the options related to reports:</p>

        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
            </tr>
            <tr>
                <td><code>-s</code>, <code>--save-report</code></td>
                <td>Generate and save HTML-formatted reports</td>
            </tr>
            <tr>
                <td><code>-w</code>, <code>--show-report</code></td>
                <td>Serve HTML-formatted reports. By default, port <code>8080</code> is used</td>
            </tr>
        </table>

        <chapter id="docker-config-reference-report-save-report" title="Save the report">

            <link-summary>The --save-report option lets you save the generated HTML report to your
                local filesystem.</link-summary>

            <tip><p>During inspection, Qodana CLI automatically saves analysis reports in the
                <code>./&lt;userCacheDir&gt;/JetBrains/Qodana/&lt;linter&gt;/&lt;project-id&gt;/results/report</code> directory.</p>
                <p>Here, the <code>linter</code> and <code>project-id</code> directories have the hash format.</p>
                <p>To view the generated report in your browser, in the project root run the <code>qodana show</code> command.</p>
            </tip>

            <p>The <code>--save-report</code> option in the Docker command lets you save the generated HTML report to your
                local filesystem: </p>

            <code-block lang="shell" prompt="$">
                docker run \
                   -v $(pwd):/data/project/ \
                   -v &lt;directory-to-save-report-to&gt;:/data/results/report \
                   -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                   jetbrains/qodana-&lt;image&gt; \
                   --save-report
            </code-block>

        </chapter>

        <chapter id="docker-config-reference-report-show-report" title="Show the report">

            <link-summary>The --show-report option runs a local web server to show an analysis report.</link-summary>

            <p>This command runs the web server on port 4040 of a host machine, so your report will be available on
                <a href="http://localhost:4040">http://localhost:4040</a>:</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -p 4040:8080 \
                           -v $(pwd):/data/project/ \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt; \
                           --show-report
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --port 4040 \
                           --show-report
                    </code-block>
                    <p>Alternatively, in the project root you can run the <code>qodana show</code> command.</p>
                </tab>
            </tabs>

            <p>To stop the web server, press <shortcut>Ctrl-C</shortcut> in the Docker console.</p>

        </chapter>
    </chapter>

    <chapter id="docker-config-reference-quality-gate" title="Quality gate">

        <link-summary>You can configure a quality gate that will act as a threshold. Once the threshold is exceeded,
            the inspection run is terminated.</link-summary>

        <p>%instance% lets you configure a <a href="quality-gate.topic">quality gate</a> or the number of problems that
            will act as a threshold. Once the threshold is exceeded, the inspection run is terminated.</p>

        <tip>You can specify the threshold as explained in the <a href="qodana-yaml.md" anchor="Set+a+quality+gate"/>
            section. However, the Docker command option overrides the settings in the <code>qodana.yaml</code> file. </tip>

        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
            </tr>
            <tr>
                <td><code>--fail-threshold</code></td>
                <td>Set the number of problems that will serve as a quality gate</td>
            </tr>
        </table>

        <p>Here is the command that tells %instance% to fail the build in case the number of problems exceeds 10:</p>

        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                       -v $(pwd):/data/project/ \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       jetbrains/qodana-&lt;image&gt; \
                       --fail-threshold 10
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       --fail-threshold 10
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --fail-threshold 10
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --fail-threshold 10
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --fail-threshold 10
                                      --linter &lt;linter&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                    specify a quality gate:</p>
                <code-block lang="shell">
                        --fail-threshold 10
                    </code-block>
            </tab>
        </tabs>

        <p>If you run %instance% with the <a anchor="docker-config-reference-baseline">baseline mode</a> enabled, a
            threshold is calculated as the sum of new and absent problems. The unchanged results are ignored.</p>

    </chapter>

    <chapter title="Quick-Fix" id="docker-config-reference-quick-fix">

        <link-summary>To apply Quick-Fix strategies to your codebase, you can invoke the --fixes-strategy option.</link-summary>

        <p>To apply <a href="quick-fix.md">Quick-Fix</a> strategies to your codebase, you can invoke the <code>--fixes-strategy</code> option.</p>
        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                       -v &lt;source-directory&gt;/:/data/project/ \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       jetbrains/qodana-&lt;image&gt; \
                       --fixes-strategy &lt;cleanup/apply&gt;
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       &lt;--apply-fixes/--cleanup&gt;
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: &lt;--apply-fixes/--cleanup&gt;
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --fixes-strategy &lt;--apply-fixes/--cleanup&gt;
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      &lt;--apply-fixes/--cleanup&gt;
                                      --linter &lt;linter&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                    specify the preferred Quick-Fix strategy:</p>
                <code-block lang="shell">
                        &lt;--apply-fixes/--cleanup&gt;
                    </code-block>
            </tab>
        </tabs>

    </chapter>

    <chapter id="docker-config-reference-properties" title="Properties">

        <link-summary>Learn how you can override %product% settings using properties.</link-summary>

        <p>Using the <code>--property=</code> option, you can override various %instance% parameters:</p>

        <list>
            <li><a anchor="docker-config-reference-properties-stdout">Logging messages to STDOUT</a></li>
            <li><a anchor="docker-config-reference-properties-user-statistics">Disabling user statistics</a></li>
            <li><a anchor="docker-config-reference-properties-config-plugins">Configuring plugins</a></li>
            <li><a anchor="docker-config-reference-properties-config-timeout">Setting up configuration timeout</a></li>
        </list>

        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
            </tr>
            <tr>
                <td><code>--property=</code></td>
                <td><p>Set a JVM property using this notation:</p>
                    <code-block lang="shell">--property=property.name=value1,...,valueN</code-block>
                    <p>This option can be repeated multiple times for setting multiple JVM properties.</p>
                </td>
            </tr>
        </table>

        <chapter id="docker-config-reference-properties-stdout" title="Log INFO messages to STDOUT">

            <note>This feature is not available in the <a href="dotnet.md">%dotnet%</a> linter.</note>

            <!-- What does this command mean?-->

            <p>The default log level for STDOUT is <code>WARN</code>. You can override it using the
                <code>idea.log.config.file</code> property.</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt; \
                           --property=idea.log.config.file=info.xml
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --property=idea.log.config.file=info.xml
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --property=idea.log.config.file=info.xml
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --property=idea.log.config.file=info.xml
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --property=idea.log.config.file=info.xml
                                      --linter &lt;linter&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                        specify the preferred Quick-Fix strategy:</p>
                    <code-block lang="shell">
                        --property=idea.log.config.file=info.xml
                    </code-block>
                </tab>
            </tabs>
        </chapter>


        <chapter id="docker-config-reference-properties-user-statistics" title="Disable user statistics">

            <link-summary>You can disable reporting of usage statistics by adjusting the idea.headless.enable.statistics
                value of the --property option.</link-summary>

            <p>To disable reporting of usage statistics, adjust the <code>idea.headless.enable.statistics</code>
                value of the <code>--property</code> option:</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt; \
                           --property=idea.headless.enable.statistics=false
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --property=idea.headless.enable.statistics=false
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --property idea.headless.enable.statistics=false
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --property=idea.headless.enable.statistics=false
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --property idea.headless.enable.statistics=false
                                      --image &lt;image&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                        specify the required property:</p>
                    <code-block lang="shell">
                        --property=idea.headless.enable.statistics=false
                    </code-block>
                </tab>
            </tabs>
        </chapter>

        <chapter id="docker-config-reference-properties-config-plugins" title="Configure plugins">

            <link-summary>Using the idea.required.plugins.id and idea.suppressed.plugins.id properties,
                you can specify the plugins required for a specific run, and the list of plugins that will
                be suppressed.</link-summary>

            <p>Using the <code>idea.required.plugins.id</code> and <code>idea.suppressed.plugins.id</code> properties,
                you can specify the plugins required for a specific run, and the list of plugins that will
                be suppressed: </p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt; \
                           --property=idea.required.plugins.id=JavaScript,org.intellij.grails \
                           --property=idea.suppressed.plugins.id=com.intellij.spring.security
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --property=idea.required.plugins.id=JavaScript,org.intellij.grails \
                           --property=idea.suppressed.plugins.id=com.intellij.spring.security
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: |
                                          --property=idea.required.plugins.id=JavaScript,org.intellij.grails
                                          --property=idea.suppressed.plugins.id=com.intellij.spring.security
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --property=idea.required.plugins.id=JavaScript,org.intellij.grails \
                                        --property=idea.suppressed.plugins.id=com.intellij.spring.security
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --property=idea.required.plugins.id=JavaScript,org.intellij.grails
                                      --property=idea.suppressed.plugins.id=com.intellij.spring.security
                                      --image &lt;image&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                        specify the required properties:</p>
                    <code-block lang="shell">
                           --property=idea.required.plugins.id=JavaScript,org.intellij.grails \
                           --property=idea.suppressed.plugins.id=com.intellij.spring.security
                    </code-block>
                </tab>
            </tabs>
        </chapter>
        <chapter id="docker-config-reference-properties-config-timeout" title="Setting up configuration timeout">
            <note>These properties are available only for the <a href="rust.md">%rust%</a>, <a href="clang.md">%cpp% and %clang%</a> linters.</note>
            <p>Using the following properties, you can configure the <a href="inspect-your-code.md" anchor="Analysis+stages">configuration stage timeout</a>:</p>
                <table>
                    <tr>
                        <td>Property</td>
                        <td>Available for the linters</td>
                    </tr>
                    <tr>
                        <td><code>qd.cpp.startup.timeout.minutes</code></td>
                        <td><a href="clang.md">%cpp% and %clang%</a></td>
                    </tr>
                    <tr>
                        <td><code>qd.rust.configuration.timeout.minutes</code></td>
                        <td><a href="rust.md">%rust%</a></td>
                    </tr>
                </table>
            <p>Here are the examples of property usage:</p>
            <tabs group="software">
                <tab title="GitHub Actions" group-key="github">
        <code-block lang="yaml">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - 'releases/*' # The release branches
            jobs:
                qodana:
                    runs-on: ubuntu-latest
                    permissions:
                        contents: write
                        pull-requests: write
                        checks: write
                    steps:
                        - uses: actions/checkout@v3
                          with:
                              ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                              fetch-depth: 0  # a full history is required for pull request analysis
                        - name: 'Qodana Scan'
                          uses: %action-version%
                          with:
                              args: --property qd.&lt;cpp|rust&gt;.startup.timeout.minutes=10
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
                </tab>
                <!--<tab title="GitLab CI/CD" group-key="gitlab">
                    <p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
                    <code-block lang="yaml" filter="cpp">
                      include:
                          - component: %gitlab-version%
                            inputs:
                                args: --linter %qd-linter%
                    </code-block>
                    <code-block lang="yaml" filter="rust">
                      include:
                          - component: %gitlab-version%
                            inputs:
                                args: --linter %qd-linter%
                    </code-block>
                </tab>-->
                <tab title="Command line" group-key="command-line">
                    <tabs group="cli-settings">
                        <tab group-key="qodana-cli" title="Qodana CLI">
                    <code-block prompt="$" lang="shell">
                      qodana scan \
                      &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                      &nbsp;&nbsp;&nbsp;--linter &lt;linter&gt; \
                      &nbsp;&nbsp;&nbsp;--property qd.&lt;cpp|rust&gt;.configuration.timeout.minutes=10
                    </code-block>
                        </tab>
                    <tab group-key="docker-image" title="Docker image">
                    <code-block lang="shell" prompt="$">
                    docker run \
                    &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
                    &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                    &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
                    &nbsp;&nbsp;&nbsp;--property qd.&lt;cpp|rust&gt;.configuration.timeout.minutes=10
                </code-block>
                        </tab>
                    </tabs>
                </tab>
            </tabs>
        </chapter>
    </chapter>

    <chapter id="docker-config-reference-changes" title="Analysis of changes">

        <link-summary>For all linters except Qodana Community for .NET, you can run incremental analysis on a change set like
            merge or pull requests, as well as inspect changes between two commits.</link-summary>

        <note>This feature is not supported by the <a href="dotnet.md">%dotnet-co%</a> and <a href="clang.md">%clang%</a> linters.</note>

        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
            </tr>
            <tr>
                <td><code>--diff-start</code> and <code>--diff-end</code></td>
                <td>
                    Run incremental analysis on a change set like merge or pull requests
                </td>
            </tr>
        </table>

        <snippet id="docker-config-reference-changes-examples">

            <p>If you just finished work and would like to analyze the changes, you
                can employ the <code>--diff-start</code> option and specify a hash of the commit that will act as a base
                for comparison, see the <a href="analyze-pr.md"/> section for details:</p>

        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                    &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
                    &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                    &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
                    &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                    &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                    &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --diff-start=&lt;GIT_START_HASH&gt;
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --diff-start=&lt;GIT_START_HASH&gt;
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --diff-start=&lt;GIT_START_HASH&gt;
                                      --image &lt;image&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                    specify the commit hash:</p>
                <code-block lang="shell">
                        --diff-start=&lt;GIT_START_HASH&gt;
                    </code-block>
            </tab>
        </tabs>

        <p>To analyze a set of changes between two commits, employ both <code>--diff-start</code>
        and <code>--diff-end</code> options:</p>

        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                    &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
                    &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                    &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
                    &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt; \
                    &nbsp;&nbsp;&nbsp;--diff-end=&lt;GIT_END_HASH&gt;
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                    &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                    &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt; \
                    &nbsp;&nbsp;&nbsp;--diff-end=&lt;GIT_END_HASH&gt;
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: |
                                          --diff-start=&lt;GIT_START_HASH&gt;
                                          --diff-end=&lt;GIT_END_HASH&gt;
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --diff-start=&lt;GIT_START_HASH&gt; \
                                        --diff-end=&lt;GIT_END_HASH&gt;
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --diff-start=&lt;GIT_START_HASH&gt;
                                      --diff-end=&lt;GIT_END_HASH&gt;
                                      --image &lt;image&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                    specify the commit hashes:</p>
                <code-block lang="shell">
                        --diff-start=&lt;GIT_START_HASH&gt; --diff-end=&lt;GIT_END_HASH&gt;
                    </code-block>
            </tab>
        </tabs>

        </snippet>

    </chapter>

    <chapter id="docker-config-reference-run-scenario" title="Run scenario">

        <link-summary>Currently, Qodana supports several run scenarios.</link-summary>

        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
                <td>Default setting</td>
            </tr>
            <tr>
                <td><code>--script</code></td>
                <td>Override the default run scenario</td>
                <td><code>default</code></td>
            </tr>
        </table>

        <tip>You can also configure this option using the
            <a href="qodana-yaml.md" anchor="Override+the+default+run+scenario"><code>qodana.yaml</code></a> file.</tip>

        <p>Application of the <code>default</code> run scenario is equivalent to running this command:</p>

        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                       -v $(pwd):/data/project/ \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       jetbrains/qodana-&lt;image&gt; \
                       --script default
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       --script default
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --script default
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --script default
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --script default
                                      --image &lt;image&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                    specify the preferred run scenario:</p>
                <code-block lang="shell">
                        --script default
                    </code-block>
            </tab>
        </tabs>

        <p>For the <a href="php-language-upgrade.topic">PHP version migration</a> scenario, use this command:</p>

        <tabs group="cli-settings">
            <tab title="Docker image" group-key="docker-image">
                <code-block lang="shell" prompt="$">
                    docker run \
                       -v $(pwd):/data/project/ \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       jetbrains/qodana-&lt;image&gt; \
                       --script php-migration:&lt;old-php-version&gt;−to−&lt;upgraded-php-version&gt;
                </code-block>
            </tab>
            <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       --script php-migration:&lt;old-php-version&gt;−to−&lt;upgraded-php-version&gt;
                </code-block>
            </tab>
            <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: --script php-migration:&lt;old-php-version&gt;−to−&lt;upgraded-php-version&gt;
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      --entrypoint=""
                                      '''
                                    image 'jetbrains/qodana-&lt;image&gt;'
                                }
                            }
                            stages {
                                stage('Qodana') {
                                    steps {
                                        sh '''
                                        qodana \
                                        --script,php-migration:&lt;old-php-version&gt;−to−&lt;upgraded-php-version&gt;
                                        '''
                                    }
                                }
                            }
                        }
                    </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      --script php-migration:&lt;old-php-version&gt;−to−&lt;upgraded-php-version&gt;
                                      --image &lt;image&gt;
                    </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
                    specify the PHP version migration run scenario:</p>
                <code-block lang="shell">
                        --script php-migration:&lt;old-php-version&gt;−to−&lt;upgraded-php-version&gt;
                    </code-block>
            </tab>
        </tabs>

    </chapter>

    <!-- What is this for?  And how can I run it? -->

    <!--<chapter id="docker-config-reference-qodana-cloud" title="Forward reports to Qodana Cloud">

        <p>To forward reports to Qodana Cloud, you can set the list of Docker environments as explained in the
            <a href="cloud-forward-reports.topic"/> section.</p>

        <p>Alternatively, see the <a anchor="docker-config-reference-qodana-send"/> chapter of this section.</p>

    </chapter>-->

        <chapter id="docker-config-reference-docker-environment-heap-size" title="Change the Heap size">

            <link-summary>By default, the Heap size is set to 80% of the host RAM. You can configure this setting using the
                _JAVA_OPTIONS variable.</link-summary>

            <p>By default, the Heap size is set to 80% of the host RAM. You can configure this setting using the
                <code>_JAVA_OPTIONS</code> variable: </p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -e _JAVA_OPTIONS=-Xmx6g \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt;
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e _JAVA_OPTIONS=-Xmx6g \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: -e _JAVA_OPTIONS=-Xmx6g
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      -e _JAVA_OPTIONS=-Xmx6g
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
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      -e _JAVA_OPTIONS=-Xmx6g
                                      --image &lt;image&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
                        configure the heap size using the <code>_JAVA_OPTIONS</code> variable:</p>
                    <code-block lang="shell">
                        -e _JAVA_OPTIONS=-Xmx6g
                    </code-block>
                </tab>
            </tabs>

            <p>To learn more about configuring the Heap, see the
                <a href="https://docs.oracle.com/cd/E19900-01/819-4742/abeik/index.html">Heap Tuning Parameters</a>
                of the Oracle documentation.</p>
        </chapter>

        <chapter id="docker-config-reference-docker-environment-idea-properties" title="Override the idea.properties file">

            <link-summary>The idea.properties file configures the default locations of the IDE files. You can override
                this file using the IDEA_PROPERTIES variable. </link-summary>

            <note>This feature is not available in the <a href="dotnet.md">%dotnet%</a> linter.</note>

            <p>The <code>idea.properties</code> configures the default locations of the IDE files.</p>

            <p>You can override the <code>idea.properties</code> file using the <code>IDEA_PROPERTIES</code> variable:</p>

            <tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -e IDEA_PROPERTIES=/data/project/idea.properties \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           jetbrains/qodana-&lt;image&gt;
                    </code-block>
                </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -e IDEA_PROPERTIES=/data/project/idea.properties \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: -e IDEA_PROPERTIES=/data/project/idea.properties
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      -e IDEA_PROPERTIES=/data/project/idea.properties
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
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      -e IDEA_PROPERTIES=/data/project/idea.properties
                                      --image &lt;image&gt;
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
                        configure the <code>IDEA_PROPERTIES</code> variable:</p>
                    <code-block lang="shell">
                        -e IDEA_PROPERTIES=/data/project/idea.properties
                    </code-block>
                </tab>
            </tabs>

        </chapter>

        <chapter id="docker-config-reference-docker-environment-run-non-root" title="Configure root and non-root users">

            <link-summary>Learn how to set up %product% for running as root and non-root users.</link-summary>

            <tip>You can build your own Docker image with the required dependencies using our
                <a href="https://github.com/JetBrains/qodana-docker/blob/main/2025.2/python-community/Dockerfile">Dockerfile</a>.
            </tip>

            <tabs group="cli-settings">
                <tab id="docker-config-reference-docker-environment-docker" group-key="docker-image" title="Docker">
                    <p>By default, a Docker container runs under the <code>root</code> user, so %instance% can
                        read project information and write inspection results. Therefore, all files in the <code>results/</code>
                        directory are owned by the <code>root</code> user after the run.</p>

                    <p>To overcome this, you can run the container as a regular user:</p>

                    <code-block lang="shell" prompt="$">
                        docker run \
                        -u $(id -u):$(id -g) \
                        -v $(pwd):/data/project/ \
                        -v &lt;results-directory&gt;:/data/results/ \
                        -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                        jetbrains/qodana-&lt;image&gt;
                    </code-block>

                    <p>In this case, the <code>results/</code> directory on the host should already be created and owned by you.
                        Otherwise, Docker will create it as the <code>root</code> user, and %instance% will not be able to write
                        to it.</p>
                </tab>
                <tab id="docker-config-reference-docker-environment-teamcity-qodana-cli" group-key="qodana-cli" title="TeamCity and Qodana CLI">
                    <p>TeamCity and <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> run %instance%
                        using a current non-root user. This can be inconvenient if you wish to install dependencies
                        using the <code>apt</code> tool invoked in the
                        <a href="qodana-yaml.md" anchor="Run+custom+commands"><code>bootstrap</code></a> section.</p>
                    <p>To run %product% as a root user in TeamCity, add the <code>-u root</code> option in the
                        <a href="teamcity.md" anchor="teamcity-qodana-runner"><ui-path>Additional Docker arguments</ui-path></a>
                        field of the %product% runner configuration.</p>
                    <p>To run Qodana CLI as a root user, you can append <code>-u root</code>
                        option to the <code>qodana scan</code> command:</p>
                    <code-block lang="shell" prompt="$">
                        qodana scan -u root
                    </code-block>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
                        &nbsp;
                    jobs:
                        qodana:
                            runs-on: ubuntu-latest
                            permissions:
                                contents: write
                                pull-requests: write
                                checks: write
                            steps:
                                - uses: actions/checkout@v3
                                  with:
                                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                      fetch-depth: 0  # a full history is required for pull request analysis
                                - name: 'Qodana Scan'
                                  uses: %action-version%
                                  with:
                                      args: -u root
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
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
                                      -u root
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
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                    <code-block lang="yaml">
                        include:
                            - component: %gitlab-version%
                              inputs:
                                  args: |
                                      -u root
                                      --image &lt;image&gt;
                    </code-block>
                </tab>
            </tabs>
        </chapter>

        <chapter id="docker-config-reference-git-submodules" title="Git submodules">
            <p>To analyze repositories that use Git submodules accessed via SSH, you must authenticate Git
                operations within the Qodana Docker container. In this case, you need to configure an SSH agent and
                pass an SSH key with access to the submodule into the container. A configuration snippet for GitHub Actions is shown below:</p>
            <code-block lang="yaml" emphasize-lines="32-34">
                name: Qodana
                on:
                    workflow_dispatch:
                    pull_request:
                    push:
                        branches: # Specify your branches here
                            - main # The 'main' branch
                            - master # The 'master' branch
                            - 'releases/*' # The release branches
                jobs:
                    qodana:
                        runs-on: ubuntu-latest
                        permissions:
                            contents: write
                            pull-requests: write
                            checks: write
                        steps:
                            - uses: actions/checkout@v4
                              with:
                                  ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                                  fetch-depth: 0  # a full history is required for pull request analysis

                            - name: Setup SSH Agent
                              uses: webfactory/ssh-agent@v0.9.0
                              with:
                                  ssh-private-key: ${{ secrets.SUBMODULE_SSH_KEY }}

                            - name: 'Qodana Scan'
                              uses: JetBrains/qodana-action@v2026.1
                              with:
                                  args: |
                                      -v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock
                                      -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock
                                      -e "GIT_SSH_COMMAND=ssh -o StrictHostKeyChecking=no"
                                  upload-result: true
                                  pr-mode: 'true'
                              env:
                                  QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
            </code-block>
            <p>This command contains the following options:</p>
            <table>
                <tr>
                    <td>Option</td>
                    <td>Description</td>
                </tr>
                <tr>
                    <td><code>-v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock</code></td>
                    <td>Mount the SSH agent socket into the container</td>
                </tr>
                <tr>
                    <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
                    <td>Set the SSH agent socket environment variable</td>
                </tr>
                <tr>
                    <td><code>-e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;</code></td>
                    <td>Disable strict host key checking for SSH operations</td>
                </tr>
            </table>
            <!--<tabs group="cli-settings">
                <tab title="Docker image" group-key="docker-image">
                    <code-block lang="shell" prompt="$">
                        docker run \
                           -v $(pwd):/data/project/ \
                           -v "$SSH_AUTH_SOCK:/tmp/ssh_agent.sock" \
                           -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock \
                           -e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot; \
                           -e QODANA_SKIP_SUBMODULE_UPDATE=true \
                           jetbrains/qodana-&lt;image&gt; \
                           --diff-start=&lt;GIT_START_HASH&gt;
                    </code-block>
                    <p>This command contains the following options:</p>
                    <table>
                        <tr>
                            <td>Option</td>
                            <td>Description</td>
                        </tr>
                        <tr>
                            <td><code>-v "$SSH_AUTH_SOCK:/tmp/ssh_agent.sock"</code></td>
                            <td>Mount the SSH agent socket into the container</td>
                        </tr>
                        <tr>
                            <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
                            <td>Set the SSH agent socket environment variable</td>
                        </tr>
                        <tr>
                            <td><code>-e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;</code></td>
                            <td>Disable strict host key checking for SSH operations</td>
                        </tr>
                        <tr>
                            <td><code>-e QODANA_SKIP_SUBMODULE_UPDATE=true</code></td>
                            <td>Skip Git submodule checkout, can be useful if the submodule checkout fails</td>
                        </tr>
                        <tr>
                            <td><code>--diff-start=&lt;GIT_START_HASH&gt;</code></td>
                            <td>Commit hash, see the <a href="analyze-pr.md" anchor="Analyze+pull+and+merge+requests"/> chapter for details</td>
                        </tr>
                    </table>
            </tab>
                <tab title="Qodana CLI" group-key="qodana-cli">
                    <code-block lang="shell" prompt="$">
                        qodana scan \
                           -v "$SSH_AUTH_SOCK:/tmp/ssh_agent.sock" \
                           -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock \
                           -e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot; \
                           -e QODANA_SKIP_SUBMODULE_UPDATE=true \
                           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                           --diff-start=&lt;GIT_START_HASH&gt;
                    </code-block>
                    <p>This command contains the following options:</p>
                    <table>
                        <tr>
                            <td>Option</td>
                            <td>Description</td>
                        </tr>
                        <tr>
                            <td><code>-v "$SSH_AUTH_SOCK:/tmp/ssh_agent.sock"</code></td>
                            <td>Mount the SSH agent socket into the container</td>
                        </tr>
                        <tr>
                            <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
                            <td>Set the SSH agent socket environment variable</td>
                        </tr>
                        <tr>
                            <td><code>-e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;</code></td>
                            <td>Disable strict host key checking for SSH operations</td>
                        </tr>
                        <tr>
                            <td><code>-e QODANA_SKIP_SUBMODULE_UPDATE=true</code></td>
                            <td>Skip Git submodule checkout, can be useful if the submodule checkout fails</td>
                        </tr>
                        <tr>
                            <td><code>--diff-start=&lt;GIT_START_HASH&gt;</code></td>
                            <td>Commit hash, see the <a href="analyze-pr.md" anchor="Analyze+pull+and+merge+requests"/> chapter for details</td>
                        </tr>
                    </table>
                </tab>
                <tab title="GitHub Actions" group-key="github-actions">
                <code-block lang="yaml">
        jobs:
            qodana-job:
                runs-on: ubuntu-latest
                steps:
                    - name: Checkout Repository
                      uses: actions/checkout@v4
                      with:
                          submodules: recursive  # clones submodules recursively

                    - name: Setup SSH Agent
                      uses: webfactory/ssh-agent@v0.9.0
                      with:
                          ssh-private-key: ${{ secrets.SUBMODULE_SSH_KEY }}

                    - name: 'Qodana Scan'
                      uses: %action-version%
                      with:
                          args: |
                              -v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock
                              -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock
                              -e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;
                              -e QODANA_SKIP_SUBMODULE_UPDATE=true
                          upload-result: true
                          pr-mode: 'true'
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
                    <p>Here, the <code>args</code> block contains the following options:</p>
                    <table>
                        <tr>
                            <td>Option</td>
                            <td>Description</td>
                        </tr>
                        <tr>
                            <td><code>-v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock</code></td>
                            <td>Mount the SSH agent socket into the container</td>
                        </tr>
                        <tr>
                            <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
                            <td>Set the SSH agent socket environment variable</td>
                        </tr>
                        <tr>
                            <td><code>-e GIT_SSH_COMMAND=ssh -o StrictHostKeyChecking=no</code></td>
                            <td>Disable strict host key checking for SSH operations</td>
                        </tr>
                        <tr>
                            <td><code>-e QODANA_SKIP_SUBMODULE_UPDATE=true</code></td>
                            <td>Skip Git submodule checkout, can be useful if the submodule checkout fails</td>
                        </tr>
                    </table>
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
                <code-block lang="yaml">
                    include:
                        - component: %gitlab-version%
                          inputs:
                              image: &lt;image&gt;
                              args: |
                                  -v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock
                                  -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock
                                  -e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;
                                  -e QODANA_SKIP_SUBMODULE_UPDATE=true
                </code-block>
                    <p>Here, the <code>args</code> block contains the following options:</p>
                    <table>
                        <tr>
                            <td>Option</td>
                            <td>Description</td>
                        </tr>
                        <tr>
                            <td><code>-v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock</code></td>
                            <td>Mount the SSH agent socket into the container</td>
                        </tr>
                        <tr>
                            <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
                            <td>Set the SSH agent socket environment variable</td>
                        </tr>
                        <tr>
                            <td><code>-e GIT_SSH_COMMAND=ssh -o StrictHostKeyChecking=no</code></td>
                            <td>Disable strict host key checking for SSH operations</td>
                        </tr>
                        <tr>
                            <td><code>-e QODANA_SKIP_SUBMODULE_UPDATE=true</code></td>
                            <td>Skip Git submodule checkout, can be useful if the submodule checkout fails</td>
                        </tr>
                    </table>
                </tab>
            </tabs>-->
        </chapter>


    </chapter>

    <chapter id="docker-config-reference-qodana-cli" title="Cache in Qodana CLI">

        <p><a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> stores files in the
            <code>&lt;userCacheDir&gt;</code> directory, which is mentioned several times throughout this section. Here
            is the list of <code>&lt;userCacheDir&gt;</code> directory locations depending on the operating system:
        </p>

        <table>
            <tr>
                <td>Operating System</td>
                <td>Path</td>
            </tr>
            <tr>
                <td>macOS</td>
                <td><code>~/Library/Caches/</code></td>
            </tr>
            <tr>
                <td>Linux</td>
                <td><code>~/.cache/</code></td>
            </tr>
            <tr>
                <td>Windows</td>
                <td><code ignore-vars="true">%LOCALAPPDATA%\</code></td>
            </tr>
        </table>

        <p>If you run the <code>qodana init</code> command in the project directory, Qodana CLI will let you choose
            the <a href="linters.md">linter</a> that will be run during inspection, and save the choice in
            <code>qodana.yaml</code>. Once done, you do not need to specify the linter in the commands, which is
            shown throughout this section.</p>

        <p>The detailed description of the <code>qodana init</code> command is available in the
            <a anchor="docker-config-reference-qodana-init"/> section.</p>

    </chapter>
