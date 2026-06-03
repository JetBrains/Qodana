# Overview of IDE support

<link-summary>%product% is available in JetBrains IDE products, as well as in Visual Studio Code and Visual Studio developed by Microsoft.</link-summary>

Using %product% in your IDE lets you study code problems without having to switch to other applications. %product% 
functionalities are available in the following integrated development environment (IDE) products:

<table>
    <tr>
        <td>IDE</td>    
        <td>Functionalities</td>
        <td>Prerequisites</td>
    </tr>
    <tr>
        <td>
            <p><a href="qodana-ide-plugin.md">JetBrains IDEs</a>:</p>
            <list>
                <li>IntelliJ IDEA</li>
                <li>PhpStorm</li>
                <li>WebStorm</li>
                <li>GoLand</li>
                <li>PyCharm</li>
                <li>Rider</li>
                <li>CLion</li>
            </list>
        </td>    
        <td>
            <list>
                <li><p>Run %product% locally using your IDE (not available in CLion)</p></li>
                <li><p>Upload reports to %cloud% (not available in CLion)</p></li>
                <li><p>Download reports from %cloud% and explore them using your IDE</p></li>
                <li><p>Open local %product% reports contained in SARIF-formatted files</p></li>
            </list>
        </td>    
        <td>
            <p>All functionalities related to uploading data to %cloud% require a <a href="project-token.md">project token</a>.</p>
        </td>
    </tr>
    <tr>
        <td><a href="vscode.md">Visual Studio Code</a></td>    
        <td>
            <p>Run %product% locally using your IDE.</p>
            <p>Upload reports to %cloud%.</p>
            <p>Download reports from %cloud% and explore them using your IDE.</p>
        </td>  
        <td>
            <p>Requires the <a href="https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana-code">%product%</a> extension and
                a %cloud% <a href="project-token.md">project token</a>.</p>
            <p>The Docker daemon should be up and running.</p>
        </td>
    </tr>
    <tr>
        <td><a href="visualstudio.md">Visual Studio</a></td>    
        <td>
            <p>Download reports from %cloud% and explore them using your IDE.</p>
        </td>    
        <td>
            <p>Requires <a href="https://www.jetbrains.com/resharper/">JetBrains ReSharper</a> and
                a %product% Cloud <a href="project-token.md">project token</a>.</p>
        </td>
    </tr>
</table>


<!-- Licensing needs to be explained here -->