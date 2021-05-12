[//]: # (title: UI Overview)

The current version of Qodana UI focuses on the single-shot analysis. It allows browsing and acting on results as well as reconfiguring the list of checks.

In this section, you will learn how to configure HTML report parameters and track detected problems in files. For information on how to open such reports in your browser, see [HTML Report](html-report.md).

## HTML report structure

1. **Sunburst diagram**   
  The interactive sunburst diagram gives you an idea of how bad the situation is, what problems are the most prominent, and lets you drill down into the cause of the issue. This chart is a result of our initial research and experiments. We believe that this visual representation dramatically enhances understanding of the data, which allows us to create more insightful views. 
   
2. **Filter set**

    To the right of the sunburst diagram, you can specify the files and folders, the linter, types and categories of problems.
3. **Checks total and configuration**

    For more information, see [Adjust your inspection profile](#Adjust+your+inspection+profile) below.
   [//]: # "check the link"
3. **Problem explorer**

4. **File explorer**

5. **Decorated code fragment**
    
    When you click a problem detected in your project, the code fragment that contains the problem  is displayed. Parts that require your attention are highlighted.

    Code duplicates detected by Clone Finder are displayed in a [diff view](clone-finder-output.md#A+sample+decorated+diff), which is also decorated to make it easy to compare several copies.  

![](general.png)

Below the function diff in the Problem and File explorers, you can
* **Open the respective file in the IDE**
 
  If you have JetBrains Toolbox installed, click the **Open file in IDE** button to open the file you are viewing in the editor.
  
* **Remove this item and similar problems from the future analysis**
    
  For more information, see [Adjust the analysis scope](#Adjust-the-analysis-scope) below.
  [//]: # "check the link"

## Adjust your inspection profile 

We believe that the ability to see what was checked is as important as the list of problems found. For example, if you haven't checked for 
typos, you can be happy to see zero typos in your project. There could be many of them&mdash;you just don't check. 

In the **Checks** section, you can see what's included in the analysis and  explore what you can add. Our recommended profile includes the most common inspections, but as you know your project better&mdash;you can fine-tune your 
experience. 

![](profile-settings.png)

You can *Enable* the inspection, and it will be added to your configuration. The UI will remind you to download and save `qodana.yaml` into your project root directory.

![](profile-save.png)

Run the analysis again with the updated `qodana.yaml` and check that you see the expected results. 

If the number of errors is manageable, you can fix them and consider the 'problem-free code' goal achieved. You are now ready to perform the 
analysis on a daily basis :) We suggest that you follow that goal and fix the errors as soon as they appear.

If there are too many errors, we suggest using the Qodana UI features to examine them. You can then formalize a not-so-big cluster of the problems to fix. Repeat the procedure to work on the next goal, and so on. 

We are working on the so-called *technical debt* support, which will help in the situation when you have no possibility to fix old problems but want to prevent the appearance of new ones. Stay tuned! 

## Adjust the analysis scope

When viewing a code fragment with a detected problem, you may decide that it is irrelevant. You can make sure that more problems of the same type are omitted in the future. 

1. Under the code fragment, click **More** and select the necessary option.

* **Exclude a file or directory from the future analysis**

  *Reason*: The analysis of the file containing the error, or even the directory containing this file, doesn't make sense in your project.
  For example, it's actually not the source code but some generated or downloaded content.

  *Howto*: Click the file path to navigate to File explorer where you can recheck the condition and mark the file/directory as **excluded**.

![](problem-area.png)
![](files-tree.png)


* **Hide a problem type or category from the list of problems**

  *Reason*: You suppose that the type of the error or its category is not relevant or want to get back to it later.  
  *Howto*: Use the **hide** action and remove the whole type or category.
  ![](problem-area-hide.png)

**Note**: If you excluded either type/category or file/directory, the UI will remind you to save the changes. Download the `qodana.yaml` file and store it under your project's root directory.