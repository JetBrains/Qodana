# Overview to IDE integration

<link-summary>%product% is available in JetBrains IDE products, as well as in Visual Studio Code and Visual Studio developed by Microsoft.</link-summary>

%product% is available in the following integrated development environment (IDE) products:

<table>
    <tr>
        <td>IDE product</td>    
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
            </list>
        </td>    
        <td>
            <p>Run %product% locally using your IDE.</p>
            <p>Upload reports to %product% Cloud.</p>
            <p>Download reports from %product% Cloud and explore them using your IDE.</p>
            <p>Open local %product% reports contained in SARIF-formatted files.</p>
        </td>    
        <td>
            <p>All functionalities related to %product% Cloud require a <a href="project-token.md">project token</a>.</p>
        </td>
    </tr>
    <tr>
        <td><a href="vscode.md">Visual Studio Code</a></td>    
        <td>
            <p>Run %product% locally using your IDE.</p>
            <p>Upload reports to %product% Cloud.</p>
            <p>Download reports from %product% Cloud and explore them using your IDE.</p>
        </td>  
        <td>
            <p>Requires the <a href="https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana-code">Qodana</a> extension and
                a %product% Cloud <a href="project-token.md">project token</a>.</p>
            <p>The Docker daemon should be up and running.</p>
        </td>
    </tr>
    <tr>
        <td><a href="visualstudio.md">Visual Studio</a></td>    
        <td>
            <p>Download reports from %product% Cloud and explore them using your IDE.</p>
        </td>    
        <td>
            <p>Requires <a href="https://www.jetbrains.com/resharper/">JetBrains ReSharper</a> and
                a %product% Cloud <a href="project-token.md">project token</a>.</p>
        </td>
    </tr>
</table>


<!-- Licensing needs to be explained here -->