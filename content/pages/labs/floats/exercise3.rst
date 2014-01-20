CSS Floats Exercise 3: Complex Floats with Clearing
###################################################

:date: 2014-01-19 15:00:00
:tags: floats, css, lab
:author: Ben Glassman
:hidden: 1

A list of items each of which includes an image is a common layout
requirement for websites. Examples include a list of staff bios with headshots,
a list of products with thumbnails or a list of portfolio items with thumbnails.
Follow the instructions below to create a list of staff bios with headshots.

1. First create an HTML and CSS page and link them together using a **link** tag in the head of the html page.

2. In the body tag of your HTML file, add a section tag with a class of **staff-list**

.. code-block:: html

    <body>
        <section class="staff-list">
        </section>
    </body>

3. Add an **article** tag with a class of **staff** to the **section** tag

.. code-block:: html

    <section class="staff-list">
        <article class="staff">
        </article>
    </section>

4. Add **div** tag with a class of **headshot** with an **img** tag inside it.
   The **img** tag should include both a **src** attribute with the image filename/url
   and an **alt** attribute with the person's name.
   **Note** You can use a website like `PlaceCage <http://www.placecage.com/>`_ to generate the image

.. code-block:: html

    <section class="staff-list">
        <article class="staff">
            <div class="headshot">
                <img src="http://www.placecage.com/c/140/200" alt="Nicholas Cage" />
            </div>
        </article>
    </section>

5. Add an **h2** tag to the **article** with a person's name

.. code-block:: html

    <section class="staff-list">
        <article class="staff">
            <div class="headshot">
                <img src="http://www.placecage.com/c/140/200" alt="Nicholas Cage" />
            </div>
            <h2>Nicholas Cage</h2>
        </article>
    </section>

6. Add a **p** tag to the **article** with a bio of the person.
   **Note** You can use a website like `Lipsum <http://lipsum.com/>`_ to generate dummy bio text

.. code-block:: html

    <section class="staff-list">
        <article class="staff">
            <div class="headshot">
                <img src="http://www.placecage.com/c/140/200" alt="Nicholas Cage" />
            </div>
            <h2>Nicholas Cage</h2>
            <p>... bio text here ...</p>
        </article>
    </section>

7. Copy and paste the **article** tag 2 more times inside the **section** tag and update the 
   image and heading to use a different person's name. You should now have 3 different bios in your HTML.

8. In your **css file**, add css that makes the class of **headshot** float to the left

.. code-block:: css

    .headshot {
        float: left;
    }

9. Looking at the result in your browser, you should see that each of the bios is wrapping around the previous bio (example below). This is because we told the **headshot** to float and so any subsequent html tags are wrapping around it.
   This is not the layout we want, so how to do fix it?

.. raw:: html

    <p data-height="593" data-theme-id="0" data-slug-hash="Fngwz" data-default-tab="result" class='codepen'>See the Pen <a href='http://codepen.io/benglass/pen/Fngwz'>Fngwz</a> by Ben Glassman (<a href='http://codepen.io/benglass'>@benglass</a>) on <a href='http://codepen.io'>CodePen</a>.</p>

10. Using the css property **clear** we can tell the browser to stop wrapping content around any previous floats.
    For each **bio**, we don't want it to wrap around any previous floats from the other bios so we tell each **bio**
    to **clear** any previous floats. Add css that sets **clear** to **left** for the **bio** class. 
    **Note** We set **clear** to **left** because the floats we are trying to clear are **float: left**. You can also set clear to **right** (to clear only **float: right**) or to **both** to clear both. **both** is almost always fine.

.. code-block:: css

    .bio {
        clear: left;
    }

11. Now that bios dont float around other bios, our layout is looking closer to how we want it.
    We would like to add some space between the bios, so lets add a CSS rule to add 15px of bottom margin to each **.bio**

.. code-block:: css

    .bio {
        /* Existing rules */
        margin-bottom: 15px;
    }

12. You will notice when you look in your browser that the last step didn't do anything, but why?
    In order to understand how our layout is working, lets add a big green border to the **.bio**
    so we can see why our margin isn't working.
    
.. code-block:: css

    .bio {
        /* Existing rules */
        border: 5px solid green;
    }

13. Looking at the layout with our green border, we can see that the **.bio** doesnt seem to wrapping
    around the **.headshot**, but why? This is because of how the **float** property works in CSS.
    When you float something in css (the **.headshot**) any parent html tags (the **.bio**) no longer
    wrap around it unless they are also floated or unless any floats inside the parent tag (**.bio**) 
    has been cleared. Lets add **float: left** to the **.bio** to resolve this issue

.. code-block:: css

    .bio {
        /* Existing rules */
        float: left;
    }

14. Previewing our changes you can now see that the **.bio** (the green box) is wrapping around the 
    **.headshot** and the **margin** we specified is being added properly. Lets remove the green
    border.
    **Note** Another convenient way to diagnose these kinds of layout problems is to use the **Chrome Developer Tools**.
    Rigth click on the bio and choose **Inspect Element**. This will open the developer tools and also 
    highlight the element on the page, showing you the space it is taking up and any margins (orange) and padding (yellow)
    assigned to it.

15. To finish the layout, lets add right and bottom margin to the **.headshot**
    so that the heading and bio text does not directly touch it.

.. code-block:: css

    .headshot {
        /* Existing rules */
        margin-right: 15px;
        margin-bottom: 15px;
    }
