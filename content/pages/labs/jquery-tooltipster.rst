Custom Tooltips with jQuery Tooltipster
#######################################

:date: 2014-03-23 15:00:00
:tags: lab, javascript, jquery, plugin, tooltips
:author: Ben Glassman
:hidden: 1

The jQuery javascript library makes it easier to add interactive javascript to your HTML websites.
There are thousands of jQuery plugins freely available (and just as many which you can purchase)
which add functionality to the jQuery library. `Tooltipster <http://iamceege.github.io/tooltipster/>`_ is a plugin
which makes it easy to add custom tooltips to sections of your website.

.. raw:: html

    <p data-height="150" data-theme-id="0" data-slug-hash="muerj" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/muerj/'>muerj</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>

1. Create a new html file with opening and closing html tags and save it as **jquery-tooltip.html**
   Add a **head** section with a **title** tag with the text **jQuery Tooltip**
   Add a **body** tag

2. The first step when we want to use a jQuery plugin is to include jQuery itself.
   Go to http://jquery.com and click on **Download**. Scroll town to the section called
   **Using jQuery with a CDN**. Copy the code for the latest version of jQuery
   and paste it into your html page, right before the closing **body** tag.

.. code-block:: html

        <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    </body>
    </html>

3. Now we need to download the jQuery plugin we want to use and attach it to the page.
   Go to to the `jQuery Tooltipster Plugin website <http://iamceege.github.io/tooltipster>`_
   and click **Download**. Unzip the file into the same folder where you saved your html file.
   Make sure the folder where all of the jquery tooltipster files are created is called **tooltipster**. 
   Rename it if necessary.

4. Now that we have downloaded the plugin, we need to add the javascript file and the css file
   containing the styles to our html page. **AFTER** the script tag we added in step 2, add another
   script tag with the src set to **tooltipster/js/jquery.tooltipster.js**. **NOTE** It is important
   that we place this AFTER the jquery script tag since it is a jquery plugin and requires jquery.

.. code-block:: html

        <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
        <script src="tooltipster/js/jquery.tooltipster.js"></script>
    </body>
    </html>

5. Some jQuery plugins come with their own stylesheets. This will usually be noted in the installation
   instructions. Lets add the stylesheet for jquery tooltipster to **head** of our html page.


.. code-block:: html

    <head>
        <title>jQuery Tooltip</title>
        <link type="text/css" rel="stylesheet" href="tooltipster/css/tooltipster.css" />
    </head>

6. Now that we have the javascript and css files attached, we can use the plugin! To make sure the scripts and
   styles are loaded properly open the html file in your browser. Right click on the screen and click **View Page Source**.
   From the page source, we can right click on the filenames for jquery, jquery tooltipster and the css file we added.
   For each one, right click on it and choose **Open Link in New Tab**. Check the tab that opens and make sure you see
   the file there. If you see an error page then the file is not loading correctly. Check the urls/filenames from steps 2-5.

7. Now that we know that jquery, the tooltipster plugin and the required css are all loading correctly, lets hook up our plugin.
   Create a new link in the **body**. Set the **href** attribute to **http://www.benglassman.com** and the **title** attribute
   to **Web 2 Course Website with Syllabus and Course Resources**. Add a **class** of **tooltip** to the anchor tag. 
   Set the text of the link to **Visit BenGlassman.com**.

.. code-block:: html

    <a href="http://www.benglassman.com" title="Web 2 Course Website with Syllabus and Course Resources" class="tooltip">Visit BenGlassman.com</a>

8. Open the html file in your browser. Place your mouse on the link and you will see a box popup with the content we placed in the **title**
   attribute. The jQuery tooltip plugin lets us customize the way this tooltip appears.

9. We need to initialize the tooltip plugin on our link, so add another **script** tag before the closing **body** tag and **AFTER** both of the other script tags.
   In this **script** tag we will select the **anchor** using the **tooltip class** we added and turn it into a tooltip.


.. code-block:: html

    <script type="text/javascript">
        $('.tooltip').tooltipster();
    </script>

10. Open the file in your browser and test that the tooltip is appearing.

11. Now lets customize the animation of the tooltip. If we visit the `jQuery Tooltipster Options <http://iamceege.github.io/tooltipster/#options>`_ page of the
    plugin website we can see what options we have available for the plugin. You can see the option **animation** lets us change the animation of the tooltip.
    We can also see that the plugin uses the animation **fade** by default. Set the **animation** option to **grow** to change the animation.

.. code-block:: html

    <script type="text/javascript">
        $('.tooltip').tooltipster({
            animation: 'grow'
        });
    </script>

12. Open the file in your browser and you can see the popup now uses the grow animation.

13. If we want to really customize the tooltip that is displayed, we can make it use HTML instead of just plain text. Reading the options we can see this is done
    by passing a **content** option to the plugin and setting the **contentAsHTML option to **true**. Delete the **title** attribute from our html and move
    the text to the **content** option of the plugin. Make the words **Syllabus** and **Course Resources** bold using **strong** tags.

.. code-block:: html

    <script type="text/javascript">
        $('.tooltip').tooltipster({
            animation: 'grow',
            content: 'Web 2 Course Website with <strong>Syllabus</strong> and <strong>Course Resources</strong>',
            contentAsHTML true
        });
    </script>

14. Open the result in your browser and you should see the content now has bolded words and is rendered as html.
