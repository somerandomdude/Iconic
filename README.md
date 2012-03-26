## Iconic is an open source icon set in raster, vector and font formats

### Iconic aims to be the most forward-thinking icon set around based on its support of forward facing display/deployment methods. Icons should not just be clear and attractive, they should be easy and flexible to work with. [Learn more about Iconic](http://somerandomdude.com/work/iconic/)

## Using Iconic

* SVG files can be found in the _vector/_ folder
* PNG files in all sizes and one color (black) can be found in the _raster/_ folder
* Fonts in two weights (stroke and fill) as well as demo HTML and CSS files can be found in the _font/_ folder
* Illustrator symbols can be found in the _etc/illustrator symbols_ folder
* Omnigraffle stencils can be found in the _etc/omnigraffle stencil_ folder

## Building Iconic

### Designing New Icons

All icons within the set are built around a strict grid. If you want to design new icons for the set, you can use the grid as your guide at _source/Template.ai_ (CS5 format). In addition, all the icons are available for reference and/or modification at _source/Iconic_all.ai_ (CS5 format).

### Generating Fonts

There are Python scripts to generate the Iconic font files (including demo HTML/CSS files) at _scripts/font creation/_. The scripts [require FontForge](http://fontforge.sourceforge.net/) and I have only been able to get them to run on Linux at this point.

### Generating PNGs

Iconic has two different JSX ExtendScripts for generating transparent PNGs. The scripts are run in Adobe Illustrator [Learn more here](http://help.adobe.com/en_US/illustrator/cs/using/WS714a382cdf7d304e7e07d0100196cbc5f-62a3a.html). To generate all icons at all sizes and colors, use _scripts/raster creation/SaveLayersAsPNG.jsx_ (this script will take a long time). To generate icons at a custom color and/or a subset of sizes use _scripts/raster creation/SaveLayersAsCustomPNG.jsx_

### Generating SVGs

You can also generate SVGs automatically with a JSX ExtendScript. The script can be found at _scripts/vector creation/SaveLayersAsSVG.jsx_ The SVG files are all generated at 32 pixels in black. 

### Generating a SWC (Depreciated)

All AS3 files and ANT build scripts can be found at  _scripts/swc creation/_

*This feature is no longer actively updated by me (feel free to fork and update)*

##Licensing 

###Icons
All icons (located in the _vector/_, _raster/_, _source/_ and _etc/_ directories) are licensed under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/). If you use these icons, please add a link to Iconic [(http://somerandomdude.com/work/iconic/)](http://somerandomdude.com/work/iconic/) somewhere on your site or in your app.

###Fonts
All fonts (located in the _fonts/_ directory) are licensed under the [SIL Open Font License](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)

###Scripts
All scripts (located in the _scripts/_ directory) are licensed under the [GNU Public License](http://www.gnu.org/licenses/gpl.html)



