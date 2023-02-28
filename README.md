![Logo](https://user-images.githubusercontent.com/116521940/221938702-b978bac3-d7cc-4601-b114-de89ec592aaf.png)
# SpotifyAPI Search web-app

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This web app allows users to search for countries where the most popular song of an artist is available. Users need to type in the name of the artist in the input and click the "Search" button. Within 6 seconds, the app will open a page with a map that highlights available countries in green and unavailable ones in red. The map is created using the Folium library.

## Requirements
 - Python 3.7+
 - Django 3.0+
 - Folium 0.12+

## Installation
 1. Clone the repository.
 ```css
  git clone https://github.com/username/repo.git
 ```
 2. Navigate to the project directory.
```css
cd repo
```
 3. Install the required packages.
```css
pip install -r requirements.txt
```
 4. Run the server.
```css
python manage.py runserver
```
 5. Open your web browser and navigate to http://127.0.0.1:8000/ to use the app.

## Usage
 1. Type the name of the artist in the input box.
 2. Click the "Search" button.
 
![image](https://user-images.githubusercontent.com/116521940/221940597-8fcab692-1ace-411b-b62d-cc8e5ff104d1.png)

 3. Wait for 6 seconds while the app searches for the countries where the song is available.
 
 ![image](https://user-images.githubusercontent.com/116521940/221940663-f16376df-137e-4128-b6b4-7f68024edc76.png)
 
 4. Once the map is loaded, countries where the song is available will be highlighted in green, and those where it is unavailable will be highlighted in red.
 
 ![image](https://user-images.githubusercontent.com/116521940/221940760-40b41c12-7d73-4a31-8515-4ceae27fc211.png)
 
 5. Click here to see a live demo of the app.
 [Demo](https://denhumen0830.pythonanywhere.com/)

## Authors

- [@denhumen](https://github.com/denhumen)


## License
This project is licensed under the MIT License - see the LICENSE file for details.
