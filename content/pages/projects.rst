Mini Projects
#############

:date: 2014-01-04 13:09
:tags: projects
:author: Ben Glassman

There are 4 mini projects that comprise the first half of the semester.
The requirements for each one are described below.

.. class:: super-section

-----------------
Project 1: Resume
-----------------

Students will design and build an HTML/CSS version of their resume. 
This project focuses on HTML for content (paragraphs, headings, etc.)
and CSS for typography (font family, size, weight, color, etc.) and assignments
should demonstrate knowledge of this material.  This is a one page website and 
does not need to have any navigation.

Content
-------

The resume should include the following information/sections:

- Name
- Contact Info (Phone, Email, Website)
- Skills
- Education (At least one entry with the following information)

  + School Name
  + Degree
  + Dates Attended

- Employment History (At least 2 entries with the following information)

  + Employer
  + Job Title
  + Description
  + Dates

Design
------

Students will design their resume using Illustrator or Photoshop 
and submit the final design in PDF format. The design can be purely typographic
with no requirement for multi-column layout. Students must use a web-safe font or 
select a web font (free web fonts are available from `google <http://www.google.com/fonts>`_ and `adobe <http://html.adobe.com/edge/webfonts/>`_).

Production
----------

The HTML and CSS should demonstrate the following techniques:

HTML
````
- Use of <section> tags for each section (Skills, Education, Employment History)
- Use of <article> tags for each item with the section (School or Job)
- Skills will be marked up using an unordered list
- Use the <link> tag to link your external stylesheet.
- Proper use of heading tags (A single h1 with student name, h2 for each section heading, h3 for each job/school)

CSS
```
- Typographic Styles for paragraphs
- Typographic Styles 3 levels of headings (h1, h2, h3)
- Typographic Styles for links (unvisited, visited, hover, active)
- Typographic Styles for unordered lists

.. class:: super-section

------------------------
Project 2: Photo Gallery
------------------------

Students will design and build a photo gallery using HTML and CSS.
The photo gallery will include a display of thumbnail images that are clickable 
in order to view a larger size image with an associated title and description.
This project focuses on basic layout and must use either floats or absolute positioning
in CSS to lay out the thumbnails. Students will use javascript (such as a `jQuery Lightbox plugin <http://fancyapps.com/fancybox/>`_) in order to display the full size images with causing a reload of the page.

Content
-------

Students will include at 10 images in the photo gallery, with two different versions of each image 
(thumbnail and full size - the same image cannot be used as both the thumbnail and full size image). 

Design
------

Students will design their resume using Illustrator or Photoshop 
and submit the final design in PDF format. The design will demonstrate how thumbnails will be displayed
as well as how the full size image is displayed. This can be submitted as a 2-page PDF or 2 separate PDFs.
The display of the full size images must be customized and cannot be the default styles supplied by jQuery plugin.

Production
----------

Students will build an HTML and CSS version of the Photo Gallery they have designed.
The HTML and CSS should demonstrate the following techniques:

HTML
````
- Use of src and alt attributes of the <img> tag
- Use of <a> tags with href attribute for linking from thumbnail images to large versions

CSS
```
- Use of floats or absolute position for thumbnail layout
- Customized styling for full size image display

Javascript/jQuery
`````````````````
- jQuery attached to the page using a <script> tag
- Use of javascript such as a `jQuery Lightbox plugin <http://fancyapps.com/fancybox/>`_ for display
  of the full size image without leaving the page.

.. class:: super-section

----------------------
Project 3: Site Layout
----------------------

Students will design a basic website layout in the form of a wireframe (content design, color, typography 
and imagery are not required) and produce it using HTML/CSS. This project is designed to familiarize students
with CSS layout properties such as floating/clearing and positioning. 

Elements
--------

The following elements/sections are required in the layout:

- Masthead
  + Logo
  + Tagline
- Primary Navigation
  + Secondary Navigation as Dropdown Menu
- Primary Content Area
  + Level 1 heading 
  + At least 1 paragraph of dummy content
  + At least 1 link
- Secondary Content Area/Sidebar
- Footer
  + Paragraph with copyright symbol

Design
------

Students will create their design using Illustrator or Photoshop and submit the design as a PDF. The design should 
show how the second level navigation dropdown will appear. The layout must be a multi-column layout and it must be centered within the browser.

Production
----------

The HTML and CSS should demonstrate the following techniques:

HTML
````
- Container div with id attribute wrapped around entire site
- Masthead using the <header> tag with an id attribute
  + Logo in a div tag with an id attribute
  + Tagline in a paragraph tag with an id attribute
- Navigation in a <nav> tag with an id attribute
  + Primary/Secondary navigation as list items in a nested unordered list
- Primary and Secondary Content Areas as sections with ids
- Footer as <footer> tag with an id attribute
- <link> tag linking to external stylesheet

CSS
```
- Use of width and auto margins on container for centering layout
- Use of id selectors for styling layout elements
- Absolute positioning for placement of logo/tagline
- Floats for multi-column layout of primary/secondary content columns
- Clear for clearing footer
- CSS for dropdown navigation using `Sons of Suckerfish technique <http://www.htmldog.com/articles/suckerfish/dropdowns/>`_
- Basic typographic styles for 3 levels of headings, paragraphs and links (can be taken from resume)

.. class:: super-section

------------------------
Project 4: jQuery Plugin
------------------------

Students will select a `jQuery plugin <http://plugins.jquery.com/>`_ and create a single HTML 
page that shows a basic working implementation. This implementation must have some kind of
customization (for example changing the speed of a slideshow or any other plugin option).
As part of the process of implementing the plugin, students will write up a set of step-by-step 
instructions of what they did to get it to work. This will be included on the HTML page
they submit in the form of an ordered list.  Students will present their plugin to the class 
and discuss implementation challenges.

Instructions
------------

Example instructions for a slideshow plugin:

1. Add a link tag to the <head> of the document with jquery.js
2. Add a div tag with an id of "slideshow"
3. Add one or more img tags inside the slideshow div
4. Add a script tag after the slideshow div with the following initialization code

.. code-block:: javascript

   $('#slideshow').cycle();

5. Change the speed of the slideshow by setting the timeout option 

.. code-block:: javascript

   $('#slideshow').cycle({
       timeout: 5000
   });

