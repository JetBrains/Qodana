[//]: # (title: UI Overview)

Qodana UI focuses on the single-shot analysis, making it easy to act on results and customize checks.

In this section, you will learn how to configure HTML report parameters and track detected problems in files. For information on how to open such reports in your browser, see [HTML Report](html-report.md).

## HTML report structure

![](general.png)

1. **Sunburst diagram**   
  The interactive sunburst diagram gives you an idea of how bad the situation is, what problems are the most prominent, and lets you drill down into the cause of the issue. 
   
2. **Filter set**

    To the right of the sunburst diagram, you can specify the files and folders, the linter, the types and categories of problems.
3. **Checks total and configuration**

    On top of the diagram, you can see the totals for detected problems and conducted checks as well as click the gear icon to [configure the inspection profile](#Adjust+your+inspection+profile).
   
[//]: # "check the link"
4. **Problem explorer**

    On the **Problems** tab below the sunburst diagram, detected problems are annotated, classified, and grouped by source files.

5. **File explorer**

   On the **Files** tab below the sunburst diagram, you can see the file tree of the analyzed project. You can get there also by clicking the respective path on top of the code fragment view.

6. **Code fragment view**
    
    When you click a problem detected in your project, the code fragment that contains the problem  is displayed. Parts that require your attention are highlighted.

    Code duplicates detected by Clone Finder are displayed in a multipanel [diff view](clone-finder-output.md#A+sample+decorated+diff), with code fragments decorated to make it easy to compare several copies.  

    Below the code fragment view in the Problem and File explorers, you can
    * **Open the respective file in the IDE**
     
      If you have JetBrains Toolbox installed, click the **Open file in IDE** button to jump to the respective file in the editor.
      
    * **Remove this item and similar problems from the future analysis**
        
      Click **More actions** and select the necessary option, as described in [Adjust the analysis scope](#Adjust+the+analysis+scope) below.
  
[//]: # "check the link"

## Adjust your inspection profile 

We believe that the ability to see what was checked is as important as the list of problems found. For example, if you haven't checked for 
typos, you can be happy to see zero typos in your project. There may be many of them&mdash;you just don't check. 

Click the gear icon next to the **Checks** total to see what's included in the analysis and  explore what you can add. Our recommended profile includes the most common inspections, but as you know your project better&mdash;you can fine-tune your 
experience. 

![](profile-settings.png)

Click an inspection to learn more about it and enable or disable it. The UI will remind you to download and save `qodana.yaml` into your project root directory.

![](profile-save.png)

Run the analysis again with the updated `qodana.yaml` and check that you see the expected results. 

If the number of errors is manageable, you can fix them and consider the 'problem-free code' goal achieved. You are now ready to perform the analysis on a daily basis :) We suggest that you follow that goal and fix the errors as soon as they appear.

If there are too many errors, we suggest using the Qodana UI features to examine them. You can then formalize a not-so-big cluster of the problems to fix. Repeat the procedure to work on the next goal, and so on. 

We are working on supporting the so-called *technical debt*, which will help in the situation when you have no possibility to fix old problems and want to prevent the appearance of new ones. Stay tuned! 

## Adjust the analysis scope

When viewing a code fragment with a detected problem, you may decide that it is irrelevant. You can make sure that more problems of the same type are omitted in the future:

* **Exclude a file or directory from the future analysis**

  *Reason*: The analysis of the file containing the error, or even the directory containing this file, doesn't make sense in your project.
  For example, it's actually not the source code but some generated or downloaded content.

  *Howto*: 
  
    - Under the code fragment view, click **More actions** and select the necessary option.
      
        OR:
  - Above the code fragment view, click the file path to navigate to File explorer where you can mark the file/directory as **excluded**.

![](problem-area.png)
![](files-tree.png)


* **Hide a problem type or category from the list of problems**

  *Reason*: You suppose that the type of the error or its category is not relevant or want to get back to it later.  
  *Howto*: Under the code fragment view, click More actions and select the necessary option.
  ![](problem-area-hide.png)

**Note**: If you exclude either type/category or file/directory, the UI will remind you to save the changes. Download the `qodana.yaml` file and store it under your project's root directory.