# About GIITS.html

This documentation provides an overview of the `GIITS.html` file, which serves as the HTML template for the GITS (GitHub Interaction and Tracking System) Flask web application. The HTML template is used to create the front-end user interface for interacting with various GitHub-related functions provided by the Flask application.

## Location of the code:
The code that implements the above-mentioned HTML functionality is located [here](/src/templates/GIITS.html).

## HTML Structure

The `GIITS.html` template has a simple HTML structure that includes a title, a stylesheet, a header, and various form elements for user interaction. Here's an overview of the key sections and elements within the HTML:

### Title
- `<title>`: The title of the web page, which is set to "GITS Homepage."

### Styles
- `<style>`: The `<style>` block contains inline CSS for styling the HTML elements. It defines the background color, text color, layout, and visibility of different form containers.

### Header
- `<h1>`: The main header of the page, which displays "GITS Homepage."

### Image Container
- `<div id="image-container">`: This container displays an animated GIF, which is loaded using the `{{ url_for('static', filename='image.gif') }}` syntax. The GIF is used for visual appeal. The gif is stored inside a static directory.

### Option Selection
- `<label>` and `<select>`: This section includes a dropdown menu labeled "Select an option," which allows users to choose from various GitHub-related actions.

### Form Containers
- Several `<div>` elements with distinct IDs, such as `form-container-create`, `form-container-clone`, `form-container-pull`, and so on, represent the form containers for different actions. These containers are initially set to `display: none` and become visible based on the selected option from the dropdown menu.

### Action Forms
- For each GitHub-related action, there is a corresponding `<form>` element inside the appropriate form container. These forms allow users to input the required information for the selected action, such as repository names, URLs, paths, and more.

## JavaScript Function
- The `<script>` section at the end of the HTML contains a JavaScript function, `toggleForm`, which is called when the user selects an option from the dropdown menu. This function controls the visibility of the form containers, displaying the relevant form based on the user's choice.

## How to Use GIITS.html

The `GIITS.html` file serves as the user interface for interacting with the GITS Flask application. To use the interface:

1. Open the web application by running the Flask application, as described in the "How to Run the Code" section of the `App.py` documentation listed [here](./app.md).

2. Access the web interface by navigating to `http://localhost:5020/` in a web browser.

3. Select an action from the dropdown menu.

4. Depending on your selection, the corresponding form will become visible, allowing you to input the required information for the chosen GitHub-related action.

5. Fill out the form and click the "Submit" button to initiate the selected action.

6. The Flask application will process the request and return a response, which will be displayed on the web page.

The `GIITS.html` file provides an easy-to-use interface for interacting with the GITS Flask application and simplifies the process of performing GitHub-related actions.

For any questions or issues, please refer to the documentation or contact the developer.
