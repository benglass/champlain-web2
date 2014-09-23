CSS Buttons Lab: Using Background Images to Create Buttons
##########################################################

:date: 2014-01-26 15:00:00
:tags: floats, css, lab, background, button, rollover
:author: Ben Glassman
:hidden: 1

Whenever possible, it is ideal to design elements for your web page that
can be created in CSS using fonts, gradients, rounded corners and other native
styles. Sometimes we need to use fonts that are not web safe or introduce design
elements that cannot easily be achieved using css alone. A common technique in these
circumstances to set a background image on a button and change it when the user moves their
mouse over the button. This lab will review the steps used to achieve this technique.

1. Create a new html file with opening and closing html tags and save it as **css-button.html**

.. code-block:: html

    <html>
    </html>

2. Add the head and body tags inside the html tags. Include a title tag inside the head tags with the title "CSS Buttons"

.. code-block:: html

    <html>
        <head>
            <title>CSS Buttons</title>
        </head>
        <body>
        </body>
    </html>

3. Create a new css file and save it as **styles.css**
   **Note**: Make sure you save it in the same folder as your HTML file.

4. Link the css file to your html file by adding the following code to the <head> of your HTML file:

.. code-block:: html

    <link href="styles.css" rel="stylesheet" type="text/css" />

5. Inside the **body** tag of your HTML file, add a new link using the **a** tag.
   Set the **href** attribute to a url such as **http://www.woot.com**
   Set the **class** attribute to **btn-shop-now**
   Make the text of the button **Shop Now**

.. code-block:: html

   <a href="http://www.woot.com" class="btn-shop-now">Shop Now</a>

6. Using Photoshop, create a single image that contains both the normal button
   as well as the hover state. The image should be twice the height of the actual
   button with the normal button image stacked on top of the hover state.
   Create a folder called **images** in the same directory as your html/css files 
   and save this file as **btn-shop-now.png** into the **images** folder
   using **File > Save For Web**. Be sure to include the text for the button in the image.

.. figure:: ../images/btn-shop-now.png

   The image is twice the height of the actual button and the top 50%
   of the image is the normal button state. The bottom 50% is the rollover state.

7. Open **styles.css** and set the **background-image** to our new button image
   for the **btn-shop-now** class we added to our link. **Note** Whenever we refer
   to images in CSS, use the format **url(path/to/image.jpg)**.

.. code-block:: css

   .btn-shop-now {
       background-image: url(images/btn-shop-now.png);
   }

8. Preview the result in your browser and you will see the button image behind the text.
   Right now the link is only the size of the text we place in it. To make sure the button
   is the right size, we need to set the **height** and **width** on it to the dimensions
   of the button. You will need to use the right pixel dimensions based on the size of the button
   you designed. **Note** The height is half the size of the image because the image contains
   both the normal button and the rollover.

.. code-block:: css

   .btn-shop-now {
        width: 50px; /* Change to the width of your button */
        height: 25px; /* Change to the height of your button */
   }

9. Preview the result in your browser and you will notice the width and height have not been applied.
   This is because some HTML tags such as the **a** tag cannot have dimensions applied to them by default.
   Other examples of tags like this are **strong**, **em** and **span**. The reason for this is that these
   tags have **display: inline;** set on them by default. This is the reason that 2 **strong** tags will
   visually appear next to each other while 2 **div** tags will include line breaks above and below. **div** tags
   (as well as h1-h6, section, article, nav and many other tags) have **display: block** set on them by default.
   This inserts a line break above and below the tag and makes it take up 100% of the available width.
   We can assign dimensions to link tags by setting **display: block**. Add that style to the button.

.. code-block:: css

   .btn-shop-now {
        display: block;
   }

**Note**: You can also apply width/height to link tags by setting **float: left** or **float: right** because
setting **float** automatically sets **display: block**

10. Preview the result in your browser and you can see the button is now the right size. We can still
    see the text from our link, which we do not want because the text is included in the button image.
    We can hide the text by setting a large negative **text-indent** on the button which will pull the text
    far off the left side of the screen. Set **text-indent: -999em** on the button.

.. code-block:: css

   .btn-shop-now {
        text-indent: -999em;
   }

11. Now that the text is hidden, all that remains is for us to add our hover style to the button so that
    it changes when the user places their mouse over the button. We will achieve the hover effect by changing the **background-position** property to pull the background image up when the user mouses over the button. We want to 
    pull the background image upwards by the height of the image so that the lower half of our image is exposed.
    The animation below illustrates how this works. The blue box shows the dimensions of the button. Mouse over the button
    and you will see how the background images is repositioned to display the hover state. In this example the change
    is animated to illustrate how it occurs but in our case we will change this immediately when the user hovers over the button.

.. raw:: html

    <p data-height="127" data-theme-id="0" data-slug-hash="hirKx" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/hirKx'>hirKx</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>

12. In order to create our rollover effect, we need to use the **:hover**
    CSS selector to target the button **only** when the user has moused over it.
    Add a new selector to your css that only applies to the button when it is hovered.
   
.. code-block:: css

    .btn-shop-now:hover {
    }

13. To reposition the background image, we will use the **background-position** property.
    **background-position** takes 2 values, both of which are numbers with units (9px, 1em, 50%, etc.).
    The first value is the change to the horizontal positioning of the background image (for example
    -20px would pull the background image 20 pixels to the left while 50px would push it 50 pixels to the right.
    The second value is the change to vertical position. In this case we want to leave the horizontal position
    unchanged and pull the image up vertically by the height of the button. Use the **background-position**
    property to set the horizontal change to 0 and the vertical change to -50px where 50px is the height of your 
    button.
   
.. code-block:: css

    .btn-shop-now:hover {
        background-position: 0 -25px;
    }

14. Preview the result in your browser and you should see that hovering over the image now displays the correct
    part of the background image.

.. raw:: html

    <p data-height="82" data-theme-id="0" data-slug-hash="jALGH" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/jALGH'>jALGH</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
