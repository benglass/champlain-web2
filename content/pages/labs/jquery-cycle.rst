Creating a Slideshow using the jQuery Cycle Plugin
##################################################

:date: 2014-02-10 15:00:00
:tags: lab, javascript, jquery, plugin, cycle, slideshow
:author: Ben Glassman
:hidden: 1

The jQuery javascript library makes it easier to add interactive javascript to your HTML websites.
There are thousands of jQuery plugins freely available (and just as many which you can purchase)
which add functionality to the jQuery library such as Slideshows, Lightboxes, Tabs, Expand/Collapse
and more. This lab will show you how to use the popular `jQuery Cycle Plugin <http://jquery.malsup.com/cycle2/>`_ to add an animated slideshow to your page. We will build a slideshow of upcoming shows at a venue. 

1. Create a new html file with opening and closing html tags and save it as **jquery-cycle.html**
   Add a **head** section with a **title** tag with the text **jQuery Cycle**
   Add a **body** tag

2. We first need to populate our slideshow with content. Create a **div** with an **id** of **slideshow**
   in the **body** tag

.. code-block:: html

    <div id="slideshow">
    </div>

3. Create an **unordered list** inside the **#slideshow** div. You will add a new **list item** for each
   slide in the slideshow.

.. code-block:: html

    <div id="slideshow">
        <ul>
        </ul>
    </div>

4. Add a **list item** to the **unordered list** for the first slide.

.. code-block:: html

    <div id="slideshow">
        <ul>
            <li>
            </li>
        </ul>
    </div>

5. Each slide will include a **heading** with the name of the artist followed by a **paragraph** with
   a description. The description text will include a **link** to a detail page for the show. Create
   a **div** with a **class** of **content**. Add a **level 2 heading** and **paragraph** with the
   content described above. You can copy the content from the `Higher Ground Website <http://www.highergroundmusic.com>`_, including images. Save images to a new folder called **images**.

.. code-block:: html

    <div id="slideshow">
        <ul>
            <li>
                <div class="content">
                    <h2>Artist Name</h2>
                    <p>Description of the artist <a href="#">Read more</a></p>
                </div>
            </li>
        </ul>
    </div>

6. Each slide will also include an **image** of the artist. Add an **img** tag after the **.content** 
   div and set the **src** and **alt** attributes. Remember to include **images/** before the filename
   in the **src** attribute so the browser knows the look inside our **images** folder.
   
.. code-block:: html

    <div id="slideshow">
        <ul>
            <li>
                <div class="content">
                    <h2>Artist Name</h2>
                    <p>Description of the artist <a href="#">Read more</a></p>
                </div>
                <img src="images/artist-image.jpg" alt="Artist Name" />
            </li>
        </ul>
    </div>

7. Repeat steps 4-6 to create 2 additional slides for the slideshow.

8. Create a new css file and save it as **styles.css**
   **Note**: Make sure you save it in the same folder as your HTML file.

9. Link the css file to your html file by adding the following code to the <head> of your HTML file:

.. code-block:: html

    <link href="styles.css" rel="stylesheet" type="text/css" />

10. Remove the margins and padding from the **unordered list** inside of the **#slideshow** by 
    setting them to 0. Remove the bullets by setting **list-style** to **none**

.. code-block:: css

    #slideshow ul {
        margin: 0;
        padding: 0;
        list-style: none;
    }

11. We will use absolute positioning to position the description of the show (the **.content** div)
    on top of the image and move it to the bottom of the slide.

.. code-block:: css

    #slideshow .content {
        position: absolute;
        left: 0;
        bottom: 0;
    }

12. Preview your file in the browser and you will notice that all of the **.content** is stacked on top
    of each other. This is because they are all being positioned relative to the **body**. To position
    them relative to the slide they are in, we will set the **position** to **relative** on each of the
    **list items** in the **#slideshow**.

.. code-block:: css

    #slideshow li {
        position: relative
    }

13. With this change, our text is positioned at the bottom of each slide. Right now the slides are
    taking up as much width as is available. We want the slideshow to be the same size as the images we used
    so set the **#slideshow** **width** to the width of the images you used.

.. code-block:: css

    #slideshow {
        width: 658px;
    }

14. To make the **.content** text readable regardless of the image used, we will set the **background color**
    to white at 50% transparency. We can do this using the rgba method of specifying color, where we specify the
    red, green, blue and alpha (transparency). The alpha value is between 0 and 1 where 0 is completely transparent and 1 is 100% opaque.

.. code-block:: css

    #slideshow .content {
        background-color: rgba(255, 255, 255, 0.5);
    }

15. Give the text content some room to breathe by adding padding to the **.content** div.
    You can use the shorthand for padding where you specify 2 values and the first is used for
    top and bottom and the second is used for left and right.

.. code-block:: css

    #slideshow .content {
        padding: 5px 15px;
    }


16. Now that we have applied basic styling to our slideshow, we are ready to use the jQuery Cycle plugin
    to enable to slideshow effect. Go to the `jQuery Cycle Plugin Website <http://jquery.malsup.com/cycle2/>` 
    and download the **Production** version of the plugin (it is compressed to make it download faster). Go to
    the downloads page and right click on the download button and choose **Save Link As**. Save this file as
    **jquery.cycle.js** in the same folder as your website.

17. At the bottom of your HTML page, right before the closing **body** tag, add a **script** tag and set
    the **src** attribute to **jquery.cycle.js** and the **type** attribute to **text/javascript** because
    the script you are attaching is a jQuery plugin, which is javascript.

.. code-block:: html

    <script src="jquery.cycle.js" type="text/javscript"></script>
    </body>

18. Preview the result in your brower and open up the **Web Developer Toolbar** by right clicking on the page
    and selecting **Inspect Element** or by hitting the **f12** key on your keyboard. Go to the **Console** tab.
    Refresh the page and you should see an error that says **Error: ReferenceError: jQuery is not defined**.
    The error could also say **$ is not defined** since $ is just a shortcut to jQuery. Whenever you see this
    error your browser is telling you that some javascript code is trying to use the jQuery library but
    it doesn't exist. In our case this is because we haven't added it to the page.

19. You can either download jQuery from the `jQuery website <http://www.jquery.com>`_ or you can use a
    **CDN** (Content Delivery Network) that will host jQuery for you and just link directly to that.
    Go to the `CDNJS Website <http://cdnjs.com/>`_ which hosts many javascript libraries. Search for **jquery**
    and scroll down until you find just plain **jquery**. You may notice they also host the jquery cycle plugin we are using. Click on the name **jquery** when you find it. From the jQuery page you end up on, you can see
    a list of all the versions of jquery they support. We want to use the latest version of **jQuery 1** which
    as of the time of this writing is **1.11.0**. Copy the URL from this page and insert a new script tag ABOVE the last one with the **src** set to the url. **Make sure to add http:// in front of the url or the file
    will not load properly while you viewing it in your browser**.

.. code-block:: html

    <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.0/jquery.min.js" type="text/javascript"></script>
    </body>

20. Not that you have jQuery and the Cycle plugin attached to your page, you can initialize your slideshow.
    Add another **script** tag after the last 2 but do not set a **src** attribute. You can add javascript
    code inside the script tags and it will be executed. You need to select the **unordered list** inside of **#slideshow** and initiaize the **cycle** plugin on it.

.. code-block:: html

    <script type="text/javascript">
    $('#slideshow ul').cycle();
    </script>

21. Preview the result in your browser and you will see the slideshow is functioning. Try moving the script tag into the **head** of the document and reloading the page. You will see it does not work because jquery and the cycle plugin have not loaded yet. Another reason this would not work is that the code is executed immediately in the html, so if it is placed in the **head** the **#slideshow** html has not loaded yet and it will not work. You can get around this by wrapping your javascript in some special jquery code that says "wait until the page has loaded and run this code". You can see an example of this code below but it is generally best to just include your javascript right before the closing body tag because the page has loaded at that point and it will also speed up page rendering because the javascript is loaded last.

.. code-block:: javascript

    $(document).ready(function() {
        $('#slideshow ul').cycle();
    });

22. What if we want to customize our slideshow, for example we want to increase the speed? This is generally achieved with jQuery plugins by passing in some options when we initialize the plugin. To see what options are available, visit the `jQuery Cycle API Page <http://jquery.malsup.com/cycle2/api/>`_. Generally you find will find this info by searching for a page called Documentation or Options or API. Reading through the options we can see there is a **timeout** option which is a number of milliseconds (thousandths of a second) between slide transitions. The default is list as **4000** (4 seconds). So to speed it up, lets change it to **2000**

.. code-block:: html

    <script type="text/javascript">
    $('#slideshow ul').cycle({
        timeout: 2000
    });
    </script>

23. What if we want to add a pager? There is an option called **pager** which is a **css selector** for an html
    element that the plugin will insert pagination links into. Lets add a **div** with a **class** of **pager**
    to the **#slideshow** div and set the **pager** option to **#slideshow .pager**. The **.pager** div should
    be empty because the cycle plugin will figure out how many pages we have an insert the html needed.

.. code-block:: html

    <div id="slideshow">
        <div class="pager"></div>
    </div>

    <script type="text/javascript">
    $('#slideshow ul').cycle({
        timeout: 2000,
        pager: '#slideshow .pager'
    });
    </script>

24. Preview the result in your browser and you see see numbered pagination links below your slideshow. Clicking on them will change the current slide. Right click on the pagination and choose **Inspect Element**. Explore the HTML that the plugin inserted. You can see it has inserted links into the **.pager** div we created and that
    whichever one is for the current slide has an **.activeSlide** class applied to it which changes as the slides transition. This allows us to style the active page differently using css.

25. Try to emulate the styles shown below by editing your HTML/CSS.

.. raw:: html
                
    <p data-height="690" data-theme-id="0" data-slug-hash="oCcyK" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/oCcyK'>oCcyK</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
