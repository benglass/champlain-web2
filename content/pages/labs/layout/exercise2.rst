Layout Exercise 2: Multi Column CSS Layout
##########################################

:date: 2014-01-26 15:00:00
:tags: positioning, floats, css, lab, layout
:author: Ben Glassman
:hidden: 1

Using the **layout-skeleton.html** file we created in `Exercise 1 <{filename}labs/layout/exercise1.rst>`__
we will create a simple 2 column layout using css floats. We will use the css position property to handle
the layout of our masthead. Below is the layout we will be creating:

.. raw:: html

    <p data-height="955" data-theme-id="0" data-slug-hash="KEekl" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/KEekl'>KEekl</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>

Instructions
------------

1. Open **layout-skeleton.html** from exercise 1, save it was a new file called **layout-skeleton-styled.html**

2. Create a new css file and save it as **styles.css**
   **Note**: Make sure you save it in the same folder as your HTML file.

3. Link the css file to your html file by adding the following code to the <head> of your HTML file:

.. code-block:: html

    <link href="styles.css" rel="stylesheet" type="text/css" />

4. In your CSS file, add a **background color** to the **body** tag of **#cccccc** (light gray)

.. code-block:: css

    body {
        background-color: #cccccc;
    }

5. To center the website, we will add a **width** to the **container** and set the **left and right margins** to a
   special value **auto** which will evenly distribute available space between them.

.. code-block:: css

    #container {
        width: 960px;
        margin-left: auto;
        margin-right: auto;
    }

6. Set the **background color** for the **masthead** to **#333333** (dark gray)

.. code-block:: css

   #masthead {
       background-color: #333333;
   }

7. Set **position: absolute** on the **logo** and use the **top** and **left** css properties
   to position it **30 pixels from the top** and **30 pixels from the left**.
   **Note**: You may need to adjust the top and left values depending on the size of your logo

.. code-block:: css

    #logo {
      position: absolute;
      top: 30px;
      left: 30px;
    }

8. Preview the result in your browser, you will see that the logo is 30 pixels from the top and 30 pixels
   from the left of the entire browser window. We want to position it relative to the website, so we need
   to set **position** to **relative** on the container to make absolutey positioned elements within the 
   **container** be positioned **relative** to the top left corner of the **container**.

.. code-block:: css

   #container {
       position: relative;
   }

9. Preview the result in your browser, you will see that the **logo** is now positioned based on the top left
   corner of the centered website **container**. We have another problem to address, which is that our gray **masthead**
   area is not wrapping around the **logo**. This is because when you use **position: absolute** the element
   is removed from the normal layout of the site and placed in a layer on top of the rest of the layout. To solve
   this, prop the **masthead** open to the desired vertical height by setting the **height** to **170px**
   **Note**: You may need to adjust the height value depending on the desired height of the masthead

.. code-block:: css

   #masthead {
       height: 170px;
   }

10. Use the same technique of **absolute positioning** to position the **tagline** exactly **100 pixels** from the right
    of the website and **35 pixels** from the top.

.. code-block:: css

    #tagline {
      position: absolute;
      right: 100px;
      top: 35px;
    }

11. Make the tagline text color **white**, bold and set the **font size** to **24 pixels**

.. code-block:: css

    #tagline {
      color: #fff;
      font-size: 24px;
      font-weight: bold;
    }

12. We will skip over the navigation for the moment and work on creating a 2 column layout with the
    **content** and the **sidebar**. Whenever you want to create multi column layout in CSS you
    will want to use the **float** property combined with setting a **width**. Add styles to
    make the **content** element **float** to the **left** and give it a **width** of **70%**

.. code-block:: css

    #content {
        width: 70%;
        float: left;
    }

13. To finish the 2 column layout, make the **sidebar** element **float** to the **left** and
    give it a **width** of **30%**

.. code-block:: css

    #sidebar {
        width: 30%;
        float: left;
    }

14. Preview the file in the browser and you will see that we have achieved a 2 column layout.
    Right now there is no space between the 2 columns, so lets add some padding to our columns.
    Add **15 pixels** of **padding** to both the **sidebar** and the **content**

.. code-block:: css

    #content {
        padding: 15px;
    }

    #sidebar {
        padding: 15px;
    }

15. Preview the file in the browser and you can see that we have broken the 2 column layout. That is because
    the widths (70% + 30%) plus the left and right padding (15px * 4) is more than 100%. By default
    the browser will add the width and the padding to determine the final width of the element. This is
    not the most expected behavior and we can tell the browser to simply use the width we specified and
    subtract any padding from that by adding the following line to the top of our css file. It is recommended
    that you always add this line to prevent this unexpected issue.

.. code-block:: css

    * { box-sizing: border-box }

16. If you preview your file now, you can see that the footer is being affected by the floating of the **content**
    and **sidebar**. Since we do not want this, we can use the **clear** css property and
    set the value to **left** to ensure that the **footer** is not affected by the **content** and **sidebar**
    floats.

.. code-block:: css

    #footer {
      clear: both;
    }

17. Lets also add some padding around the content in our **footer** and **top border** to visually separate
    it from the **content** and **sidebar**.

.. code-block:: css

    #footer {
        padding: 25px;
        text-align: center;
        border-top: 5px solid #333;
    }

18. Now that the **content**, **sidebar** and **footer** are laid out properly, lets return to the **navigation**
    and apply some styling. The first step is to remove the default **margins**, **padding** and **bullets** from
    the **unordered list**.

.. code-block:: css

    #navigation ul {
        margin: 0;
        padding: 0;
        list-style: none;
    }

19. In order to achieve a horizontal layout for our **navigation** we will apply **float: left** to each of the **list items** in it.

.. code-block:: css

    #navigation li {
        float: left;
    }

20. Now lets apply a light gray **background color** to our **navigation unordered list** so it appears as a horizontal bar.

.. code-block:: css

    #navigation ul {
      background: #999999;
    }

21. When we preview our file, we cannot see the **background color** we just applied to the **unordered list**. This is because the **list items** are floated and the **unordered list** is not, so the **unordered list** does not wrap around the **list items**. To see how this is effecting the layout, add a **red border** to the unordered list and take a look in your browser. You will see a thin red line that indicates the **unordered list** is not wrapping around the floated **list items**.

.. code-block:: css

    #navigation ul {
        border: 1px solid red;
    }

22. To fix the layout issue lets add a **float: left** to the **unordered list**. 
    
.. code-block:: css

    #navigation ul {
        float: left;
    }

23. Previewing this in your browser you can see that the **unordered list** is now wrapping around the **list items** but we still cannot see the **background color** because it is now exactly the **width** of the items. Fix this by setting the **width** to **100%** on the **unordered list**.

.. code-block:: css

    #navigation ul {
        width: 100%;
    }

24. To make our navigation links easier to click, lets add some padding around them

.. code-block:: css

    #navigation a {
        padding: 15px;
    }

25. Preview this in your browser and you can see that the left and right padding was added but not the top and bottom.
    This is because HTML tags like **a**, **strong** and **em** cant have top and bottom padding added to them unless
    you either set **float** on them or set **display: block**. Lets float the **a** tags to the left to fix this.

.. code-block:: css

    #navigation a {
        float: left;
    }

26. The clickable area is now larger for our navigation, making it easier to use. Lets remove the underline from them
    by setting **text-decoration** to **none**

.. code-block:: css

    #navigation a {
        text-decoration: none;
    }

27. Lets add some interactivity when the users hover over our links. We will make the **background color** change from 
    **black** to **red** and the **color** change from **white** to **black**. Add a css rule to set the **background color** to **black** and the **color** to **white** for **visited** and **unvisited** links.
    **Note** We are using the **comma** to combine 2 separate **css selectors**

.. code-block:: css

    #navigation a:link, #navigation a:visited { color: white; background-color: black; }


28. Add a rule that sets the **background color** to **red** and the **color** to **black** when the links are **hovered** or **active**

.. code-block:: css

    #navigation a:hover, #navigation a:active { color: black; background-color: red; }
