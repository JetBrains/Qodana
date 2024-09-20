[//]: # (title: Inspect code formatting)

You can use %product% to analyze whether your code adheres to correct formatting. Currently, %product% can analyze the
IntelliJ IDEA, Eclipse, and EditorConfig code style schemes. 

Follow these steps to configure formatting analysis. 

<procedure>
    <step>In your IDE, configure the project code style scheme that you would like to employ, see the 
        <a href="https://www.jetbrains.com/help/idea/configuring-code-style.html">IntelliJ IDEA documentation</a> as an example.
    </step>
    <step><p>In the <code>.idea/codeStyles</code> directory of your project, save the <code>codeStyleConfig.xml</code> 
            file containing the following configuration:</p>
        <code-block lang="xml">
            &lt;component name="ProjectCodeStyleConfiguration"&gt;
              &lt;state&gt;
                &lt;option name="USE_PER_PROJECT_SETTINGS" value="true" /&gt;
              &lt;/state&gt;
            &lt;/component&gt;
        </code-block>
    </step>
    <step>
        <p>In the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file, enable the <code>IncorrectFormatting</code> inspection:</p>
        <code-block lang="yaml">
            include:
              - name: IncorrectFormatting
        </code-block>
    </step>
</procedure>

Once all configurations are complete, you can run %product%.

