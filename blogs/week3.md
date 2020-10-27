# HTML and CSS Foundations

## HTML

### Learned

1. Structure, Elements and Tags
2. Attributes
3. Forms
4.

### Structure, Elements and Tags

The '<html>' tag is the top element in the example, and </html> is the closing tag.
There is a heiarchy, for example: `<html>, <head>, <title>`. Children elements are nested under their parent element.

Block and Inline elements are important, specifically when it comes to styling.

```HTML
<html>
  <head>
    <title>Sample Title</title>
  </head>
  <body></body>
</html>
```

### Attributes

An opening tag supports attributes to add more detailed annotation to the element.
You will always find an attribute inside an opening tag separated by a space.

Id attributes can only be used to describe one element at a time. The `class` attribute can be used more than once to maybe group different elements together.

```HTML
<div id = "new-zealand" class = "content">
            <p>
                Intro: Consectetur dolore esse amet est qui irure id magna consectetur est ullamco sint.
            </p>
            <p>
                This is are <span>some images of <strong><em>New Zealand</em></strong></span>. It's not Australia and
                people will get mad if you call them the same place.
                So don't call them the same place.
            </p>
            <div>
            <a href="#"><img width = 450 src="https://www.telegraph.co.uk/content/dam/Travel/2018/December/Milford-Sound-GettyImages-875331434-xlarge.jpg" alt="Milford Sound, NZ" /></a>
            </div>
            <div>
                <a href="#"><img width = 450 src="https://www.switchbacktravel.com/sites/default/files/images/articles/Queenstown%2C%20New%20Zealand%20sunset.jpg" alt="Queenstown, NZ"></a>
            </div>
        </div>
```

### Forms

Form tags are used to identify the start and end of forms.
The fieldset is a good way to create groups of form controls that share the same purpose.
Many assistive technologies, like screen readers, will use legend element.

```HTML
<form>
    <fieldset>
        <legend>User Information</legend>
    <p>
      <label for="first-name"> First Name </label>
      <input type="text" name="first-name" id="first-name" />
    </p>
    <p>
      <label for="last-name"> Last Name </label>
      <input type="text" name="Last-name" id="Last-name" />
    </p>
    <p>
      <label for="address"> Home Address </label>
      <input type="text" name="address" id="address" />
    </p>
  </fieldset>
  <input type="submit" id="submit-button" value="submit" />
    </fieldset>
</form>
```

The `<label>` tag allows you to define a label from an `<input>` tag.
An `<input>` tag allows you to create form control widgets. The main attribute used with the `<input>` tage is _type_.

```HTML
<label for="name">User Name</label>
<input type="text" id="name" name="user-name" />

<!--Alternatively-->

<label>
  User Name
  <input type="text" id="name" name="user-name"/>
  <label></label
></label>
```

Main _Type_ Atributes
| Type | Description | Example |
| ----------| -----------------------------------------------------------------------------------------------------| ----------------------------|
| text | Allows user to input text. | ` <input type="text">`` | | checkbox | Allows single values to be selected/deselected. |  `<input type="checkbox">`` | | radio | Allows single value to be selected out of multiple choices with the same name value. | `<input type="radio">`` |
| range | Control for entering a value that isn't exactly important. Used with **min** and **max** attributes. | ` <input type="range">`` | | submit | Button that submits the form. |  `<input type="submit">`` |
